"""Week 9 Homework: The Case of the Missing Festival Lanterns.

Read HOMEWORK_BRIEF.md for the full assignment instructions.

Run tests with:

    pytest -q

Do not solve this by only printing output.
The function must return a report dictionary.
"""

EXPECTED_LANTERNS = {
    "river-dragon",
    "blue-crane",
    "moon-rabbit",
    "gold-tiger",
    "white-lotus",
    "red-kite",
}

LANTERN_LOG = [
    ("river-dragon", "North Gate"),
    ("blue-crane", "River Walk"),
    ("moon-rabbit", "River Walk"),
    ("river-dragon", "North Gate"),
    ("gold-tiger", "Market Street"),
    ("silver-fox", "Market Street"),
    ("red-kite", "South Bridge"),
]

CORRECT_SECTIONS = {
    "river-dragon": "North Gate",
    "blue-crane": "River Walk",
    "moon-rabbit": "River Walk",
    "gold-tiger": "Market Street",
    "white-lotus": "Temple Road",
    "red-kite": "Temple Road",
}


def analyze_lanterns(
    expected_lanterns: set[str],
    lantern_log: list[tuple[str, str]],
    correct_sections: dict[str, str],
) -> dict[str, object]:
    """Analyze festival lantern records and return a report.

    Args:
        expected_lanterns:
            A set of lantern names that should appear at the festival.
        lantern_log:
            A list of records. Each record is a tuple:
            (lantern_name, actual_section).
        correct_sections:
            A dictionary where each key is an expected lantern name and each
            value is the section where that lantern should appear.

    Returns:
        A dictionary with these keys:
            - "seen_lanterns": set[str]
            - "missing_lanterns": set[str]
            - "unexpected_lanterns": set[str]
            - "duplicate_lanterns": set[str]
            - "count_by_section": dict[str, int]
            - "wrong_section_lanterns": dict[str, dict[str, str]]

    Important rules:
        - Return the dictionary. Do not only print it.
        - Only expected lanterns should be checked for wrong sections.
        - Unexpected lanterns should not appear in wrong_section_lanterns.
        - If an expected lantern appears in more than one wrong section, record
          the first wrong section found in the log.
    """

    # TODO 1: Create the collections you need.
    # Suggested names:
    # seen_lanterns = set()
    # seen_once = set()
    # duplicate_lanterns = set()
    # count_by_section = {}
    # wrong_section_lanterns = {}

    # TODO 2: Loop through lantern_log.
    # Each record has:
    # lantern_name, actual_section

    # TODO 3: During the loop:
    # - add each lantern name to seen_lanterns
    # - use seen_once to detect duplicate lantern names
    # - count how many records appear in each section
    # - check wrong sections for expected lanterns only

    # TODO 4: After the loop, use set operations:
    # missing_lanterns = expected_lanterns - seen_lanterns
    # unexpected_lanterns = seen_lanterns - expected_lanterns

    # TODO 5: Return the full report dictionary with all required keys.

    raise NotImplementedError("Complete analyze_lanterns in src/challenges.py")


if __name__ == "__main__":
    report = analyze_lanterns(EXPECTED_LANTERNS, LANTERN_LOG, CORRECT_SECTIONS)
    print(report)
