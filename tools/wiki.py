#!/usr/bin/env python3
"""The one tool of the machine (CLAUDE.md). python3 stdlib + curl + pdftotext.

usage: wiki.py status                          one screen
       wiki.py harvest                         new candidates (queries, then the arXiv sweep) → .claude/runs/batch.json
       wiki.py judge   --input F               the selector's verdicts {"verdicts": [{id, verdict, why}]}
       wiki.py fetch   [--limit N]             download + extract every selected work without a file
       wiki.py next                            the reading list: selected, unread, with text
       wiki.py apply   [--input F]             a round's packages and reviews → keep or revert, mark read, queue queries
                                               (default: .claude/runs/round/<key>.package.json + <key>.review.json, then cleared)
       wiki.py check   [--file F]              the note contract; exit 1 on failure
       wiki.py commit                          check, then commit the round with its numbers
       wiki.py query   add "q" | --input F --origin chat|owner|explore|reader [--from KEY]   (F: {"queries": [...]})
       wiki.py null    --key K --why "…"       the owner's verdict on a work
       wiki.py hook    post-write|stop         Claude Code hooks (JSON on stdin; exit 2 blocks)
"""
import calendar, json, math, os, re, subprocess, sys, time, unicodedata
from datetime import date as D, timedelta

ROOT = os.environ.get("WIKI_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
META = os.path.join(ROOT, "meta")
ARCHIVE = os.path.join(META, "archive")
CONFIG, SOURCES, QUERIES, SWEEP = (os.path.join(META, f) for f in ("config.json", "sources.jsonl", "queries.jsonl", "sweep.json"))
RUNS = os.path.join(ROOT, ".claude", "runs")
ORIGINS = ("chat", "owner", "reader", "explore", "seed")   # also the order queries are searched in


def today():
    return D.today().isoformat()


def rel(p):
    return os.path.relpath(p, ROOT)


# ---- state: three plain files ------------------------------------------------------------------------------------------

def load_json(p, default=None):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else default


def save_json(p, obj):
    json.dump(obj, open(p + ".tmp", "w", encoding="utf-8"), indent=1, ensure_ascii=False); os.replace(p + ".tmp", p)


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()] if os.path.exists(p) else []


def save_jsonl(p, rows):
    with open(p + ".tmp", "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(p + ".tmp", p)


def sources():
    return {r["key"]: r for r in load_jsonl(SOURCES)}


def save_sources(S):
    save_jsonl(SOURCES, S.values())


def text_path(key):
    return os.path.join(ARCHIVE, key + ".txt")


# ---- search backends ---------------------------------------------------------------------------------------------------

OPENALEX, ARXIV_API = "https://api.openalex.org/works", "https://export.arxiv.org/api/query"
STOP = {"or", "and", "the", "of", "a", "an", "in", "on", "for", "to", "as", "when", "with", "before", "by", "from", "at", "via", "into",
        "under", "over", "its", "their", "than", "that", "this", "what", "how", "why", "is", "are", "be"}
GENERIC = {"language", "languages", "model", "models", "large", "llm", "llms", "system", "systems", "agent", "agents", "based", "using",
           "learning", "method", "methods", "approach", "task", "tasks", "data", "neural", "network", "networks", "deep"}


def curl(url, out=None):
    args = ["curl", "-sL", "--max-time", "40", "-A", "Mozilla/5.0 (wiki harvest; curl)"] + (["-o", out] if out else []) + [url]
    r = subprocess.run(args, capture_output=True, text=not out)
    return r.returncode == 0 and (r.stdout if not out else os.path.exists(out) and os.path.getsize(out) > 0)


def _q(s):
    from urllib.parse import quote
    return quote(s, safe="")


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()).strip()


def arxiv_id(url):
    m = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?", url or "")
    return m.group(1) if m else None


