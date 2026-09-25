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

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
