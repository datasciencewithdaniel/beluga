import numpy as np
import pytest
from beluga import metrics
from beluga import helpers

IN1 = np.array(["1", "1", "0"])
IN2 = np.array(["4", "5", "6"])
IN3: list = ["1"]
IN4: list = []
IN5: int = 1
IN6: dict = {0: 2, 1: 3}


def test_true_positive():

    output = metrics.true_positive(IN1, IN1, raw=True)

    assert isinstance(output, dict)
    assert output["1"] == 2
    assert output["0"] == 1
    assert len(output) == len(np.unique(IN1))

    with pytest.raises(KeyError):
        output["2"] != 0

    output = metrics.true_positive(IN1, IN2, raw=True)

    assert sum(output.values()) == 0

    output = metrics.true_positive(IN1, IN1)

    assert output is True

    with pytest.raises(TypeError):
        output = metrics.true_positive(IN3, raw=True)

    with pytest.raises(ValueError):
        output = metrics.true_positive(IN3, IN4)
    with pytest.raises(TypeError):
        output = metrics.true_positive(IN5, IN5, raw=True)


def test_true_negative():

    output = metrics.true_negative(IN1, IN1, raw=True)

    assert isinstance(output, dict)
    assert output["1"] == 1
    assert output["0"] == 2
    assert len(output) == len(np.unique(IN1))

    with pytest.raises(KeyError):
        output["2"] != 0

    output = metrics.true_negative(IN3, IN3, raw=True)

    assert sum(output.values()) == 0

    output = metrics.true_negative(IN1, IN1)

    assert output is True

    with pytest.raises(TypeError):
        output = metrics.true_negative(IN3, raw=True)

    with pytest.raises(ValueError):
        output = metrics.true_negative(IN3, IN4)
    with pytest.raises(TypeError):
        output = metrics.true_negative(IN5, IN5, raw=True)


def test_false_positive():

    output = metrics.false_positive(IN1, IN1, raw=True)

    assert isinstance(output, dict)
    assert output["1"] == 0
    assert output["0"] == 0
    assert len(output) == len(np.unique(IN1))

    with pytest.raises(KeyError):
        output["2"] != 0

    output = metrics.false_positive(IN3, IN3, raw=True)

    assert sum(output.values()) == 0

    output = metrics.false_positive(IN1, IN1)

    assert output is True

    with pytest.raises(TypeError):
        output = metrics.false_positive(IN3, raw=True)

    with pytest.raises(ValueError):
        output = metrics.false_positive(IN3, IN4)
    with pytest.raises(TypeError):
        output = metrics.false_positive(IN5, IN5, raw=True)


def test_false_negative():

    output = metrics.false_negative(IN1, IN1, raw=True)

    assert isinstance(output, dict)
    assert output["1"] == 0
    assert output["0"] == 0
    assert len(output) == len(np.unique(IN1))

    with pytest.raises(KeyError):
        output["2"] != 0

    output = metrics.false_negative(IN3, IN3, raw=True)

    assert sum(output.values()) == 0

    output = metrics.false_negative(IN1, IN1)

    assert output is True

    with pytest.raises(TypeError):
        output = metrics.false_negative(IN3, raw=True)

    with pytest.raises(ValueError):
        output = metrics.false_negative(IN3, IN4)
    with pytest.raises(TypeError):
        output = metrics.false_negative(IN5, IN5, raw=True)


def test_precision():

    output = metrics.precision(IN1, IN1, raw=True)

    assert isinstance(output, dict)
    assert isinstance(output["1"], float)
    assert output["1"] == 1.0
    assert output["0"] == 1.0
    assert len(output) == len(np.unique(IN1))

    with pytest.raises(KeyError):
        output["2"] != 0

    output = metrics.precision(IN1, IN2, raw=True)

    assert sum(output.values()) == 0
    assert output["4"] == 0.0

    output = metrics.precision(IN1, IN1)

    assert output is True

    with pytest.raises(TypeError):
        output = metrics.precision(IN3, raw=True)

    with pytest.raises(ValueError):
        output = metrics.precision(IN3, IN4)
    with pytest.raises(TypeError):
        output = metrics.precision(IN5, IN5, raw=True)


