from .helpers import np, Iterable
from . import helpers


def true_positive(
    predictions: Iterable[int], ground_truth: Iterable[int], 
    raw: bool = False) -> dict or bool:

    predictions, ground_truth = helpers.array_check(predictions, ground_truth)

    labels = np.unique(ground_truth)

    raw_metrics = {}

    for lab in labels:

        pred_true = np.where(predictions == lab, 1, 0)
        truth_true = np.where(ground_truth == lab, 1, -1)

        raw_metrics[lab] = np.sum(np.where(pred_true == truth_true, 1, 0))

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "True Positive")


def true_negative(
    predictions: Iterable[int], ground_truth: Iterable[int], 
    raw: bool = False) -> dict or bool:

    predictions, ground_truth = helpers.array_check(predictions, ground_truth)

    labels = np.unique(ground_truth)

    raw_metrics = {}

    for lab in labels:

        pred_true = np.where(predictions != lab, 1, 0)
        truth_true = np.where(ground_truth != lab, 1, -1)

        raw_metrics[lab] = np.sum(np.where(pred_true == truth_true, 1, 0))

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "True Negative")


def false_positive(
    predictions: Iterable[int], ground_truth: Iterable[int], 
    raw: bool = False) -> dict or bool:

    predictions, ground_truth = helpers.array_check(predictions, ground_truth)

    labels = np.unique(ground_truth)

    raw_metrics = {}

    for lab in labels:

        pred_true = np.where(predictions == lab, 1, 0)
        truth_true = np.where(ground_truth != lab, 1, -1)

        raw_metrics[lab] = np.sum(np.where(pred_true == truth_true, 1, 0))

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "False Positive")


def false_negative(
    predictions: Iterable[int], ground_truth: Iterable[int], 
    raw: bool = False) -> dict or bool:

    predictions, ground_truth = helpers.array_check(predictions, ground_truth)

    labels = np.unique(ground_truth)

    raw_metrics = {}

    for lab in labels:

        pred_true = np.where(predictions != lab, 1, 0)
        truth_true = np.where(ground_truth == lab, 1, -1)

        raw_metrics[lab] = np.sum(np.where(pred_true == truth_true, 1, 0))

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "False Negative")


def precision(
    predictions: Iterable[int], ground_truth: Iterable[int], 
    raw: bool = False) -> dict or bool:

    tp = true_positive(predictions, ground_truth, raw=True)
    fp = false_positive(predictions, ground_truth, raw=True)

    raw_metrics = {}

    for (tp_key, tp_val) in tp.items():
        if tp_val == 0 and fp[tp_key] == 0:
            raw_metrics[tp_key] = 0
        else:
            raw_metrics[tp_key] = tp_val / (tp_val + fp[tp_key])

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "Precision")


def recall(predictions: Iterable[int], ground_truth: Iterable[int], 
    raw: bool = False) -> dict or bool:

    tp = true_positive(predictions, ground_truth, raw=True)
    fn = false_negative(predictions, ground_truth, raw=True)

    raw_metrics = {}

    for (tp_key, tp_val) in tp.items():
        if tp_val == 0 and fn[tp_key] == 0:
            raw_metrics[tp_key] = 0
        else:
            raw_metrics[tp_key] = tp_val / (tp_val + fn[tp_key])

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "Recall")


def sensitivity(
    predictions: Iterable[int], ground_truth: Iterable[int], 
    raw: bool = False) -> dict or bool:

    raw_metrics = recall(predictions, ground_truth, raw=True)

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "Sensitivity")


def specificity(
    predictions: Iterable[int], ground_truth: Iterable[int], 
    raw: bool = False) -> dict or bool:

    tn = true_negative(predictions, ground_truth, raw=True)
    fp = false_positive(predictions, ground_truth, raw=True)

    raw_metrics = {}

    for (tn_key, tn_val) in tn.items():
        if tn_val == 0 and fp[tn_key] == 0:
            raw_metrics[tn_key] = 0
        else:
            raw_metrics[tn_key] = tn_val / (tn_val + fp[tn_key])

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "Specificity")


def f1(
    predictions: Iterable[int], ground_truth: Iterable[int], 
    raw: bool = False) -> dict or bool:

    prec = precision(predictions, ground_truth, raw=True)
    rec = recall(predictions, ground_truth, raw=True)

    raw_metrics = {}

    for (prec_key, prec_val) in prec.items():
        if prec_val == 0 and rec[prec_key] == 0:
            raw_metrics[prec_key] = 0
        else:
            raw_metrics[prec_key] = (2 * prec_val * rec[prec_key]) / (
                prec_val + rec[prec_key]
            )

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "F1 score")

 
def accuracy(
    predictions: Iterable[int], ground_truth: Iterable[int], 
    raw: bool = False) -> dict or bool:

    tp = true_positive(predictions, ground_truth, raw=True)
    tn = true_negative(predictions, ground_truth, raw=True)
    fp = false_positive(predictions, ground_truth, raw=True)
    fn = false_negative(predictions, ground_truth, raw=True)

    raw_metrics = {}

    for (tp_key, tp_val) in tp.items():
        raw_metrics[tp_key] = \
            (tp_val + tn[tp_key]) / (tp_val + fp[tp_key] + fn[tp_key] + tn[tp_key])

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "Accuracy")

if __name__ == "__main__":
    true_positive([1, 1, 1, 0, 0], [1, 0, 1, 0, 0])