<div align="center">

<img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Logo" height="48" />

# Python Master Handbook

**A live "proof of work" tracking daily algorithmic practice, core language fundamentals, and hands-on Python projects.**

<!-- DO NOT REMOVE THE COMMENTS BELOW. THEY ARE USED BY GITHUB ACTIONS TO AUTO-UPDATE THE COUNTS -->

<!-- QUESTIONS_COUNT:START -->
<img src="https://img.shields.io/badge/Questions_Created-20-blue?style=for-the-badge" alt="Questions Count" />
<!-- QUESTIONS_COUNT:END -->
&nbsp;
<!-- PROJECTS_COUNT:START -->
<img src="https://img.shields.io/badge/Main_Projects-1-success?style=for-the-badge" alt="Projects Count" />
<!-- PROJECTS_COUNT:END -->

<br/>

</div>

---

## About This Repo

This is a multi-project Python learning repo. Each **main project** is a real, production-grade system built step-by-step from isolated practice questions. Finish all questions → build each module → wire them into the final runnable app. Complete one main project, then move to the next.

**Current progress:** &nbsp; 🔨 Project 1 — PyMart Inventory & Analytics Engine &nbsp;|&nbsp; Questions 1–20 &nbsp;|&nbsp; 5 modules

| # | Main Project | Questions | Status |
|:---:|:---|:---:|:---:|
| 1 | **[PyMart Inventory & Analytics Engine](./projects/pro-final-pymart/about.txt)** — multi-source inventory data pipeline | ques 1–20 | 🔨 In Progress |
| 2 | _(coming after Project 1 completes)_ | — | ⬜ |

**How to use:**
1. Expand a project row below.
2. Solve every question in the left column.
3. Build every function in the right column.
4. Complete all modules → run the final project.
5. Start the next main project.

---

## 🗺️ The Road to PyMart

```
 ques 1–6          ques 7–10         ques 11–13        ques 14–18        ques 19–20
    │                  │                  │                  │                 │
    ▼                  ▼                  ▼                  ▼                 ▼
[pro-1]            [pro-2]            [pro-3]            [pro-4]         [pro-final]
Py Utils   →   Data Normalizer  →  RBAC Engine  →  Analytics Engine  →   PyMart Engine
```

---

<table width="100%" border="1">
<tr>
<td align="center"><br/>

## 🚀 Project 1 &nbsp;—&nbsp; PyMart Inventory & Analytics Engine &nbsp;·&nbsp; `pro-final-pymart`

**What you'll achieve:** Build a complete inventory data pipeline from scratch. Raw stock/order data from 3 sources (CSV exports, a JSON supplier API, and a legacy XML-like nested feed) enters the system, gets normalized to one unified schema, passes through a role-based security layer that masks sensitive fields per user role, flows into an analytics engine generating pivot tables and running reports, and streams out as a lazily-evaluated report you can serialize safely to JSON. You finish by running one command — `python projects/pro-final-pymart/main.py` — that executes the entire pipeline end-to-end. A real, demonstrable portfolio piece.

**Build path:** &nbsp; `1.1 Py Utils` &nbsp;→&nbsp; `1.2 Data Normalizer` &nbsp;→&nbsp; `1.3 RBAC Engine` &nbsp;→&nbsp; `1.4 Analytics Engine` &nbsp;→&nbsp; `1.Final PyMart Engine`

<br/>

</td>
</tr>
<tr>
<td>

<details>
<summary><strong>📦 1.1 &nbsp;—&nbsp; Py Utility Belt &nbsp;·&nbsp; <code>pro-1-py-utils</code></strong> &nbsp;&nbsp;┆&nbsp;&nbsp; ques 1–6 &nbsp;&nbsp;┆&nbsp;&nbsp; 🔽 click to open</summary>

<br/>

**What you will gain:** You build the utility functions every real Python codebase relies on — deep copying, flattening nested data, decorator-based composition, caching results with expiry, and currying. After this module you will understand how libraries like `toolz` and `functools` work internally, and every module you build after this will import from here.

<br/>

<table>
<tr>
<th>📝 Questions &nbsp;— solve all 6 first</th>
<th>🔨 Functions to Build &nbsp;·&nbsp; <a href="./projects/pro-1-py-utils/about.txt">open project guide →</a></th>
</tr>
<tr>
<td valign="top">

| # | File | What to Learn |
|:---:|:---|:---|
| 1 | [ques-1-deep-copy](./question-practice/ques-1-deep-copy.py) | Recursive deep copy |
| 2 | [ques-2-flatten-dict](./question-practice/ques-2-flatten-dict.py) | Dot-notation dict flattening |
| 3 | [ques-3-flatten-list](./question-practice/ques-3-flatten-list.py) | Arbitrary-depth list flattening |
| 4 | [ques-4-pipe-compose](./question-practice/ques-4-pipe-compose.py) | Decorator-based function composition |
| 5 | [ques-5-memoize-ttl](./question-practice/ques-5-memoize-ttl.py) | TTL result caching decorator |
| 6 | [ques-6-curry-partial](./question-practice/ques-6-curry-partial.py) | Curry & partial application |

