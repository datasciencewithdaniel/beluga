import numpy as np


def display_helper(raw_metrics, header=""):

    max_label_len = max([len(str(lab)) for lab in raw_metrics.keys()])

    if header:
        print(header)

    print("=" * (max_label_len + 9))
    for key, val in raw_metrics.items():
        key = str(key).ljust(max_label_len + 2, " ")
        print("{0} {1:.4f}".format(key, val))
    print("=" * (max_label_len + 9))

    return True


# def error_check(metric_1, metric_2):  # POTENTIALLY REMOVE
#     if metric_1 + metric_2 == 0:
#         raise ZeroDivisionError("You tried to divide by zero, check your input data")
#     if metric_1 + metric_2 < 0:
#         raise ValueError("Your metric does not make sense, check your input data")
#     return True


def array_check(array_1, array_2):
    try:
        iter(array_1)
        iter(array_2)
    except TypeError:
        raise TypeError("Your data is not iterable, check your input data") from None

    if len(array_1) != len(array_2):
        raise ValueError("Your arrays do not match in length")

    if isinstance(array_1, np.ndarray) and isinstance(array_2, np.ndarray):
        return array_1, array_2
    return np.array(array_1), np.array(array_2)