def openalex(query, n=20):
    url = (f"{OPENALEX}?search={_q(query)}&per-page={n}&mailto=wiki-harvest@example.org&filter=type:article|preprint|book-chapter|book|review|dissertation"
           "&select=id,doi,title,publication_year,open_access,primary_location,authorships,abstract_inverted_index")
    try:
        d = json.loads(curl(url) or "{}")
    except json.JSONDecodeError:
        return []
    out = []
    for r in d.get("results", []):
        doi = (r.get("doi") or "").replace("https://doi.org/", "") or None
        oa = (r.get("open_access") or {}).get("oa_url")
        pos = {p: w for w, ps in (r.get("abstract_inverted_index") or {}).items() for p in ps}
        out.append({"id": f"doi:{doi}" if doi else r["id"], "doi": doi, "arxiv": arxiv_id(oa), "title": r.get("title") or "", "year": r.get("publication_year"),
                    "authors": [a.get("author", {}).get("display_name", "") for a in r.get("authorships", [])][:6],
                    "url": oa or (doi and f"https://doi.org/{doi}") or (r.get("primary_location") or {}).get("landing_page_url"),
                    "abstract": " ".join(pos[i] for i in sorted(pos))[:1500]})
    return out


def _arxiv_entries(xml):
    out = []
    for e in re.findall(r"<entry>(.*?)</entry>", xml or "", re.S):
        g = lambda tag: (re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", e, re.S) or [None, ""])[1]
        aid = arxiv_id(g("id").strip())
        if aid:
            out.append({"id": f"arxiv:{aid}", "doi": None, "arxiv": aid, "title": re.sub(r"\s+", " ", g("title")).strip(),
                        "year": int(g("published")[:4]) if g("published") else None, "authors": re.findall(r"<name>(.*?)</name>", e)[:6],
                        "url": f"https://arxiv.org/abs/{aid}", "abstract": re.sub(r"\s+", " ", g("summary")).strip()[:1500]})
    return out


def arxiv(query, n=20):
    return _arxiv_entries(curl(f"{ARXIV_API}?search_query=all:{_q(query)}&max_results={n}&sortBy=relevance"))


def arxiv_day(cats, day):
    d, c, out = day.replace("-", ""), "%20OR%20".join(f"cat:{x}" for x in cats), []
    for start in range(0, 5000, 500):
        got = _arxiv_entries(curl(f"{ARXIV_API}?search_query=({c})%20AND%20submittedDate:%5B{d}0000%20TO%20{d}2359%5D"
                                  f"&start={start}&max_results=500&sortBy=submittedDate&sortOrder=descending"))
        out += got; time.sleep(3)
        if len(got) < 500:
            break
    return out


def _stems(text):
    return {_stem(w) for w in re.findall(r"[A-Za-z][A-Za-z-]{3,}", text) if w.lower() not in STOP and w.lower() not in GENERIC}


def _stem(w):
    w = w.lower()
    for suf in ("ations", "ation", "ing", "ies", "ers", "er", "ed", "es", "s"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def prefilter(queries):
    """The sweep's vocabulary is the queries: a listed work passes when it carries ≥75 % (and ≥2) of one query's stems
    (measured 2026-10-06 on one arXiv day, 523 works, 343 queries: 0.6 passes 16 %, 0.75 passes 4 %)."""
    terms = [st for st in (_stems(q["q"]) for q in queries) if len(st) >= 2]
    def match(text):
        words = {_stem(w) for w in re.findall(r"[A-Za-z][A-Za-z-]{3,}", text)}
        return any(len(st & words) >= max(2, math.ceil(len(st) * 0.75)) for st in terms)
    return match


# ---- harvest / judge ---------------------------------------------------------------------------------------------------

def slug(id_):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", id_.lower().replace("https://", "").replace("http://", ""))).strip("-")[:80]


def horizon(cfg):
    """The sweep's months, newest first: sweep.months back from sweep.from."""
    y, m = map(int, cfg["sweep"]["from"].split("-")); out = []
    for _ in range(int(cfg["sweep"]["months"])):
        out.append(f"{y:04d}-{m:02d}"); y, m = (y, m - 1) if m > 1 else (y - 1, 12)
    return out


def harvest(date):
    cfg, S, Q = load_json(CONFIG), sources(), load_jsonl(QUERIES)
    known = {x for s in S.values() for x in (s["key"], s.get("id"), s.get("doi") and f"doi:{s['doi']}", s.get("arxiv") and f"arxiv:{s['arxiv']}") if x}
    titles = {norm_title(s.get("title")) for s in S.values()}
    n = cfg["candidates_per_round"]; stats = {"queries": [], "sweep_days": [], "new": 0}
    unread = sum(1 for s in S.values() if s["verdict"] == "select" and not s.get("read") and not s.get("fetch_failed"))
    pending = lambda: sum(1 for s in S.values() if s["verdict"] == "pending")

    def record(c, found_by):
        if c["id"] in known or norm_title(c["title"]) in titles or not c["title"]:
            return False
        key = slug(c["id"])
        if key in S:
            return False
        S[key] = {"key": key, "id": c["id"], "doi": c.get("doi"), "arxiv": c.get("arxiv"), "title": c["title"], "year": c.get("year"),
                  "authors": c.get("authors") or [], "url": c.get("url"), "abstract": c.get("abstract", ""), "found_by": found_by, "added": date,
                  "verdict": "pending", "why": None, "read": None, "notes": [], "file": None}
        if not (c.get("abstract") or "").strip():   # nothing to judge from: the selector would only refuse it
            S[key].update(verdict="null", why="no abstract", judged=date); S[key].pop("abstract")
        known.add(c["id"]); titles.add(norm_title(c["title"])); stats["new"] += 1
        return True

    for s in S.values():
        if s["verdict"] == "pending" and not (s.get("abstract") or "").strip():
            s.update(verdict="null", why="no abstract", judged=date); s.pop("abstract", None)
    if unread < 3 * cfg["reads_per_round"] and pending() < n:   # reading and judging first: no harvest while either backlog is full
        todo = sorted([q for q in Q if not q.get("searched")], key=lambda q: (ORIGINS.index(q.get("origin", "seed")), q.get("added", "")))
        for q in todo[: cfg["queries_per_round"]]:
            res = openalex(q["q"]) or arxiv(q["q"])
            q["searched"] = date; q["found"] = sum(record(c, f"query: {q['q']}") for c in res)
            stats["queries"].append([q["q"], len(res), q["found"]])
        stats["explore"] = len(todo) <= cfg["queries_per_round"]   # the queue is (nearly) empty: the explorer proposes more
        sw = load_json(SWEEP, {}); months = horizon(cfg); oldest = months[-1] + "-01"
        cur = sw.get("cursor") or f"{months[0]}-{calendar.monthrange(*map(int, months[0].split('-')))[1]:02d}"
        match = prefilter(Q); swept = 0   # the sweep walks every round, whatever the queries found: its share of a batch
        while swept < n * cfg.get("sweep_share", 0.5) and cur >= oldest:
            listed = arxiv_day(cfg["sweep"]["cats"], cur)
            hits = [c for c in listed if match(c["title"] + " " + c["abstract"])]
            got = sum(record(c, f"sweep: {cur}") for c in hits); swept += got
            stats["sweep_days"].append([cur, len(listed), got])
            cur = (D.fromisoformat(cur) - timedelta(days=1)).isoformat(); sw["cursor"] = cur
        save_json(SWEEP, sw); save_jsonl(QUERIES, Q)
    else:
        stats["skipped"] = f"backlog: {unread} selected works unread, {pending()} candidates pending"
    save_sources(S)
    note_stats(found=stats["new"], sweep=[d[0] for d in stats["sweep_days"]])
    batch = [{"id": s["key"], "title": s["title"], "year": s.get("year"), "authors": s.get("authors", [])[:3], "abstract": s.get("abstract", "")}
             for s in S.values() if s["verdict"] == "pending"][:n]
    os.makedirs(RUNS, exist_ok=True); open(os.path.join(RUNS, "batch.json"), "w").write('{"candidates": [\n' + ",\n".join(json.dumps(c, ensure_ascii=False) for c in batch) + "\n]}\n")   # one per line: the selector's Read truncates long lines
    sw = load_json(SWEEP, {}); stats["sweep_done"] = (sw.get("cursor") or "9") < horizon(cfg)[-1] + "-01"
    stats["cursor"] = sw.get("cursor")
    return {**stats, "batch": rel(os.path.join(RUNS, "batch.json")), "n": len(batch)}


def judge(verdicts, date):
    S, Q = sources(), {q["q"]: q for q in load_jsonl(QUERIES)}; n = {"select": 0, "null": 0, "unknown": 0}
    for v in verdicts:
        s = S.get(v.get("id"))
        if not s or v.get("verdict") not in ("select", "null"):
            n["unknown"] += 1; continue
        s.update(verdict=v["verdict"], why=v.get("why"), judged=date); s.pop("abstract", None); n[v["verdict"]] += 1
        q = Q.get((s.get("found_by") or "").removeprefix("query: "))
        if q and v["verdict"] == "select":
            q["selected"] = q.get("selected", 0) + 1
    save_sources(S); save_jsonl(QUERIES, Q.values())
    note_stats(select=n["select"], judged=n["select"] + n["null"])
    return n


# ---- fetch -------------------------------------------------------------------------------------------------------------

STUB = re.compile(r"cloudflare|just a moment|403 forbidden|access denied|enable javascript|are you a robot|captcha|attention required", re.I)


def html_text(path):
    """Visible text, one line per block element, wrapped at 100 columns (readers read line slices)."""
    import html, textwrap
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", open(path, encoding="utf-8", errors="ignore").read(), flags=re.S | re.I)
    t = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"</?(p|div|br|h\d|li|tr|section|article|blockquote|pre)\b[^>]*>", "\n", t, flags=re.I)))
    paras = [re.sub(r"[ \t]+", " ", l).strip() for l in t.split("\n")]
    return "\n".join(textwrap.fill(l, 100, break_on_hyphens=False, break_long_words=False) for l in paras if l)