def test_recall():

    output = metrics.recall(IN1, IN1, raw=True)

    assert isinstance(output, dict)
    assert isinstance(output["1"], float)
    assert output["1"] == 1.0
    assert output["0"] == 1.0
    assert len(output) == len(np.unique(IN1))

    with pytest.raises(KeyError):
        output["2"] != 0

    output = metrics.recall(IN1, IN2, raw=True)

    assert sum(output.values()) == 0
    assert output["4"] == 0.0

    output = metrics.recall(IN1, IN1)

    assert output is True

    with pytest.raises(TypeError):
        output = metrics.recall(IN3, raw=True)

    with pytest.raises(ValueError):
        output = metrics.recall(IN3, IN4)
    with pytest.raises(TypeError):
        output = metrics.recall(IN5, IN5, raw=True)


def test_sensitivity():

    assert metrics.sensitivity(IN1, IN1, raw=True) == metrics.recall(IN1, IN1, raw=True)
    assert metrics.sensitivity(IN1, IN2, raw=True) == metrics.recall(IN1, IN2, raw=True)

    output = metrics.sensitivity(IN1, IN1)

    assert output is True


def test_specificity():

    output = metrics.specificity(IN1, IN1, raw=True)

    assert isinstance(output, dict)
    assert isinstance(output["1"], float)
    assert output["1"] == 1.0
    assert output["0"] == 1.0
    assert len(output) == len(np.unique(IN1))

    with pytest.raises(KeyError):
        output["2"] != 0

    output = metrics.specificity(IN3, IN3, raw=True)

    assert sum(output.values()) == 0
    assert output["1"] == 0.0

    output = metrics.specificity(IN1, IN1)

    assert output is True

    with pytest.raises(TypeError):
        output = metrics.specificity(IN3, raw=True)

    with pytest.raises(ValueError):
        output = metrics.specificity(IN3, IN4)
    with pytest.raises(TypeError):
        output = metrics.specificity(IN5, IN5, raw=True)


def test_f1():

    output = metrics.f1(IN1, IN1, raw=True)

    assert isinstance(output, dict)
    assert isinstance(output["1"], float)
    assert output["1"] == 1.0
    assert output["0"] == 1.0
    assert len(output) == len(np.unique(IN1))

    with pytest.raises(KeyError):
        output["2"] != 0

    output = metrics.f1(IN1, IN2, raw=True)

    assert sum(output.values()) == 0
    assert output["4"] == 0.0

    output = metrics.f1(IN1, IN1)

    assert output is True

    with pytest.raises(TypeError):
        output = metrics.f1(IN3, raw=True)

    with pytest.raises(ValueError):
        output = metrics.f1(IN3, IN4)
    with pytest.raises(TypeError):
        output = metrics.f1(IN5, IN5, raw=True)


def test_accuracy():

    output = metrics.accuracy(IN1, IN1, raw=True)

    assert isinstance(output, dict)
    assert isinstance(output["1"], float)
    assert output["1"] == 1.0
    assert output["0"] == 1.0
    assert len(output) == len(np.unique(IN1))

    with pytest.raises(KeyError):
        output["2"] != 0

    output = metrics.accuracy(IN1, IN1)

    assert output is True

    output = metrics.accuracy(IN3, IN3, raw=True)

    assert sum(output.values()) == 1.0
    assert output["1"] == 1.0

    with pytest.raises(TypeError):
        output = metrics.accuracy(IN3, raw=True)
    with pytest.raises(ValueError):
        output = metrics.accuracy(IN3, IN4)
    with pytest.raises(TypeError):
        output = metrics.accuracy(IN5, IN5, raw=True)


def test_model_accuracy():

    output = metrics.model_accuracy(IN1, IN1, raw=True)

    assert isinstance(output, dict)
    assert isinstance(output["Total"], float)
    assert output["Total"] == 1.0
    assert len(output) == 1

    with pytest.raises(KeyError):
        output["2"] != 0

    output = metrics.model_accuracy(IN1, IN1)

    assert output is True

    output = metrics.model_accuracy(IN3, IN3, raw=True)

    assert sum(output.values()) == 1.0
    assert output["Total"] == 1.0

    with pytest.raises(TypeError):
        output = metrics.model_accuracy(IN3, raw=True)
    with pytest.raises(ValueError):
        output = metrics.model_accuracy(IN3, IN4)
    with pytest.raises(TypeError):
        output = metrics.model_accuracy(IN5, IN5, raw=True)


def test_summary():

    output = metrics.summary(IN1, IN1)
    assert output is True

    output = metrics.summary(IN1, IN1, conditions=True)
    assert output is True


def test_array_check():

    assert isinstance(IN3, list)

    new3, _ = helpers.array_check(IN3, IN3)

    assert isinstance(new3, np.ndarray)

    with pytest.raises(ValueError):
        helpers.array_check(IN4, IN4)
