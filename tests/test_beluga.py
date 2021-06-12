import beluga.metrics as metrics


def test_true_positive():
    assert metrics.true_positive([1, 1, 0], [1, 1, 0]) == 2
    assert metrics.true_positive([1, 1, 0], [1, 1, 0]) != 1
    # NEED TO HAVE MORE ROBUST TESTS


def test_true_negative():
    assert metrics.true_negative([1, 1, 0], [1, 1, 0]) == 1
    assert metrics.true_negative([1, 1, 0], [1, 1, 0]) != 2


# NEED TO WRITE FOR THE REMAINING FUNCTIONS