def extract_text(path):
    if path.endswith(".pdf"):
        out = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True, timeout=300).stdout
    else:
        out = html_text(path)
    return re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+\n", "\n", out.replace("\r\n", "\n").replace("\r", "\n")))


def fetch(date, limit=None):
    """Open-access PDFs (arXiv and other open hosts) and HTML snapshots; a paywall or a bot wall is refused, never bypassed."""
    S = sources(); os.makedirs(ARCHIVE, exist_ok=True); got = {"pdf": [], "html": [], "failed": []}
    todo = [s for s in S.values() if s["verdict"] == "select" and not s.get("file") and not s.get("fetch_failed")]
    for s in todo[: limit or None]:
        k = s["key"]; aid = s.get("arxiv") or arxiv_id(s.get("url"))
        url = f"https://arxiv.org/pdf/{aid}" if aid else s.get("url") or (s.get("doi") and f"https://doi.org/{s['doi']}")
        tmp = os.path.join(ARCHIVE, f".{k}.tmp")
        ok = bool(url) and curl(url, tmp)
        m = subprocess.run(["file", "-b", "--mime-type", tmp], capture_output=True, text=True).stdout.strip() if ok else ""
        ext = "pdf" if m == "application/pdf" else "html" if m.startswith("text/") else None
        if ext == "html" and (STUB.search(open(tmp, encoding="utf-8", errors="ignore").read(20000)) or len(html_text(tmp)) < 1500):
            ext = None; m = "stub: paywall, bot wall or landing page"
        if not ext:
            if os.path.exists(tmp):
                os.remove(tmp)
            s["fetch_failed"] = f"{date}: {m or 'no url or download failed'}"; got["failed"].append(k); continue
        dest = os.path.join(ARCHIVE, f"{k}.{ext}"); os.replace(tmp, dest); s["file"] = f"{k}.{ext}"
        text = extract_text(dest)
        if len(text.strip()) < 200:
            s["fetch_failed"] = f"{date}: no text layer"; got["failed"].append(k); continue
        open(text_path(k), "w", encoding="utf-8").write(text); got[ext].append(k)
        save_sources(S)
    save_sources(S)
    return {k: len(v) for k, v in got.items()} | {"failed_keys": got["failed"]}


