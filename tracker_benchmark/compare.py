def compare_scores(score_a: float, score_b: float) -> str:
    if score_a > score_b:
        return "Score A is better"
    if score_b > score_a:
        return "Score B is better"
    return "Scores are equal"