# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
This is a retrieval-augmented question system built over the campus_life corpus. You
can ask question about courses, housing, dining, etc., and the system will retrieves
the most relevant posts, and giving the answer. If nothing in the corpus related to
the question, it says so instead of guessing.


## Chunking Strategy

**Chunk size: 150 - 600 characters**
**Overlap:None**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.
 
     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->
     The documents in corpora/campus_life are short. I checked the range and found the
     shortest documents has 178 characters, while the longest has 549. Actually, at first,
     I give my min-bound for this is 40 characters before checking, because I want to make sure
     that short documents still count as one chunk, except those are too short, which usually can't
     give enough information. Moreover, if a document exceeds 600, it gets splitted at paragraph break,
     and merge any piece under 150 characters back into its neighbor.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->
     

**Chunk 1** — source: `` — produced by: ``

```
======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `` — produced by: ``

```
======================================================================
Chunk 2  |  source: course_biol_160.txt#0  |  produced by: chunker.py::split_documents
======================================================================
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `` — produced by: ``

```
======================================================================
Chunk 3  |  source: course_hist_118_workload.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `` — produced by: ``

```
======================================================================
Chunk 4  |  source: dining_pellew_dining_hall_followup.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `` — produced by: ``

```
======================================================================
Chunk 5  |  source: housing_innisfree_hall.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:
"What is the deadline for declaring a major?"**

**Answer:**

```
You declare a major at the end of your second semester, or later if you need to, as there is no penalty for declaring late (`admin_declaring_a_major.txt`).
```

**My relevance cutoff:0.6**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->


| Question | In corpus? | Best distance |
|---|---|---|
| "What is the deadline for declaring a major?" | Yes | 0.302 |
| "When will library close in reading week?" | Yes | 0.440 |
| "Is morrow house noisy?" | Yes | 0.366 |
| "Does CS 210 have a curve for the exams?" | Yes | 0.336 |
| "What is the maximum hours per week for work-study?" | Yes | 0.462 |
| "What is the capital of Mongolia?" | No | 0.825 |
| "How do I change the oil in a diesel engine?" | No | 0.934 |
| "Who won the 1994 World Cup?" | No | 0.886 |
| "What is the recommended dosage of ibuprofen for a headache?" | No | 0.844 |
| "How do I write a for loop in Rust?" | No | 0.896 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
"I asked Claude to check my 5th criteria. It gave me some suggestion about it,
but I don't use that suggestion."

**2.**
"When testing the conversational memory, the history block wasn't showing at all.
So I asked Claude, and turn out, I was running two seperate "python app.py ask" command.
It supposed to run 2 questions in the same session."

**3.**
"I asked Claude to help diagnose one miss by pipleline stage, and the cause is the source,
which exactly as I thinking.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->
## Stretch: Metadata Filtering
I added a "category" field to each chunk's metadata, and added a "--category" flag to
"python app.py retrieve" that filters result by it.

**Without filter** — "python app.py retrieve "what does it cost"":
| distance | source | preview |
|---|---|---|
|0.5536     |housing_calder_annexe.txt        |Calder Annexe — what it's actually like  Second-year...|
|0.6270     |admin_printing_quota.txt         |On the printing quota  Every student gets $30 of pri...|
|0.6681     |housing_fenwick_court.txt        |Fenwick Court — what it's actually like  Just finish...|
|0.6713     |money_textbooks.txt              |Textbooks without paying full price  The library hol...|
|0.6822     |housing_innisfree_hall.txt       |Innisfree Hall — what it's actually like  Transferre...|

**With filter** — "python app.py retrieve "what does it cost" --category housing":
| distance | source | preview |
|---|---|---|
|0.5536     |housing_calder_annexe.txt        |Calder Annexe — what it's actually like  Second-year...|
|0.6681     |housing_fenwick_court.txt        |Fenwick Court — what it's actually like  Just finish...|
|0.6822     |housing_innisfree_hall.txt       |Innisfree Hall — what it's actually like  Transferre...|
|0.7100     |housing_aldridge_hall.txt        |Aldridge Hall — what it's actually like  I lived her...|
|0.7165     |housing_morrow_house.txt         |Morrow House — what it's actually like  Just finishe...|

**What change:**
Filtering removed the two non-housing results (printing quota, textbooks)
and pulled in two additional housing results that weren't in the
unfiltered


## Stretch: Conversational memory
I added "history" parameter, so the previous question and answer get include in the next prompt

**Question 1:** "what's Aldridge Hall like?"
> Aldridge Hall is a building constructed in 1968 and renovated in 2019...
> Laundry costs $1.75 to wash and $1.50 to dry using a card only...
> Source: housing_aldridge_hall.txt

**Question 2:** "what's about the laundry there?"
> In Aldridge Hall, laundry costs $1.75 to wash and $1.50 to dry using a card only. There are eight washers and six dryers...
> Source: housing_aldridge_hall_laundry.txt

**What change:**
In question 2, if there is no history, it will pull back laundry chunks for different buildings. However, with history included,
retrieval still returns the same 5 builiding's chunks, but the model narrows it answer to the building from question 1,
showing the second answer depends on the first one rather than sharing the topic.


---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk size ( 150 - 600 characters ) | ALL CHUNKS | pass | pass | pass | MET |
| 5. Answer includes fact + 1 detail | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
**Criterion 1 — Retrieved chunk contains the answer**
Produced by: `store.py::search`, `chunker.py::split_documents`
> Question: What is the deadline for declaring a major?

> Best distance: 0.3025 (passed the gate)
> Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_graduation_requirements.txt, admin_pass_fail_option.txt, course_cs_340.txt
>
> You declare at the end of your second semester, or later if you need to, because there is no penalty for declaring late.
>
> Source: admin_declaring_a_major.txt

**Criterion 2 — Every answer names a source**
Produced by: `generate.py::answer_from_chunks`
>Question: Does CS 210 have a curve for the exams?

> Yes, the midterms for CS 210 are curved, but the final is not curved.
>
> Sources: `course_cs_210.txt` and `course_cs_210_exams.txt`

**Criterion 3 — Gate stops out-of-corpus questions**
Produced by: `gate.py::check`

> What is the capital of Mongolia?
> Best distance: 0.825 — refused
>
> (5 of 5 out-of-scope questions refused)

**Criterion 4 — Chunk size (150–600 characters)**
Produced by: `chunker.py::split_documents`

> 88 chunks, 317 characters on average (shortest 178, longest 549)
> 0 documents exceeded 600 characters — every document remained one
> chunk, within bounds.

**Criterion 5 — Answer includes the fact plus one related detail**
Produced by: `generate.py::answer_from_chunks`

> The library is open until 10pm during reading week (study_library_hours.txt).

This shows why criterion 5 is MISSED: the answer did answer the question
but includes no second related detail, unlike questions like "Is Morrow House noisy?"
which included both a fact and a follow-up detail from the same source.


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer (4 of 5) | MET | All 5 quesions had the answer in the retrieved chunk, in all 3 runs. |
| 2 | Every answer names a source (5 of 5) | MET | Every answers (15 in total) all named at least one source. |
| 3 | Gate stops out-of-corpus questions (4 of 5) | MET | All 5 out of scope questions were refused. |
| 4 | Chunk size (150 - 600 characters) | MET | 0 of 88 documents exceed 600 characters or lower than 150. |
| 5 | Answer includes fact + 1 detail (4 of 5) | MISSED | Only 3 of 5 questions included a second relative detail. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->
**Criterion 5: Answer includes facts + one related detail**

Stage: Loading

Retrieval found the right chunk in all 5 questions, and show what actually in there, rather than
inventing a new fact. The sources for question 2 and 5 only have one fact. The criterion assumed
richer source material than the document actually have.

## The Improvement

**What I changed:**
Add hybrid search - BM25 keyword matching combined with existing search

**Why I picked it:**
I want to test whether this hybrid search can improve retrieval quality.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk size (150-600 characters) | all chunks | PASS | PASS | PASS | MET |
| 5. Answer includes fact + 1 detail (4 of 5)| 3/5 | 3/5 | 3/5 | 3/5 | MISSED |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->
No. The retrieval source for all 5 questions were still the same. The searching machenic is
already optimal, so adding BM25 can not improve anything. This confirm that criterion 5's miss
comes from two source documents, not retrieval mechanism issue.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->
**Criterion 5**
What I'd do about it: rewrite the two documents to include a second fact.
Why I stopped where I did: I cannot do anything else because it the document's issues.

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
I'd rewrite the criterion 5 to only apply where the source document actually contains more than one fact.
Also, maybe the criterion 4 cause the none of the documents exceed the 600 characters.


## Capstone

**The System**

The Unofficial Guide, the retrieval-augmented question system over the
`campus_life` corpus from units 1 and 2. It retrieves the closest posts for a
question, refuses through a relevance gate when nothing is close enough, and
otherwise answers from the retrieved posts with the source file named.


**Shape and Path:**

Shape A, deploy and instrument, on Path B, local with logs. Before this unit, serve.py could answer questions over HTTP but left no record of what it did, so nothing it did could be checked afterwards. The extension is the operational layer around the pipeline that already exists. Every run, whether answered, refused by the gate, crashed, or rejected for missing input, writes one JSON record to logs/runs.jsonl. The record has named fields for the question, the answer, total time split into retrieval and generation, the best distance, the sources, and the token counts the model service reported. python serve.py starts the whole system from a clean checkout, building the index first if there isn’t one. measure_cost.py turns ten uncached runs from that log into a per-run cost.

**Out of scope:** I not choose path A

**How to Run It**

See `RUNNING.md`, section "Capstone run path". The start command is
`python serve.py`.

**Instrumentation**

Every request to `/ask`, and every `python app.py ask`, appends one JSON object
to `logs/runs.jsonl`, written by `run_log.py::write`. Answered, refused and
errored runs are logged by `app.py::ask_pipeline`; requests with no question are
logged by `serve.py::ask` before they reach the pipeline. Fields: `ts`,
`run_id`, `entrypoint`, `status` (ok / refused / rejected / error), `question`,
`answer`, `duration_ms`, `retrieve_ms`, `generate_ms`, `best_distance`,
`threshold`, `sources`, `model_calls`, `cache_hit`, `prompt_tokens`,
`output_tokens`, `error`, `http_status`.


10 LOG ENTRIES
```bash
{"ts": "2026-11-16T00:05:17.128+00:00", "run_id": "50f9f173", "entrypoint": "http", "status": "ok", "question": "Is morrow house noisy?", "answer": "Yes, Morrow House is loud until about 1am on weekends and has no enforced quiet hours (housing_morrow_house.txt and housing_morrow_house_noise.txt).", "duration_ms": 815.9, "retrieve_ms": 52.1, "generate_ms": 763.8, "best_distance": 0.3658, "threshold": 0.6, "sources": ["housing_fenwick_court_noise.txt", "housing_innisfree_hall_noise.txt", "housing_morrow_house.txt", "housing_morrow_house_noise.txt", "housing_old_brewhouse_noise.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 596, "output_tokens": 38, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:17.972+00:00", "run_id": "c9d21f34", "entrypoint": "http", "status": "ok", "question": "Does CS 210 have a curve for the exams?", "answer": "Yes, the midterms for CS 210 are curved, but the final is not curved (sources: course_cs_210_exams.txt and course_cs_210.txt).", "duration_ms": 784.7, "retrieve_ms": 56.2, "generate_ms": 728.5, "best_distance": 0.3359, "threshold": 0.6, "sources": ["course_cs_210.txt", "course_cs_210_exams.txt", "course_cs_340_exams.txt", "course_engl_205_exams.txt", "course_stat_150_exams.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 519, "output_tokens": 45, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:21.291+00:00", "run_id": "82ee49eb", "entrypoint": "http", "status": "ok", "question": "What is the maximum hours per week for work-study?", "answer": "The maximum is 20 hours a week during the term (from money_jobs.txt).", "duration_ms": 771.2, "retrieve_ms": 51.8, "generate_ms": 719.3, "best_distance": 0.4623, "threshold": 0.6, "sources": ["course_engl_205_workload.txt", "course_phys_130_workload.txt", "course_stat_150_workload.txt", "money_jobs.txt", "study_group_rooms.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 555, "output_tokens": 20, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:27.284+00:00", "run_id": "98b991cf", "entrypoint": "http", "status": "refused", "question": "Who won the 1994 World Cup?", "answer": "I don't have enough information about that.", "duration_ms": 58.4, "retrieve_ms": 58.4, "generate_ms": 0.0, "best_distance": 0.8859, "threshold": 0.6, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:28.858+00:00", "run_id": "c3e532a4", "entrypoint": "http", "status": "refused", "question": "How do I write a for loop in Rust?", "answer": "I don't have enough information about that.", "duration_ms": 54.0, "retrieve_ms": 54.0, "generate_ms": 0.0, "best_distance": 0.896, "threshold": 0.6, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:35.637+00:00", "run_id": "b958024e", "entrypoint": "http", "status": "ok", "question": "How much does laundry cost in Innisfree Hall?", "answer": "Laundry in Innisfree Hall costs $1.75 for a wash and $1.75 for a dry. \n\nThis information comes from *housing_innisfree_hall.txt* and *housing_innisfree_hall_laundry.txt*.", "duration_ms": 566.7, "retrieve_ms": 55.9, "generate_ms": 510.7, "best_distance": 0.2052, "threshold": 0.6, "sources": ["housing_aldridge_hall.txt", "housing_aldridge_hall_laundry.txt", "housing_calder_annexe.txt", "housing_innisfree_hall.txt", "housing_innisfree_hall_laundry.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 709, "output_tokens": 57, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:36.231+00:00", "run_id": "7acfaaf0", "entrypoint": "http", "status": "ok", "question": "How long is the wait at Pellew Dining Hall at peak?", "answer": "The wait at Pellew Dining Hall at peak is 12 to 18 minutes (dining_pellew_dining_hall.txt and dining_pellew_dining_hall_followup.txt).", "duration_ms": 724.0, "retrieve_ms": 50.1, "generate_ms": 673.8, "best_distance": 0.1568, "threshold": 0.6, "sources": ["dining_halden_hall.txt", "dining_halden_hall_followup.txt", "dining_pellew_dining_hall.txt", "dining_pellew_dining_hall_followup.txt", "dining_the_ridgeway_cafe_followup.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 704, "output_tokens": 46, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:38.091+00:00", "run_id": "c3f08fde", "entrypoint": "http", "status": "ok", "question": "Is BIOL 160 curved?", "answer": "No, BIOL 160 is not curved. \n\nSource: course_biol_160_exams.txt (also mentioned in course_biol_160.txt)", "duration_ms": 638.5, "retrieve_ms": 53.1, "generate_ms": 585.4, "best_distance": 0.44, "threshold": 0.6, "sources": ["course_biol_160.txt", "course_biol_160_exams.txt", "course_engl_205_exams.txt", "course_phys_130.txt", "course_phys_130_exams.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 520, "output_tokens": 43, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:44.137+00:00", "run_id": "cc5f2d5b", "entrypoint": "http", "status": "rejected", "question": "''", "answer": null, "duration_ms": 0.1, "retrieve_ms": null, "generate_ms": 0.0, "best_distance": null, "threshold": null, "sources": null, "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "error": "rejected input: no question", "http_status": 400}
{"ts": "2026-11-16T00:06:24.359+00:00", "run_id": "1a764d8b", "entrypoint": "cli", "status": "error", "question": "test", "answer": null, "duration_ms": 438.6, "retrieve_ms": null, "generate_ms": 0.0, "best_distance": null, "threshold": null, "sources": null, "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "error": "RuntimeError: No index called 'campus_life__default'. Run `python app.py index` first.", "http_status": null}
```

1 FAIL RUN
```bash
{"ts": "2026-11-16T00:06:24.359+00:00", "run_id": "1a764d8b", "entrypoint": "cli", "status": "error", "question": "test", "answer": null, "duration_ms": 438.6, "retrieve_ms": null, "generate_ms": 0.0, "best_distance": null, "threshold": null, "sources": null, "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "error": "RuntimeError: No index called 'campus_life__default'. Run `python app.py index` first.", "http_status": null}
```

**What It Costs**

Method: `measure_cost.py::main` sends 10 questions from `questions.py` through
`app.py::ask_pipeline` with the cache off, then averages the `prompt_tokens`,
`output_tokens` and `duration_ms` fields of those 10 records. Token counts come
from the `usage_metadata` on each Gemini response, not from the pricing page.
The report is committed in `results/`.

Averages over the answered runs:

| Measure | Mean per run |
|---|---|
| Input tokens | 547.4 |
| Output tokens | 32.8 |
| Total tokens | 580.2 |
| Total duration | 934.1 ms |
| Retrieval (embed + search) | 100.1 ms |
| Generation (model call) | 735.0 ms |

**Criteria**

See `criteria.md`, section "Capstone".

**Run Log — Before**


| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Run appear on the log| 9 of 10 | 10 of 10 | 10 of 10 | 10 of 10 | MET |
| 2. Number of token| max 650 | 612 | 630  | 587 | MET |
| 3. Time output| under 2s | 2.2 | 1.8 | 2 | MISSED |
| 4. Missing index is logged as status error| 3 of 3 | 3 of 3 | 3 of 3 | 3 of 3 | MET |
| 5. | | | | | |

```bash
{"ts": "2026-11-15T23:35:33.939+00:00", "run_id": "d865c691", "entrypoint": "cli", "status": "ok", "question": "What is the deadline for declaring a major?", "answer": "You declare a major at the end of your second semester, or later if you need to, as there is no penalty for declaring late (admin_declaring_a_major.txt).", "duration_ms": 2739.1, "retrieve_ms": 525.5, "generate_ms": 2213.5, "best_distance": 0.3025, "threshold": 0.6, "sources": ["admin_add_drop_deadline.txt", "admin_declaring_a_major.txt", "admin_graduation_requirements.txt", "admin_pass_fail_option.txt", "course_cs_340.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 542, "output_tokens": 39, "error": null, "http_status": null}
{"ts": "2026-11-15T23:35:41.418+00:00", "run_id": "81a315bc", "entrypoint": "cli", "status": "refused", "question": "What is the capital of Mongolia?", "answer": "I don't have enough information about that.", "duration_ms": 487.1, "retrieve_ms": 486.9, "generate_ms": 0.0, "best_distance": 0.8246, "threshold": 0.6, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "error": null, "http_status": null}
{"ts": "2026-11-15T23:38:12.534+00:00", "run_id": "316698dc", "entrypoint": "http", "status": "ok", "question": "Is morrow house noisy?", "answer": "Yes, Morrow House is loud until about 1am on weekends and has no enforced quiet hours (housing_morrow_house.txt and housing_morrow_house_noise.txt).", "duration_ms": 1458.2, "retrieve_ms": 209.9, "generate_ms": 1247.1, "best_distance": 0.3658, "threshold": 0.6, "sources": ["housing_fenwick_court_noise.txt", "housing_innisfree_hall_noise.txt", "housing_morrow_house.txt", "housing_morrow_house_noise.txt", "housing_old_brewhouse_noise.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 596, "output_tokens": 38, "error": null, "http_status": 200}
{"ts": "2026-11-15T23:38:14.028+00:00", "run_id": "fa97e5ce", "entrypoint": "http", "status": "rejected", "question": "{\"q\": \"wrong key\"}", "answer": null, "duration_ms": 0.1, "retrieve_ms": null, "generate_ms": 0.0, "best_distance": null, "threshold": null, "sources": null, "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "error": "rejected input: no question", "http_status": 400}
{"ts": "2026-11-16T00:05:14.914+00:00", "run_id": "4d240d44", "entrypoint": "http", "status": "ok", "question": "What is the deadline for declaring a major?", "answer": "You declare at the end of your second semester, or later if you need to. There is no penalty for declaring late. \n\nSource: admin_declaring_a_major.txt", "duration_ms": 1484.2, "retrieve_ms": 213.0, "generate_ms": 1270.1, "best_distance": 0.3025, "threshold": 0.6, "sources": ["admin_add_drop_deadline.txt", "admin_declaring_a_major.txt", "admin_graduation_requirements.txt", "admin_pass_fail_option.txt", "course_cs_340.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 542, "output_tokens": 39, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:16.426+00:00", "run_id": "9a16d311", "entrypoint": "http", "status": "ok", "question": "When will library close in reading week?", "answer": "The library is open until 10pm during reading week. \n\nSource: study_library_hours.txt", "duration_ms": 669.7, "retrieve_ms": 55.5, "generate_ms": 614.2, "best_distance": 0.44, "threshold": 0.6, "sources": ["admin_library_holds.txt", "housing_calder_annexe_noise.txt", "housing_morrow_house_noise.txt", "money_textbooks.txt", "study_library_hours.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 525, "output_tokens": 24, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:17.128+00:00", "run_id": "50f9f173", "entrypoint": "http", "status": "ok", "question": "Is morrow house noisy?", "answer": "Yes, Morrow House is loud until about 1am on weekends and has no enforced quiet hours (housing_morrow_house.txt and housing_morrow_house_noise.txt).", "duration_ms": 815.9, "retrieve_ms": 52.1, "generate_ms": 763.8, "best_distance": 0.3658, "threshold": 0.6, "sources": ["housing_fenwick_court_noise.txt", "housing_innisfree_hall_noise.txt", "housing_morrow_house.txt", "housing_morrow_house_noise.txt", "housing_old_brewhouse_noise.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 596, "output_tokens": 38, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:17.972+00:00", "run_id": "c9d21f34", "entrypoint": "http", "status": "ok", "question": "Does CS 210 have a curve for the exams?", "answer": "Yes, the midterms for CS 210 are curved, but the final is not curved (sources: course_cs_210_exams.txt and course_cs_210.txt).", "duration_ms": 784.7, "retrieve_ms": 56.2, "generate_ms": 728.5, "best_distance": 0.3359, "threshold": 0.6, "sources": ["course_cs_210.txt", "course_cs_210_exams.txt", "course_cs_340_exams.txt", "course_engl_205_exams.txt", "course_stat_150_exams.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 519, "output_tokens": 45, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:21.291+00:00", "run_id": "82ee49eb", "entrypoint": "http", "status": "ok", "question": "What is the maximum hours per week for work-study?", "answer": "The maximum is 20 hours a week during the term (from money_jobs.txt).", "duration_ms": 771.2, "retrieve_ms": 51.8, "generate_ms": 719.3, "best_distance": 0.4623, "threshold": 0.6, "sources": ["course_engl_205_workload.txt", "course_phys_130_workload.txt", "course_stat_150_workload.txt", "money_jobs.txt", "study_group_rooms.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 555, "output_tokens": 20, "error": null, "http_status": 200}
{"ts": "2026-11-16T00:05:27.284+00:00", "run_id": "98b991cf", "entrypoint": "http", "status": "refused", "question": "Who won the 1994 World Cup?", "answer": "I don't have enough information about that.", "duration_ms": 58.4, "retrieve_ms": 58.4, "generate_ms": 0.0, "best_distance": 0.8859, "threshold": 0.6, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "error": null, "http_status": 200}
```


**Verdicts and Diagnoses**

**The Improvement**


**Run Log — After**

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. | | | | | |
| 2. | | | | | |
| 3. | | | | | |
| 4. | | | | | |
| 5. | | | | | |


**What's Still Broken**



**What I'd Do Next**



**How I Used AI**