def next_reads():
    cfg, S = load_json(CONFIG), sources()
    U = [s for s in S.values() if s["verdict"] == "select" and not s.get("read") and os.path.exists(text_path(s["key"]))]
    U.sort(key=lambda s: (-(s.get("year") or 0), s.get("added") or ""), reverse=False)
    return [{"key": s["key"], "title": s["title"], "year": s.get("year"), "authors": s.get("authors", [])[:3], "text": rel(text_path(s["key"])),
             "lines": sum(1 for _ in open(text_path(s["key"]), encoding="utf-8"))} for s in U[: cfg["reads_per_round"]]]


# ---- apply: keep what passed, revert the rest -------------------------------------------------------------------------

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, cwd=ROOT)


def tracked(path):
    return git("ls-files", "--error-unmatch", path).returncode == 0


def revert(path):
    p = os.path.join(ROOT, path)
    if tracked(path):
        git("checkout", "HEAD", "--", path)
    elif os.path.exists(p):
        os.remove(p)


def add_query(Q, q, origin, date, frm=None):
    q = re.sub(r"\s+", " ", q or "").strip()
    if not q or any(x["q"].lower() == q.lower() for x in Q):
        return False
    Q.append({"q": q, "origin": origin, "from": frm, "added": date, "searched": None, "found": 0, "selected": 0})
    return True


