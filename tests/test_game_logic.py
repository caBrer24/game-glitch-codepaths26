from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty


# --- Original scaffold tests ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Bug 1: Hint direction was backwards ---
# Original: guess > secret returned "Too High" but said "Go HIGHER!" (should say "Go LOWER!")
# Fix: swapped message strings so Too High → Go LOWER, Too Low → Go HIGHER

def test_high_guess_outcome_is_too_high():
    # 99 > 93 — player guessed too high, must go lower
    assert check_guess(99, 93) == "Too High"

def test_low_guess_outcome_is_too_low():
    # 10 < 93 — player guessed too low, must go higher
    assert check_guess(10, 93) == "Too Low"


# --- Bug 2: Type juggling converted secret to string on even attempts ---
# Original: on even attempts, secret was cast to str, causing lexicographic comparison
# e.g. str(10) > str(9) is False ("10" < "9"), so check_guess(10, 9) wrongly returned "Too Low"
# Fix: removed the str() cast; secret is always compared as int

def test_double_digit_vs_single_digit_compares_numerically():
    # "10" < "9" lexicographically — if type juggling were still present this would fail
    assert check_guess(10, 9) == "Too High"

def test_int_comparison_is_not_lexicographic():
    assert check_guess(8, 9) == "Too Low"


# --- Bug 3 & 4: Score went negative; Too High gained points on even attempts ---
# Original: Too High on even attempts added 5 points; no floor of 0
# Fix: both outcomes always subtract 5, floored at max(0, ...)

def test_score_does_not_go_negative_on_too_high():
    assert update_score(0, "Too High", 1) >= 0

def test_score_does_not_go_negative_on_too_low():
    assert update_score(0, "Too Low", 1) >= 0

def test_too_high_and_too_low_deduct_equally():
    # Before fix, Too High on even attempts gained 5; Too Low always lost 5
    assert update_score(20, "Too High", 2) == update_score(20, "Too Low", 2)

def test_wrong_guess_deducts_five_when_score_allows():
    assert update_score(20, "Too High", 1) == 15
    assert update_score(20, "Too Low", 1) == 15


# --- Bug 5: Win score minimum floors at 10 ---
# Original: 100 - 10*(attempt+1) could go negative on very late wins
# Fix: added if points < 10: points = 10

def test_win_score_never_goes_below_ten():
    assert update_score(0, "Win", 100) >= 10

def test_win_score_rewards_early_guess():
    # Win on attempt 1: 100 - 10*(1+1) = 80
    assert update_score(0, "Win", 1) == 80


# --- Bug 6: Empty/invalid inputs should not count as attempts ---
# Original: attempts incremented before parse_guess; empty submit burned an attempt
# Fix: moved attempts += 1 inside the valid-guess block (tested via parse_guess behavior)

def test_empty_string_is_invalid():
    ok, _, _ = parse_guess("")
    assert not ok

def test_none_is_invalid():
    ok, _, _ = parse_guess(None)
    assert not ok

def test_non_numeric_string_is_invalid():
    ok, _, _ = parse_guess("abc")
    assert not ok

def test_valid_number_parses_correctly():
    ok, value, _ = parse_guess("42")
    assert ok
    assert value == 42

def test_float_string_truncates_to_int():
    ok, value, _ = parse_guess("7.9")
    assert ok
    assert value == 7


# --- Bug 7: Hard difficulty range was 1-50 (easier range than Normal's 1-100) ---
# Fix: Hard range changed to 1-200 so difficulty scales correctly

def test_hard_range_is_larger_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_easy_range_is_smaller_than_normal():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high
