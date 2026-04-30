# Week 9 Homework Brief

## Weekly Coding #7: The Case of the Missing Festival Lanterns

**Due:** Sunday 2026-05-03 at 23:59 KST  
**Standards:** S6 Hash Tables with `dict` / `set`, S1 Python + Testing Fundamentals, S3 Big-O Reasoning  
**Language:** Python 3.11+  
**Dependencies:** Standard library only, plus `pytest` for tests  
**Graded files:** `.py` files, `pytest` tests, and README evidence

---

## Story

Every spring, the town of Bellweather holds a lantern festival.

Each neighborhood designs paper lanterns and hangs them along the river path. At night, the lanterns are lit one by one, and visitors walk through the glowing trail.

This year, something strange happened.

The festival volunteers prepared a checklist of lanterns that should appear on the path. But after sunset, some lanterns were missing, some lanterns appeared twice, and a few lanterns were hanging in the wrong neighborhood section.

Your job is to write a small Python function that analyzes the lantern records and returns a clear report.

No drama. Just data. Then maybe drama.

---

## Files You Must Submit

```text
src/challenges.py
tests/test_challenges.py
README.md
```

Do not submit a notebook as your graded work. Notebooks are demo-only.

---

## Your Task

Complete the function in:

```text
src/challenges.py
```

Function:

```python
def analyze_lanterns(
    expected_lanterns: set[str],
    lantern_log: list[tuple[str, str]],
    correct_sections: dict[str, str],
) -> dict[str, object]:
    pass
```

The function must **return** a report dictionary.

Do not solve this by only printing output.

---

## Input Data

### `expected_lanterns`

A set of lantern names that should appear at the festival.

Example:

```python
{
    "river-dragon",
    "blue-crane",
    "moon-rabbit",
    "gold-tiger",
    "white-lotus",
    "red-kite",
}
```

### `lantern_log`

A list of records. Each record is a tuple:

```python
(lantern_name, actual_section)
```

Example:

```python
[
    ("river-dragon", "North Gate"),
    ("blue-crane", "River Walk"),
    ("moon-rabbit", "River Walk"),
    ("river-dragon", "North Gate"),
    ("gold-tiger", "Market Street"),
    ("silver-fox", "Market Street"),
    ("red-kite", "South Bridge"),
]
```

### `correct_sections`

A dictionary where:

- key = expected lantern name
- value = section where that lantern should appear

Example:

```python
{
    "river-dragon": "North Gate",
    "blue-crane": "River Walk",
    "moon-rabbit": "River Walk",
    "gold-tiger": "Market Street",
    "white-lotus": "Temple Road",
    "red-kite": "Temple Road",
}
```

---

## Required Report Dictionary

Your function must return a dictionary with exactly these six keys:

```python
{
    "seen_lanterns": ...,
    "missing_lanterns": ...,
    "unexpected_lanterns": ...,
    "duplicate_lanterns": ...,
    "count_by_section": ...,
    "wrong_section_lanterns": ...,
}
```

### 1. `seen_lanterns`

A `set[str]` of all lantern names found in the log.

Expected result for the starter data:

```python
{
    "river-dragon",
    "blue-crane",
    "moon-rabbit",
    "gold-tiger",
    "silver-fox",
    "red-kite",
}
```

### 2. `missing_lanterns`

A `set[str]` of expected lanterns that were not found in the log.

Expected result for the starter data:

```python
{"white-lotus"}
```

### 3. `unexpected_lanterns`

A `set[str]` of lanterns found in the log but not listed in `expected_lanterns`.

Expected result for the starter data:

```python
{"silver-fox"}
```

### 4. `duplicate_lanterns`

A `set[str]` of lantern names that appeared more than once in the log.

Expected result for the starter data:

```python
{"river-dragon"}
```

Important: duplicate checking is based on the lantern name, not the section.

### 5. `count_by_section`

A `dict[str, int]` that counts how many lantern records appeared in each section.

Expected result for the starter data:

```python
{
    "North Gate": 2,
    "River Walk": 2,
    "Market Street": 2,
    "South Bridge": 1,
}
```

Important: count every record in the log, including unexpected lanterns.

### 6. `wrong_section_lanterns`

A `dict[str, dict[str, str]]` showing expected lanterns that appeared in the wrong section.

The outer key should be the lantern name.

The inner dictionary should have:

- `"expected"`
- `"actual"`

Expected result for the starter data:

```python
{
    "red-kite": {
        "expected": "Temple Road",
        "actual": "South Bridge",
    }
}
```

Important rules:

- Ignore unexpected lanterns when checking wrong sections.
- For example, `"silver-fox"` is unexpected, so it should not appear in `wrong_section_lanterns`.
- If an expected lantern appears in more than one wrong section, record the first wrong section found in the log.

---

## Suggested Work Order

1. Create `seen_lanterns`.
2. Create `seen_once` and `duplicate_lanterns`.
3. Create `count_by_section`.
4. Create `wrong_section_lanterns`.
5. Loop through `lantern_log`.
6. Inside the loop, collect seen lanterns, detect duplicates, count sections, and check wrong sections.
7. After the loop, use set subtraction for missing and unexpected lanterns.
8. Return the full report dictionary.
9. Run `pytest -q`.
10. Add at least one meaningful test of your own.
11. Fill out the TODO sections in `README.md`.

---

## Testing Requirements

The starter tests check several important cases.

Before submitting, you must:

- pass the starter tests with `pytest -q`
- add at least **one meaningful test of your own**
- keep your new test in `tests/test_challenges.py`

Good extra test ideas:

- all expected lanterns are present and in the correct section
- the log is empty but `expected_lanterns` is not empty
- the same lantern appears three times
- an expected lantern appears once correctly and once in the wrong section

---

## README Requirements

Your `README.md` is where you explain your work.

Before submitting, fill in these sections:

- Summary
- Approach
- How I used dictionaries and sets
- Complexity
- Edge-case checklist
- Tests I added
- Assistance and sources

The starter `README.md` already has the required headings and TODO prompts.

---

## Complexity Expectations

Your solution should avoid unnecessary nested loops.

A strong solution should usually be:

- **Time:** O(n + m), where `n` is the number of log records and `m` is the number of expected lanterns
- **Space:** O(a + s), where `a` is the number of distinct lantern names stored and `s` is the number of sections stored

Your explanation may use different variable names, but it should clearly explain what grows when the input grows.

---

## Standards Evidence

### S6 — Hash Tables with `dict` / `set`

To meet this standard, your code should use dictionaries and sets for the correct jobs:

- sets for seen, missing, unexpected, and duplicate lanterns
- dictionaries for section counts and wrong-section details

### S1 — Python + Testing Fundamentals

To meet this standard, your tests should pass and you should add at least one meaningful test of your own.

### S3 — Big-O Reasoning

To meet this standard, your README should include a short, accurate complexity explanation.

---

## Submission Checklist

Before you submit, check:

- [ ] `src/challenges.py` contains a completed `analyze_lanterns` function
- [ ] `tests/test_challenges.py` includes at least one test you added
- [ ] `pytest -q` passes
- [ ] `README.md` is filled out
- [ ] your latest work is pushed to GitHub

---

## Journal #9 Prompt

Submit this separately if your instructor asks for a journal response.

```text
This week we learned about hash tables, dictionaries, and sets.

Explain one situation where using a dictionary or set makes a program simpler or faster.

Then describe one part of Project 2 where you could possibly use a dictionary or set to improve your code.
```
