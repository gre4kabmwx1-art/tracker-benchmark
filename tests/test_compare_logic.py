from tracker_benchmark.compare import compare_scores


def test_compare_scores_a_better():
    assert compare_scores(0.9, 0.8) == "Score A is better"


def test_compare_scores_b_better():
    assert compare_scores(0.7, 0.8) == "Score B is better"


def test_compare_scores_equal():
    assert compare_scores(0.8, 0.8) == "Scores are equal"