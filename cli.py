import click

from tracker_benchmark.runner import run_example


@click.group()
def cli():
    pass


@cli.command()
def run():
    """Run example benchmark."""
    run_example()


if __name__ == "__main__":
    cli()