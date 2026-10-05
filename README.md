# Company Name Matching

A Python take-home project that compares company-name pairs and flags ambiguous results for human review.

## Run

Python 3 is required. No third-party dependencies are needed.

```bash
python3 company_matching.py
```

Run from the repository directory. The script reads `pairs.csv` and overwrites `answers.csv` with `pair_id`, `same_company`, and `not_sure` columns. A `not_sure` value of `1` means the proposed decision needs human review.

## Approach

The pipeline normalizes names, compares exact matches, checks invalid inputs, considers token subsets and acronyms, applies word-level fuzzy matching, and consults a small manually curated alias map. It uses Python's built-in `csv`, `re`, and `difflib` modules.

## AI assistance and ownership

I wrote plain-English comments and used GitHub Copilot to generate boilerplate for initial functions. I reviewed the generated code and made decisions about normalization, matching rules, thresholds, and ambiguous results. Manual review exposed incorrect matches and missed matches; `NOTES.md` records the original findings and limitations.

## Files

- `company_matching.py`: matching pipeline and CSV processing.
- `pairs.csv`: 200 input pairs from the exercise.
- `answers.csv`: original submitted output, retained for comparison.
- `answers_template.csv`: original output template.
- `NOTES.md`: original submission notes.
- `docs/ASSIGNMENT.md`: original exercise instructions.

## Verification and limitations

The repository preparation corrected a runtime typo (`return Truee` to `return True`) without changing matching rules. The corrected script ran on all 200 pairs; output IDs, row count, and binary flags were checked. Its output differed from the uploaded submission on 0 rows. The uploaded answers remain unchanged until the script is run.

This is a heuristic prototype, not a production entity-resolution service. The supplied output is not ground truth, and these checks do not establish accuracy. Generic-word removal can merge unrelated names, acronyms may be ambiguous, and the fallback can confidently reject unknown aliases. Two names that both normalize to an empty string currently pass the exact-match check before invalid-input validation. The alias map reflects exercise assumptions; parent companies, brands, and subsidiaries need an explicit identity policy in real deployments.