</td>
<td valign="top">

| Function to Build | Needs |
|:---|:---:|
| `deep_copy(value)` | ques-1 |
| `flatten_dict(d, prefix)` | ques-2 |
| `flatten_list(lst)` | ques-3 |
| `pipe(*fns)` | ques-4 |
| `compose(*fns)` | ques-4 |
| `memoize(fn, ttl)` | ques-5 |
| `curry(fn)` | ques-6 |
| `partial_(fn, *args)` | ques-6 |

</td>
</tr>
</table>

</details>

</td>
</tr>
<tr>
<td>

<details>
<summary><strong>📦 1.2 &nbsp;—&nbsp; Data Normalizer &nbsp;·&nbsp; <code>pro-2-data-normalizer</code></strong> &nbsp;&nbsp;┆&nbsp;&nbsp; ques 7–10 &nbsp;&nbsp;┆&nbsp;&nbsp; 🔽 click to open</summary>

<br/>

**What you will gain:** You learn to accept raw, inconsistent inventory data from 3 different source formats and convert all of it into one clean unified shape. After this module you will understand the Adapter design pattern, recursive tree structures, deep object diffing, and concurrency-limited batch fetching — skills used in every backend data pipeline that ingests from multiple vendors.

<br/>

<table>
<tr>
<th>📝 Questions &nbsp;— solve all 4 first</th>
<th>🔨 Functions to Build &nbsp;·&nbsp; <a href="./projects/pro-2-data-normalizer/about.txt">open project guide →</a></th>
</tr>
<tr>
<td valign="top">

| # | File | What to Learn |
|:---:|:---|:---|
| 7 | [ques-7-normalize-adapter](./question-practice/ques-7-normalize-adapter.py) | Adapter pattern, multi-source mapping |
| 8 | [ques-8-permission-tree](./question-practice/ques-8-permission-tree.py) | Recursive permission-tree resolution |
| 9 | [ques-9-deep-diff](./question-practice/ques-9-deep-diff.py) | Nested dict/list change detection |
| 10 | [ques-10-concurrent-batch-fetch](./question-practice/ques-10-concurrent-batch-fetch.py) | Concurrency-limited batch fetching |

</td>
<td valign="top">

| Function to Build | Needs |
|:---|:---:|
| `csv_row_adapter(raw)` | ques-7 |
| `json_api_adapter(raw)` | ques-7 |
| `legacy_xml_adapter(raw)` | ques-7 |
| `normalize_batch(rows, source)` | ques-7, ques-10 |
| `resolve_permissions(tree, role)` | ques-8 |
| `deep_diff(a, b)` | ques-9 |
| `fetch_batch_limited(fetch_fns, limit)` | ques-10 |

</td>
</tr>
</table>

</details>

</td>
</tr>
<tr>
<td>

<details>
<summary><strong>📦 1.3 &nbsp;—&nbsp; RBAC Engine &nbsp;·&nbsp; <code>pro-3-rbac-engine</code></strong> &nbsp;&nbsp;┆&nbsp;&nbsp; ques 11–13 &nbsp;&nbsp;┆&nbsp;&nbsp; 🔽 click to open</summary>

<br/>

**What you will gain:** You build a security layer that controls exactly what inventory data each user is allowed to see. After this module you will understand how an LRU Cache works (used in every OS, database and CDN), how a Trie powers SKU/autocomplete search (used in warehouse and POS systems), and how field-level data masking works under GDPR and similar regulations — a required feature in every regulated platform.

<br/>

<table>
<tr>
<th>📝 Questions &nbsp;— solve all 3 first</th>
<th>🔨 Functions to Build &nbsp;·&nbsp; <a href="./projects/pro-3-rbac-engine/about.txt">open project guide →</a></th>
</tr>
<tr>
<td valign="top">

| # | File | What to Learn |
|:---:|:---|:---|
| 11 | [ques-11-lru-cache](./question-practice/ques-11-lru-cache.py) | OrderedDict-based LRU eviction |
| 12 | [ques-12-trie](./question-practice/ques-12-trie.py) | Prefix tree / SKU autocomplete |
| 13 | [ques-13-field-masking](./question-practice/ques-13-field-masking.py) | Role-based field masking |

</td>
<td valign="top">

| Function to Build | Needs |
|:---|:---:|
| `resolve_permissions(tree, role)` | ques-8 (from 1.2) |
| `LRUCache` class | ques-11 |
| `Trie` class | ques-12 |
| `mask_email(email)` | ques-13 |
| `mask_phone(phone)` | ques-13 |
| `apply_rbac(record, role)` | ques-8, ques-13 |

