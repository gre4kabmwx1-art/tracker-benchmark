from click.testing import CliRunner
from cli import cli


def test_cli_run():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        ["run", "--box-a", "0,0,100,100", "--box-b", "50,50,150,150"]
    )

    assert result.exit_code == 0
    assert "IoU score:" in result.output