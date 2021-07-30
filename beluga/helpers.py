from typing import Tuple, Collection, Union
import numpy as np


def display_helper(raw_metrics: dict, header: str = "") -> bool:
    """A helper function to print out the calculated metrics

    Args:
        raw_metrics (dict): The input metrics to print
        header (str, optional): The title of the metrics. Defaults to "".

    Raises:
        ValueError: If the input metrics are not in Dictionary format

    Returns:
        bool: True if the print succeeds, False otherwise
    """

    if not isinstance(raw_metrics, dict):
        raise ValueError("Your raw metrics is not a dictionary")

    max_label_len = max([len(str(lab)) for lab in raw_metrics.keys()] + [5])

    try:
        print()
        if header:
            print(header)

        print("=" * (max_label_len + 9))
        for key, val in raw_metrics.items():
            key = str(key).ljust(max_label_len + 2, " ")
            print("{0} {1:.4f}".format(key, val))
        print("=" * (max_label_len + 9))
        print()

    except Exception:
        return False

    return True


def summary_display(summary_data: dict, total_acc: Union[dict, bool]) -> bool:
    """Displays the given metrics in a formatted way

    Args:
        summary_data (dict): The input metrics to be displayed
        total_acc (Union[dict, bool]): The total model accuracy

    Raises:
        ValueError: If the input metrics are not in Dictionary format

    Returns:
        bool: True if the print succeeds, False otherwise
    """

    if not isinstance(summary_data, dict) or not isinstance(total_acc, dict):
        raise ValueError("Your summary data is not a dictionary")

    labels = list([i.keys() for i in summary_data.values()][0])
    max_label_len = max([len(str(labe)) for labe in labels] + [5])
    max_len = max_label_len + 52

    headers = list(summary_data.keys())
    data: dict = {}
    for label in labels:
        for metrics in summary_data.values():
            for key, val in metrics.items():
                if key == label:
                    data[label] = data.get(label, []) + [val]

    total_acc = round(list(total_acc.values())[0], 4)

    try:
        print()
        print(("{0:^" + str(max_len) + "}").format("Machine Learning Model Summary"))
        print("=" * (max_len))
        print(
            (
                "| {0:^"
                + str(max_label_len)
                + "}  {1:^10}  {2:^10}  {3:^10}  {4:^10} |"
            ).format("Label", headers[0], headers[1], headers[2], headers[3])
        )
        for lab, dat in data.items():
            print(
                (
                    "| {0:^"
                    + str(max_label_len)
                    + "}  {1:^10.4f}  {2:^10.4f}  {3:^10.4f}  {4:^10.4f} |"
                ).format(lab, dat[0], dat[1], dat[2], dat[3])
            )
        print("-" * (max_len))
        print(
            ("| {0:^" + str(max_len - 4) + "} |").format(
                "Total Model Accuracy =  " + str(total_acc)
            )
        )
        print("=" * (max_len))
        print()

    except Exception:
        return False

    return True


def array_check(
    array_1: Collection, array_2: Collection
) -> Tuple[np.ndarray, np.ndarray]:
    """A helper function to check if the given arrays are valid

    Args:
        array_1 (Collection): The first array to check
        array_2 (Collection): The second array to check

    Raises:
        TypeError: If either of the given arrays are not iterable
        ValueError: If the arrays are not of the same length
        ValueError: If both of the arrays are empty

    Returns:
        Tuple[np.ndarray, np.ndarray]: Numpy arrays ready for future processing
    """

    try:
        iter(array_1)
        iter(array_2)
    except TypeError:
        raise TypeError("Your data is not iterable, check your input data") from None

    if len(array_1) != len(array_2):
        raise ValueError("Your arrays do not match in length")

    if len(array_1) == 0 and len(array_2) == 0:
        raise ValueError("You passed empty arrays")

    if isinstance(array_1, np.ndarray) and isinstance(array_2, np.ndarray):
        return array_1, array_2

    return np.array(array_1), np.array(array_2)