</td>
</tr>
</table>

</details>

</td>
</tr>
<tr>
<td>

<details>
<summary><strong>📦 1.4 &nbsp;—&nbsp; Analytics Engine &nbsp;·&nbsp; <code>pro-4-analytics-engine</code></strong> &nbsp;&nbsp;┆&nbsp;&nbsp; ques 14–18 &nbsp;&nbsp;┆&nbsp;&nbsp; 🔽 click to open</summary>

<br/>

**What you will gain:** You turn raw inventory/order records into real business intelligence — pivot tables, running totals, moving averages, and sorted reports. You also build an Observer/pub-sub event system (the pattern behind most Python event frameworks) and a token-bucket Rate Limiter (used in every API gateway like AWS, Cloudflare and Nginx). After this module you will be able to power any analytics dashboard with live, reactive data.

<br/>

<table>
<tr>
<th>📝 Questions &nbsp;— solve all 5 first</th>
<th>🔨 Functions to Build &nbsp;·&nbsp; <a href="./projects/pro-4-analytics-engine/about.txt">open project guide →</a></th>
</tr>
<tr>
<td valign="top">

| # | File | What to Learn |
|:---:|:---|:---|
| 14 | [ques-14-pubsub-events](./question-practice/ques-14-pubsub-events.py) | Observer / pub-sub event system |
| 15 | [ques-15-rate-limiter](./question-practice/ques-15-rate-limiter.py) | Token bucket algorithm |
| 16 | [ques-16-pivot-table](./question-practice/ques-16-pivot-table.py) | 2D aggregation pivot table |
| 17 | [ques-17-running-total](./question-practice/ques-17-running-total.py) | Running totals & moving averages |
| 18 | [ques-18-multi-key-sort](./question-practice/ques-18-multi-key-sort.py) | Priority multi-key sort |

</td>
<td valign="top">

| Function to Build | Needs |
|:---|:---:|
| `EventBus` class | ques-14 |
| `RateLimiter` class | ques-15 |
| `pivot_table(records, row, col, val)` | ques-16 |
| `running_total(records, key)` | ques-17 |
| `moving_average(records, key, n)` | ques-17 |
| `multi_key_sort(records, config)` | ques-18 |

</td>
</tr>
</table>

</details>

</td>
</tr>
<tr>
<td>

<details>
<summary><strong>⭐ 1.Final &nbsp;—&nbsp; PyMart Inventory & Analytics Engine &nbsp;·&nbsp; <code>pro-final-pymart</code></strong> &nbsp;&nbsp;┆&nbsp;&nbsp; ques 19–20 + all above &nbsp;&nbsp;┆&nbsp;&nbsp; 🔽 click to open</summary>

<br/>

**What you will gain:** You wire all 4 modules into one running application. Run `python main.py` and watch raw inventory data flow through normalization → RBAC masking → analytics, producing a live report streamed lazily through a generator pipeline and serialized safely to JSON. After this you will have a complete, demonstrable data pipeline architecture — a real portfolio piece that shows you can design and build production-grade Python systems end-to-end.

<br/>

<table>
<tr>
<th>📝 Questions &nbsp;— final 2 concepts + all previous</th>
<th>🔨 Pipeline Steps to Build &nbsp;·&nbsp; <a href="./projects/pro-final-pymart/about.txt">open project guide →</a></th>
</tr>
<tr>
<td valign="top">

| # | File | What to Learn |
|:---:|:---|:---|
| 19 | [ques-19-lazy-stream](./question-practice/ques-19-lazy-stream.py) | Generator-based lazy streaming pipeline |
| 20 | [ques-20-safe-json](./question-practice/ques-20-safe-json.py) | Safe JSON serialization (circular refs) |

**Also requires:** all ques 1–18 (modules 1.1–1.4 complete)

</td>
<td valign="top">

| Pipeline Step | Needs |
|:---|:---:|
| `step1_normalize(batch, source)` | 1.2 complete |
| `step2_apply_rbac(records, role)` | 1.3 complete |
| `step3_generate_report(records)` | 1.4 complete |
| `step4_audit_trail(before, after)` | ques-9, ques-20 |
| `stream_records(batches)` | ques-19 |
| `build_pipeline(role)` | 1.1 `pipe()` + all above |

**Run:** `python projects/pro-final-pymart/main.py`

</td>
</tr>
</table>

</details>

</td>
</tr>
</table>

---

## 📋 Quick Reference

### [🚀 Project 1 — PyMart Inventory & Analytics Engine](./projects/pro-final-pymart/about.txt) &nbsp;·&nbsp; `pro-final-pymart`
