import numpy as np
from typing import Iterable


def check_length_matching(*lists: Iterable[list]) -> True or Exception:
    for list_ in lists[1:]:
        if len(list_) != len(lists[0]):
            raise ValueError("Lengths of given lists aren't matching")
    return True


def true_positive(predictions: Iterable[int], ground_truth: Iterable[int]) -> int:
    check_length_matching(predictions, ground_truth)
    return np.sum(np.array(predictions) & np.array(ground_truth))


def true_negative(predictions: Iterable[int], ground_truth: Iterable[int]) -> int:
    check_length_matching(predictions, ground_truth)
    return np.sum(np.invert(np.array(predictions) | np.array(ground_truth)).astype(bool))


def false_positive(predictions: Iterable[int], ground_truth: Iterable[int]) -> int:
    check_length_matching(predictions, ground_truth)
    return np.sum(np.array(predictions) & np.invert(np.array(ground_truth).astype(bool)))


def false_negative(predictions: Iterable[int], ground_truth: Iterable[int]) -> int:
    check_length_matching(predictions, ground_truth)
    return np.sum(np.invert(np.array(predictions).astype(bool)) & np.array(ground_truth))


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


def error_check(metric_1: int, metric_2: int) -> True or Exception:
    if metric_1 + metric_2 == 0:
        raise ZeroDivisionError("You tried to divide by zero, check your input data")
    elif metric_1 + metric_2 < 0:
        raise ValueError("Your metric does not make sense, check your input data")
    return True