def collect_round():
    """The readers' and reviewers' files for this round → {"items": [...]}; the directory is emptied after reading."""
    d = os.path.join(RUNS, "round"); items = {}
    for it in load_json(os.path.join(d, "_workflow.json"), []):   # what a workflow collected; the agents' own files win
        items[it["key"]] = {"key": it["key"], "package": it.get("package"), "review": it.get("review")}
    for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        key, _, kind = f[:-5].rpartition(".")
        if f.endswith(".json") and kind in ("package", "review"):
            got = load_json(os.path.join(d, f))
            if got:
                items.setdefault(key, {"key": key, "package": None, "review": None})[kind] = got
    for k in load_json(os.path.join(RUNS, "reading.json"), []):   # a work `next` listed whose reader wrote nothing failed
        items.setdefault(k, {"key": k, "package": None, "review": None})
    import shutil; shutil.rmtree(d, ignore_errors=True)
    return {"items": list(items.values())}


def apply(rnd, date):
    """rnd = {"items": [{"key", "package": {files, queries, nothing} | null, "review": {"notes": [{file, verdict, why}]} | null}]}.
    A note that a review passes and the contract accepts is kept; everything else under wiki/ that changed is reverted."""
    S, Q = sources(), load_jsonl(QUERIES); out = {"new": [], "revised": [], "dropped": [], "queries": 0, "unread": []}
    keep = set()
    for it in rnd.get("items", []):
        s, pkg = S.get(it["key"]), it.get("package")
        if not s:
            continue
        if not pkg:   # the reader returned nothing: read again next round; set aside after two failures
            s["attempts"] = s.get("attempts", 0) + 1; out["unread"].append(it["key"])
            if s["attempts"] >= 2:
                s["read"] = date; s["why_unread"] = "reader failed twice"
            continue
        verdicts = {os.path.basename(n["file"]): n for n in (it.get("review") or {}).get("notes", [])}
        for f in pkg.get("files", []):
            f = "wiki/" + os.path.basename(f); v = verdicts.get(os.path.basename(f), {"verdict": "drop", "why": "not reviewed"})
            bad = check_file(os.path.join(ROOT, f)) if os.path.exists(os.path.join(ROOT, f)) else ["missing"]
            if v["verdict"] == "pass" and not bad:
                keep.add(f); (out["revised"] if tracked(f) else out["new"]).append(os.path.basename(f)[:-3])
                s.setdefault("notes", []).append(os.path.basename(f)[:-3])
            else:
                out["dropped"].append({"note": os.path.basename(f)[:-3], "why": v.get("why") or "; ".join(bad)[:300]})
        for q in pkg.get("queries", [])[:3]:
            out["queries"] += add_query(Q, q, "reader", date, it["key"])
        s["read"] = date; s["notes"] = sorted(set(s.get("notes", [])))
        if pkg.get("nothing"):
            s["why_nothing"] = pkg["nothing"][:300]
    changed = {l[3:].strip().strip('"') for l in git("status", "--porcelain", "--", "wiki").stdout.splitlines()}
    for f in changed - keep:
        revert(f)
    notes = {f[:-3] for f in os.listdir(WIKI) if f.endswith(".md")}
    for f in keep:   # a kept note may link a sibling the review dropped: the link becomes plain text
        p = os.path.join(ROOT, f); t = open(p, encoding="utf-8").read()
        t2 = LINK.sub(lambda m: m.group(0) if m.group(1).strip() in notes else m.group(1), t)
        if t2 != t:
            open(p, "w", encoding="utf-8").write(t2)
    save_sources(S); save_jsonl(QUERIES, Q)
    note_stats(read=sum(1 for it in rnd.get("items", []) if it.get("package")), new=len(out["new"]),
               revised=len(set(out["revised"])), dropped=len(out["dropped"]), queries=out["queries"])
    return out


