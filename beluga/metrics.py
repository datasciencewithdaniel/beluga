import numpy as np
from typing import Iterable


def true_positive(predictions: Iterable[int], ground_truth: Iterable[int]) -> int:
    return sum(
        [1 if p == 1 and g == 1 else 0 for p, g in zip(predictions, ground_truth)]
    )  # CONVERT TO USING NUMPY ARRAY


def true_negative(predictions: Iterable[int], ground_truth: Iterable[int]) -> int:
    return sum([1 for p, g in zip(predictions, ground_truth) if p == 0 and g == 0])


def false_positive(predictions: Iterable[int], ground_truth: Iterable[int]) -> int:
    return sum([1 for p, g in zip(predictions, ground_truth) if p == 1 and g == 0])


def false_negative(predictions: Iterable[int], ground_truth: Iterable[int]) -> int:
    return sum([1 for p, g in zip(predictions, ground_truth) if p == 0 and g == 1])


def precision(predictions: Iterable[int], ground_truth: Iterable[int]) -> float:
    tp = true_positive(predictions, ground_truth)
    fp = false_positive(predictions, ground_truth)
    error_check(tp, fp)
    return tp / (tp + fp)


def recall(predictions: Iterable[int], ground_truth: Iterable[int]) -> float:
    tp = true_positive(predictions, ground_truth)
    fn = false_negative(predictions, ground_truth)
    error_check(tp, fn)
    return tp / (tp + fn)


def sensitivity(predictions: Iterable[int], ground_truth: Iterable[int]) -> float:
    return recall(predictions, ground_truth)


def specificity(predictions: Iterable[int], ground_truth: Iterable[int]) -> float:
    tn = true_negative(predictions, ground_truth)
    fp = false_positive(predictions, ground_truth)
    error_check(tn, fp)
    return tn / (tn + fp)


def f1(predictions: Iterable[int], ground_truth: Iterable[int]) -> float:
    prec = precision(predictions, ground_truth)
    rec = recall(predictions, ground_truth)
    error_check(prec, rec)
    return (2 * prec * rec) / (prec + rec)


def error_check(metric_1, metric_2):
    if metric_1 + metric_2 == 0:
        raise ZeroDivisionError("You tried to divide by zero, check your input data")
    elif metric_1 + metric_2 < 0:
        raise ValueError("Your metric does not make sense, check your input data")
    return True
