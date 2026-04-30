[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QtC5AQlU)
# Week 9 Homework: The Case of the Missing Festival Lanterns

## Student Info

Name: Alisha  
Student number: 2412093  
GitHub username: GurungAlisha

---

## Summary

`analyze_lanterns` solves the problem of auditing festival lantern records to find missing, unexpected, duplicate, and misplaced lanterns. It receives three inputs: a set of lantern names that are expected at the festival, a log of (lantern_name, actual_section) tuples recorded during the event, and a dictionary mapping each expected lantern to its correct section. It processes these inputs and returns a detailed report dictionary with six keys covering every aspect of the audit. The report makes it easy to identify exactly what went wrong during the festival — which lanterns never showed up, which were not supposed to be there, which appeared more than once, and which were in the wrong location.

---

## Approach

- First, I created empty collections: a `seen_lanterns` set, a `seen_once` set to detect duplicates, a `duplicate_lanterns` set, a `count_by_section` dictionary, and a `wrong_section_lanterns` dictionary.
- During the loop over `lantern_log`, I unpacked each tuple into `lantern_name` and `actual_section`, then added the name to `seen_lanterns`. I used `seen_once` to detect duplicates — if a name was already in `seen_once`, it went into `duplicate_lanterns`; otherwise it was added to `seen_once`.
- Still inside the loop, I incremented `count_by_section` for the current section using `dict.get` with a default of 0.
- Also inside the loop, I checked wrong sections only for expected lanterns: if the actual section did not match the correct section from `correct_sections`, and the lantern had not already been recorded in `wrong_section_lanterns`, I stored the first wrong section found.
- After the loop, I used set subtraction to compute `missing_lanterns` (expected minus seen) and `unexpected_lanterns` (seen minus expected).
- Finally, I returned all six values in a single report dictionary.

---

## How I Used Dictionaries and Sets

1. **Sets used:** `seen_lanterns` tracks every lantern encountered. `seen_once` helps detect duplicates. `duplicate_lanterns` stores names that appeared more than once. `missing_lanterns` and `unexpected_lanterns` are computed using set subtraction (`-` operator).
2. **Dictionaries used:** `count_by_section` maps each section name to how many log entries it received. `wrong_section_lanterns` maps a lantern name to a nested dict with `"expected"` and `"actual"` section strings. `correct_sections` (the input) is used for O(1) lookups of the expected section per lantern.
3. **Why not lists:** Set membership checks (`in`) are O(1) whereas the same check on a list is O(n). Dictionary lookups are also O(1). If we used only lists, every lookup would require scanning the entire list, making the solution significantly slower for large logs.

```text
Sets give O(1) membership checks and make set operations like subtraction
simple and readable. Dictionaries give O(1) key lookups for section counts
and correct-section comparisons. Lists would require linear scans for the
same tasks.
```

---

## Complexity

```text
Time complexity: O(n)
Space complexity: O(n)
Explanation:
The solution loops through lantern_log exactly once (n = number of records).
There are no nested loops. Inside the loop every operation — set add, dict
get/set, membership check — is O(1). After the loop, set subtraction runs
in O(|expected_lanterns| + |seen_lanterns|), which is bounded by n.
Extra space used: seen_lanterns, seen_once, duplicate_lanterns,
count_by_section, and wrong_section_lanterns each grow at most to the size
of the log, so total space is O(n).
```

---

## Edge-Case Checklist

- [x] empty `lantern_log` — the loop body never executes; all sets and dicts are empty; every expected lantern is missing.
- [x] empty `expected_lanterns` — missing and unexpected are computed correctly; wrong-section check is skipped for all lanterns since none are expected.
- [x] no missing lanterns — `missing_lanterns` is an empty set when all expected lanterns appear in the log.
- [x] no unexpected lanterns — `unexpected_lanterns` is an empty set when every logged lantern is in `expected_lanterns`.
- [x] duplicate lanterns — detected by comparing against `seen_once` before adding; only stored once in `duplicate_lanterns`.
- [x] wrong-section lanterns — checked inside the loop; only the first wrong section is recorded per lantern.
- [x] unexpected lanterns ignored for wrong-section checking — the guard `if lantern_name in expected_lanterns` prevents unexpected lanterns from ever entering `wrong_section_lanterns`.

Add one more edge case you thought about:

```text
A lantern appears in the correct section on one visit and a wrong section
on a later visit. Because we only record the first wrong section found,
and correct appearances are simply skipped, the report stays accurate
regardless of visit order.
```

---

## Tests I Added

```text
Test name: test_analyze_lanterns_all_correct
What it checks: When every expected lantern appears exactly once in its
correct section and there are no unexpected lanterns, all five "problem"
fields (missing, unexpected, duplicate, wrong_section_lanterns) are empty,
and count_by_section reflects the actual log entries.
Why it matters: Confirms the happy path works — the function should not
flag anything as wrong when the festival runs perfectly.
```

---

## How to Run the Tests

```bash
pytest -q
```

```text
5 passed in 0.09s
```

---

## Assistance and Sources

```text
AI used? Y
What it helped with: code structure, implementation of the loop logic,
set operations, and README writeup.
Other sources used: Python standard library documentation (sets, dicts).
```

---

## Submission Self-Check

- [x] I completed `analyze_lanterns` in `src/challenges.py`.
- [x] I added at least one meaningful test of my own.
- [ ] `pytest -q` passes.
- [x] I completed this README.
- [ ] I pushed my latest work to GitHub.