STATS = os.path.join(RUNS, "stats.json")


def note_stats(**kw):
    """Accumulate the round's numbers for its commit message (.claude/runs/stats.json, cleared by commit)."""
    st = load_json(STATS, {})
    for k, v in kw.items():
        st[k] = st.get(k, [] if isinstance(v, list) else 0) + v
    os.makedirs(RUNS, exist_ok=True); save_json(STATS, st)


def commit(date):
    """check, then one commit for the round: `grow: <date> | sweep a..b | select x/y | read n | notes +a ~b -c | queries +q`."""
    bad = check()
    if bad:
        return {"committed": False, "failing": {f: F[:2] for f, F in list(bad.items())[:10]}}
    st = load_json(STATS, {}); sw = st.get("sweep") or []
    msg = (f"grow: {date}" + (f" | sweep {sw[0]}..{sw[-1]}" if sw else "") + f" | select {st.get('select', 0)}/{st.get('judged', 0)}"
           f" | read {st.get('read', 0)} | notes +{st.get('new', 0)} ~{st.get('revised', 0)} -{st.get('dropped', 0)} | queries +{st.get('queries', 0)}")
    git("add", "-A"); r = git("commit", "-q", "-m", msg + "\n\nCo-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>")
    if r.returncode == 0 and os.path.exists(STATS):
        os.remove(STATS)
    return {"committed": r.returncode == 0, "message": msg, "error": (r.stdout + r.stderr)[-300:] if r.returncode else None}


# ---- the note contract -------------------------------------------------------------------------------------------------

FN_REF = re.compile(r"\[\^([^\]\s]+)\](?!:)")
FN_DEF = re.compile(r"^\[\^([^\]\s]+)\]:\s*(.*)$", re.M)
CITE = re.compile(r'^([a-z0-9][a-z0-9-]*)(?:\s+—\s+"(.+)")?\s*$')
LINK = re.compile(r"\[\[([^\]|#\n\\]+)(?:#[^\]|\n]*)?(?:\\?\|[^\]\n]*)?\]\]")
_TEXT = {}


