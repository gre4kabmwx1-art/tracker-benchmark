from tracker_benchmark.runner import run_example


def test_run_example(capsys):
    run_example()
    captured = capsys.readouterr()

    assert "IoU score:" in captured.out