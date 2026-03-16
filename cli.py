import click

from tracker_benchmark.metrics import iou
from tracker_benchmark.compare import compare_scores


@click.group()
def cli():
    pass


def parse_box(box_str):
    return [int(x) for x in box_str.split(",")]


@cli.command()
@click.option("--box-a", required=True, help="Box A: x1,y1,x2,y2")
@click.option("--box-b", required=True, help="Box B: x1,y1,x2,y2")
def run(box_a, box_b):
    """Calculate IoU for two boxes."""
    box_a = parse_box(box_a)
    box_b = parse_box(box_b)

    score = iou(box_a, box_b)
    print(f"IoU score: {score:.4f}")


@cli.command()
@click.option("--score-a", required=True, type=float, help="First score")
@click.option("--score-b", required=True, type=float, help="Second score")
def compare(score_a, score_b):
    """Compare two scores."""
    print(compare_scores(score_a, score_b))


if __name__ == "__main__":
    cli()