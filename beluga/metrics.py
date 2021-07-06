from typing import Union
from .helpers import np, Collection
from . import helpers


def true_positive(
    predictions: Collection, ground_truth: Collection, raw: bool = False
) -> Union[dict, bool]:
    """Number of correctly classified labels of the positive class

    Args:
        predictions (Collection): Predicted classes from the model
        ground_truth (Collection): Correct classes from the data
        raw (bool, optional): If the raw metrics are to be returned.
            Defaults to False.

    Returns:
        Union[dict, bool]: The raw metrics if specified,
            otherwise the output of the printing function
    """

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
    predictions: Collection, ground_truth: Collection, raw: bool = False
) -> Union[dict, bool]:
    """Number of correctly classified labels of the negative class

    Args:
        predictions (Collection): Predicted classes from the model
        ground_truth (Collection): Correct classes from the data
        raw (bool, optional): If the raw metrics are to be returned.
            Defaults to False.

    Returns:
        Union[dict, bool]: The raw metrics if specified,
            otherwise the output of the printing function
    """

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
    predictions: Collection, ground_truth: Collection, raw: bool = False
) -> Union[dict, bool]:
    """Number of incorrectly classified labels of the postive class

    Args:
        predictions (Collection): Predicted classes from the model
        ground_truth (Collection): Correct classes from the data
        raw (bool, optional): If the raw metrics are to be returned.
            Defaults to False.

    Returns:
        Union[dict, bool]: The raw metrics if specified,
            otherwise the output of the printing function
    """

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
    predictions: Collection, ground_truth: Collection, raw: bool = False
) -> Union[dict, bool]:
    """Number of incorrectly classified labels of the negative class

    Args:
        predictions (Collection): Predicted classes from the model
        ground_truth (Collection): Correct classes from the data
        raw (bool, optional): If the raw metrics are to be returned.
            Defaults to False.

    Returns:
        Union[dict, bool]: The raw metrics if specified,
            otherwise the output of the printing function
    """

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
    predictions: Collection, ground_truth: Collection, raw: bool = False
) -> Union[dict, bool]:
    """Percentage of positive class predictions that are correct

    Args:
        predictions (Collection): Predicted classes from the model
        ground_truth (Collection): Correct classes from the data
        raw (bool, optional): If the raw metrics are to be returned.
            Defaults to False.

    Returns:
        Union[dict, bool]: The raw metrics if specified,
            otherwise the output of the printing function
    """

    tp = true_positive(predictions, ground_truth, raw=True)
    fp = false_positive(predictions, ground_truth, raw=True)

    raw_metrics = {}

    if isinstance(tp, dict) and isinstance(fp, dict):

        for (tp_key, tp_val) in tp.items():
            if tp_val == 0 and fp[tp_key] == 0:
                raw_metrics[tp_key] = 0
            else:
                raw_metrics[tp_key] = tp_val / (tp_val + fp[tp_key])

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "Precision")


def recall(
    predictions: Collection, ground_truth: Collection, raw: bool = False
) -> Union[dict, bool]:
    """Percentage of correctly classified labels from the positive class

    Args:
        predictions (Collection): Predicted classes from the model
        ground_truth (Collection): Correct classes from the data
        raw (bool, optional): If the raw metrics are to be returned.
            Defaults to False.

    Returns:
        Union[dict, bool]: The raw metrics if specified,
            otherwise the output of the printing function
    """

    tp = true_positive(predictions, ground_truth, raw=True)
    fn = false_negative(predictions, ground_truth, raw=True)

    raw_metrics = {}

    if isinstance(tp, dict) and isinstance(fn, dict):

        for (tp_key, tp_val) in tp.items():
            if tp_val == 0 and fn[tp_key] == 0:
                raw_metrics[tp_key] = 0
            else:
                raw_metrics[tp_key] = tp_val / (tp_val + fn[tp_key])

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "Recall")


def sensitivity(
    predictions: Collection, ground_truth: Collection, raw: bool = False
) -> Union[dict, bool]:
    """Percentage of correctly classified labels from the positive class

    Args:
        predictions (Collection): Predicted classes from the model
        ground_truth (Collection): Correct classes from the data
        raw (bool, optional): If the raw metrics are to be returned.
            Defaults to False.

    Returns:
        Union[dict, bool]: The raw metrics if specified,
            otherwise the output of the printing function
    """

    raw_metrics = recall(predictions, ground_truth, raw=True)

    if raw:
        return raw_metrics

    if isinstance(raw_metrics, dict):
        out = helpers.display_helper(raw_metrics, "Sensitivity")

    return out


def specificity(
    predictions: Collection, ground_truth: Collection, raw: bool = False
) -> Union[dict, bool]:
    """Percentage of correctly classified labels from the negative class

    Args:
        predictions (Collection): Predicted classes from the model
        ground_truth (Collection): Correct classes from the data
        raw (bool, optional): If the raw metrics are to be returned.
            Defaults to False.

    Returns:
        Union[dict, bool]: The raw metrics if specified,
            otherwise the output of the printing function
    """

    tn = true_negative(predictions, ground_truth, raw=True)
    fp = false_positive(predictions, ground_truth, raw=True)

    raw_metrics = {}

    if isinstance(tn, dict) and isinstance(fp, dict):

        for (tn_key, tn_val) in tn.items():
            if tn_val == 0 and fp[tn_key] == 0:
                raw_metrics[tn_key] = 0
            else:
                raw_metrics[tn_key] = tn_val / (tn_val + fp[tn_key])

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "Specificity")


def f1(
    predictions: Collection, ground_truth: Collection, raw: bool = False
) -> Union[dict, bool]:
    """The harmomic mean of precision and recall

    Args:
        predictions (Collection): Predicted classes from the model
        ground_truth (Collection): Correct classes from the data
        raw (bool, optional): If the raw metrics are to be returned.
            Defaults to False.

    Returns:
        Union[dict, bool]: The raw metrics if specified,
            otherwise the output of the printing function
    """

    prec = precision(predictions, ground_truth, raw=True)
    rec = recall(predictions, ground_truth, raw=True)

    raw_metrics = {}

    if isinstance(prec, dict) and isinstance(rec, dict):

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
    predictions: Collection, ground_truth: Collection, raw: bool = False
) -> Union[dict, bool]:
    """Percentage of correctly classified labels

    Args:
        predictions (Collection): Predicted classes from the model
        ground_truth (Collection): Correct classes from the data
        raw (bool, optional): If the raw metrics are to be returned.
            Defaults to False.

    Returns:
        Union[dict, bool]: The raw metrics if specified,
            otherwise the output of the printing function
    """

    tp = true_positive(predictions, ground_truth, raw=True)
    tn = true_negative(predictions, ground_truth, raw=True)
    fp = false_positive(predictions, ground_truth, raw=True)
    fn = false_negative(predictions, ground_truth, raw=True)

    raw_metrics = {}

    if (
        isinstance(tp, dict)
        and isinstance(tn, dict)
        and isinstance(fp, dict)
        and isinstance(fn, dict)
    ):

        for (tp_key, tp_val) in tp.items():
            raw_metrics[tp_key] = (tp_val + tn[tp_key]) / (
                tp_val + fp[tp_key] + fn[tp_key] + tn[tp_key]
            )

    if raw:
        return raw_metrics

    return helpers.display_helper(raw_metrics, "Accuracy")
