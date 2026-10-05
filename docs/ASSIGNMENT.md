# Take-Home Exercise: Same Company, Different Names

**Time-box:** 3–4 hours · **Return within:** 5 days · **Language:** your choice

---

## 1. The problem

A customer database has the same business typed in many times, by different people, in
different systems. Nobody enforced a format. So the same company shows up under a dozen
spellings, and two completely unrelated companies can look almost identical.

You'll recognise this problem if you've ever looked up a customer and found four records
that might all be them.

| Name A | Name B | Answer |
|---|---|---|
| `IBM` | `I.B.M. Inc` | same |
| `walmart` | `Wal-Mart Stores, Inc.` | same |
| `Delta Air Lines` | `Delta Dental` | different |
| `American Airlines` | `American Express` | different |
| `RTX` | `Raytheon` | same |
| `PG&E` | `Pacific Gas and Electric` | same |

You get `pairs.csv`: 200 rows, two names each. Decide.

---

## 2. There are two different problems in this file

Look at the last two rows of that table again. They are not just harder versions of the
Walmart row — they are a different problem entirely.

**Most pairs are a spelling problem.** `walmart` and `Wal-Mart Stores, Inc.` are the same
letters wearing different clothes. Tidy up the text on both sides and compare — capitals,
punctuation, spacing, endings like `Inc` and `Ltd`. This will get you a long way, and it's
the right place to start.

**Some pairs are a knowledge problem.** `RTX` and `Raytheon` share almost no letters.
Neither do `PG&E` and `Pacific Gas and Electric`. No amount of tidying will ever connect
them, because the answer isn't in the text — you have to *know* that one is the other.

> ### The part we're most interested in
>
> Roughly **30 of the 200 pairs** are the knowledge kind. Comparing text will never solve
> them, however good your comparison gets. Finding out which ones they are, and deciding
> what to do about them, is the part of this exercise we care about most.
>
> There is more than one sensible answer, and some of them involve writing very little
> code. We're not looking for a specific one — we want to see you notice the difference
> between the two problems and make a deliberate choice.

A warning worth taking seriously: if you try to catch the knowledge pairs by loosening your
text comparison until they match, you will start merging `Delta Air Lines` with
`Delta Dental`. Tightening it up again will lose the matches you just gained. You cannot fix
both ends by turning one dial — that's the whole point.

---

## 3. What to build

A program that reads `pairs.csv` and writes `answers.csv` with your decision for every pair.

> **Read this before you start**
>
> You do **not** need machine learning, AI, or anything clever. Simple rules that you
> understand and can explain are a completely good answer — and often a better one. We care
> much more about how you thought about it than which technique you used.

A sensible order of work: get the spelling problem handled first, see how far it takes you,
then *look at the list of pairs it got wrong*. That list is where the second problem is
hiding, and reading it is more useful than any further tuning.

---

## 4. What to send back

| File | What it is |
|---|---|
| your code | Tell us how to run it. |
| `answers.csv` | `pair_id`, `same_company` (1 or 0), `not_sure` (1 or 0) |
| `NOTES.md` | One page, plain English. We read this first. |

Use `answers_template.csv` as your starting point — it already has all 200 `pair_id` values
in the right order.

The `not_sure` column is there on purpose. Marking a pair as one you'd want a human to check
is a real answer, not a cop-out.

---

## 5. Five questions to answer in NOTES.md

1. **What did you do about the knowledge pairs** — the ones text comparison can't solve?
   How did you find them, what did you decide, and what would you do differently with more time?

2. **How many did you get right?** We didn't give you the answers — so to know how you did,
   you'll have to work some out yourself. Tell us how you did that, and how many you checked.

3. **Which mistake is worse:** saying two different companies are the same, or missing that
   two names are the same company? Pick one, say why, and tell us if it changed what you built.

4. **Show us one your program got wrong,** and explain why it got confused.

5. **What did you have to learn?** Something you didn't know when you started — where you
   learned it, and what confused you at first.

---

## 6. Rules

- **Stop at four hours.** If you run out of time, send what you have and say what you
  didn't get to.
- **Use any language, any library, any AI assistant.** Just tell us what you used and
  where it helped.
- **Working and simple beats clever and broken.** We'd rather see 70% right with clear
  reasoning than 95% you can't explain.
- **Don't hand-write 200 answers.** The program has to do the deciding.

We're not looking for a perfect score. We're looking for someone who can take a vague
problem, make sensible decisions about it, and tell us honestly how well it worked.

---

**Questions about the exercise?** Ask — knowing when to ask is part of the job, and it
won't count against you.
