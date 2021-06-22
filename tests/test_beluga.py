import numpy as np
from beluga import metrics


def test_true_positive():
    assert isinstance(
        metrics.true_positive(
            np.array(["1", "1", "0"]), np.array(["1", "1", "0"]), raw=True
        ),
        dict,
    )


#     assert metrics.true_positive([1, 1, 0], [1, 1, 0]) == 2
#     assert metrics.true_positive([1, 1, 0], [1, 1, 0]) != 1
#     # NEED TO HAVE MORE ROBUST TESTS


# def test_true_negative():
#     assert metrics.true_negative([1, 1, 0], [1, 1, 0]) == 1
#     assert metrics.true_negative([1, 1, 0], [1, 1, 0]) != 2


# def test_false_positive():
#     assert metrics.false_positive([1, 1, 0], [1, 1, 0]) == 0
#     assert metrics.false_positive([1, 1, 0], [1, 1, 0]) != 1


# def test_false_negative():
#     assert metrics.false_negative([1, 1, 0], [1, 1, 0]) == 0
#     assert metrics.false_negative([1, 1, 0], [1, 1, 0]) != 1


# NEED TO WRITE FOR THE REMAINING FUNCTIONS