def _norm(s):
    s = unicodedata.normalize("NFKC", s).lower()
    return re.sub(r"\s+", " ", re.sub(r"[-­‐‑]\s*", "", s)).strip()


def quote_found(key, quote):
    if key not in _TEXT:
        p = text_path(key)
        _TEXT[key] = _norm(open(p, encoding="utf-8").read()) if os.path.exists(p) else None
    return _TEXT[key] is not None and _norm(quote) in _TEXT[key]


def parse(path):
    t = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not m:
        return None, t
    meta = {}
    for line in m.group(1).split("\n"):
        k, _, v = line.partition(":"); v = v.strip()
        try:
            meta[k.strip()] = json.loads(v) if v[:1] in '["' else v
        except json.JSONDecodeError:
            meta[k.strip()] = v
    return meta, t[m.end():]


def write_note(path, meta, body):
    fm = "\n".join(f"{k}: {json.dumps(meta[k], ensure_ascii=False)}" for k in ("description", "aliases", "sources"))
    open(path, "w", encoding="utf-8").write(f"---\n{fm}\n---\n{body.lstrip(chr(10))}")


def check_file(path, notes=None, known=None):
    """The contract (CLAUDE.md): returns the list of failures (empty = ok)."""
    notes = notes if notes is not None else {f[:-3] for f in os.listdir(WIKI) if f.endswith(".md")}
    known = known if known is not None else set(sources())
    meta, body = parse(path); F = []
    if meta is None:
        return ["no frontmatter"]
    if set(meta) != {"description", "aliases", "sources"}:
        F.append(f"frontmatter keys must be description, aliases, sources (got {sorted(meta)})")
    d = meta.get("description") or ""
    if not 80 <= len(d) <= 200:
        F.append(f"description is {len(d)} chars (80–200)")
    if not isinstance(meta.get("aliases"), list) or not isinstance(meta.get("sources"), list) or not meta.get("sources"):
        F.append("aliases must be a list; sources a non-empty list")
    if not re.search(r"^# \S", body, re.M):
        F.append("no # title")
    if not re.search(r"^## Limits\s*$", body, re.M):
        F.append("no ## Limits")
    prose = re.sub(r"```.*?```", "", body, flags=re.S)
    for l in sorted(set(LINK.findall(prose))):
        if l.strip() not in notes:
            F.append(f"link [[{l}]] does not resolve")
    rel_ = re.search(r"^## Related\s*$(.*?)(?=^## |^\[\^|\Z)", prose, re.M | re.S)
    if not rel_ or not LINK.search(rel_.group(1)):
        F.append("## Related needs a [[link]]")
    defs = dict(FN_DEF.findall(prose)); refs = set(FN_REF.findall(prose))
    if not defs:
        F.append("no footnote: every note cites its source")
    for r in sorted(refs - set(defs)):
        F.append(f"footnote [^{r}] has no definition")
    for fid, txt in defs.items():
        m = CITE.match(txt.strip())
        if not m:
            F.append(f'[^{fid}] must be `key` or `key — "exact quote"`'); continue
        key, quote = m.groups()
        if key not in (meta.get("sources") or []) or key not in known:
            F.append(f"[^{fid}] cites {key}: not in sources:/meta/sources.jsonl")
        elif quote and not quote_found(key, quote):
            F.append(f"[^{fid}] quote not found in meta/archive/{key}.txt")
    return F


def check(file=None):
    notes = {f[:-3] for f in os.listdir(WIKI) if f.endswith(".md")}; known = set(sources())
    files = [file] if file else [os.path.join(WIKI, n + ".md") for n in sorted(notes)]
    return {rel(f): F for f in files if (F := check_file(f, notes, known))}


