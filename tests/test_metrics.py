from tracker_benchmark.metrics import iou


def test_iou_overlap():
    box_a = [0, 0, 100, 100]
    box_b = [50, 50, 150, 150]

    result = iou(box_a, box_b)

    assert result > 0


def test_iou_no_overlap():
    box_a = [0, 0, 100, 100]
    box_b = [200, 200, 300, 300]

    result = iou(box_a, box_b)

    assert result == 0.0

def test_iou_full_overlap():
    box_a = [0, 0, 100, 100]
    box_b = [0, 0, 100, 100]

    result = iou(box_a, box_b)

    assert result == 1.0

def test_iou_zero_union_area():
    box_a = [0, 0, 0, 0]
    box_b = [0, 0, 0, 0]

    result = iou(box_a, box_b)

    assert result == 0.0    