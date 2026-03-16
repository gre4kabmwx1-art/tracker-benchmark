from tracker_benchmark.metrics import iou


def run_example():
    box_a = [0, 0, 100, 100]
    box_b = [50, 50, 150, 150]

    score = iou(box_a, box_b)

    print(f"IoU score: {score:.4f}")