# ---- status, hooks -----------------------------------------------------------------------------------------------------

def status():
    cfg, S, Q, sw = load_json(CONFIG), sources(), load_jsonl(QUERIES), load_json(SWEEP, {})
    v = {}
    for s in S.values():
        v[s["verdict"]] = v.get(s["verdict"], 0) + 1
    sel = [s for s in S.values() if s["verdict"] == "select" and not s.get("read")]
    q = {o: sum(1 for x in Q if x.get("origin") == o and not x.get("searched")) for o in ORIGINS}
    months = horizon(cfg)
    print(f"notes {len([f for f in os.listdir(WIKI) if f.endswith('.md')])} · works {len(S)} {v}")
    print(f"to read {len(sel)} ({sum(1 for s in sel if os.path.exists(text_path(s['key'])))} with text, {sum(1 for s in sel if s.get('fetch_failed'))} unfetchable)")
    print(f"queries {len(Q)} · unsearched {q}")
    print(f"sweep {months[-1]}…{months[0]} · cursor {sw.get('cursor')} · cats {len(cfg['sweep']['cats'])}")
    print("last: " + git("log", "-1", "--format=%h %s").stdout.strip())


def hook(mode):
    try:
        p = json.load(sys.stdin)
    except Exception:
        p = {}
    if mode == "post-write":
        f = os.path.abspath((p.get("tool_input") or {}).get("file_path") or "")
        if os.path.dirname(f) == WIKI and f.endswith(".md") and os.path.exists(f) and (F := check_file(f)):
            sys.stderr.write(f"{rel(f)} breaks the note contract (CLAUDE.md):\n- " + "\n- ".join(F) + "\n"); sys.exit(2)
    elif mode == "stop" and not p.get("stop_hook_active"):
        bad = check()
        if bad:
            sys.stderr.write(f"wiki.py check: {len(bad)} notes fail — fix or revert before stopping:\n" +
                             "\n".join(f"- {f}: {'; '.join(F)[:300]}" for f, F in list(bad.items())[:15]) + "\n"); sys.exit(2)


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    cmd, date = (a[0] if a else ""), opt("--date", today())
    J = lambda o: print(json.dumps(o, ensure_ascii=False))   # one line: what a workflow's runner returns
    if cmd == "status":
        status()
    elif cmd == "harvest":
        J(harvest(date))
    elif cmd == "judge":
        J(judge(load_json(opt("--input"))["verdicts"], date))
    elif cmd == "fetch":
        J(fetch(date, int(opt("--limit") or 0) or None))
    elif cmd == "next":
        R = next_reads(); os.makedirs(RUNS, exist_ok=True); save_json(os.path.join(RUNS, "reading.json"), [r["key"] for r in R]); J(R)
    elif cmd == "apply":
        J(apply(load_json(opt("--input")) if "--input" in a else collect_round(), date))
    elif cmd == "commit":
        J(commit(date))
    elif cmd == "check":
        bad = check(opt("--file"))
        for f, F in bad.items():
            print(f"{f}: " + "; ".join(F))
        print("ok" if not bad else f"{len(bad)} notes fail"); sys.exit(1 if bad else 0)
    elif cmd == "query" and a[1:2] == ["add"]:
        Q = load_jsonl(QUERIES)
        qs = load_json(opt("--input"))["queries"] if "--input" in a else [a[2]]
        n = sum(add_query(Q, q, opt("--origin", "owner"), date, opt("--from")) for q in qs); save_jsonl(QUERIES, Q)
        print(f"added {n}/{len(qs)}")
    elif cmd == "null":
        S = sources(); s = S[opt("--key")]; s.update(verdict="null", why=f"owner: {opt('--why', '')}"); save_sources(S); print("ok")
    elif cmd == "hook":
        hook(a[1])
    else:
        print(__doc__); sys.exit(1)
