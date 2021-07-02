import numpy as np
from typing import Tuple, Iterable


def display_helper(raw_metrics: dict, header: str = "") -> bool:

    if not isinstance(raw_metrics, dict):
        raise ValueError("Raw metrics is not a dict")

    max_label_len = max([len(str(lab)) for lab in raw_metrics.keys()])

    try:
        if header:
            print(header)

        print("=" * (max_label_len + 9))
        for key, val in raw_metrics.items():
            key = str(key).ljust(max_label_len + 2, " ")
            print("{0} {1:.4f}".format(key, val))
        print("=" * (max_label_len + 9))

    except Exception:
        return False

    return True


def array_check(array_1: Iterable, array_2: Iterable) -> Tuple[np.ndarray, np.ndarray]:

    try:
        iter(array_1)
        iter(array_2)
    except TypeError:
        raise TypeError("Your data is not iterable, check your input data") from None

    if len(array_1) != len(array_2):
        raise ValueError("Your arrays do not match in length")

    if len(array_1) == 0 or len(array_2) == 0:
        raise ValueError("You passed empty arrays")

    if isinstance(array_1, np.ndarray) and isinstance(array_2, np.ndarray):
        return array_1, array_2

    return np.array(array_1), np.array(array_2)
