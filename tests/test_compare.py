from click.testing import CliRunner
from cli import cli


def test_compare_score_b_better():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["compare", "--score-a", "0.71", "--score-b", "0.76"],
    )

    assert result.exit_code == 0
    assert "Score B is better" in result.output


def test_compare_scores_equal():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["compare", "--score-a", "0.80", "--score-b", "0.80"],
    )

    assert result.exit_code == 0
    assert "Scores are equal" in result.output