# Beluga - make predictions, get metrics

[![License](https://img.shields.io/github/license/datasciencewithdaniel/beluga?style=plastic)](https://github.com/datasciencewithdaniel/beluga/blob/main/LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg?style=plastic)](https://github.com/psf/black)
[![Last Commit](https://img.shields.io/github/last-commit/datasciencewithdaniel/beluga?style=plastic)](https://github.com/datasciencewithdaniel/beluga/commits/main)
[![Contributors](https://img.shields.io/github/contributors/datasciencewithdaniel/beluga?style=plastic)](https://github.com/datasciencewithdaniel/beluga/graphs/contributors)
[![Size](https://img.shields.io/github/repo-size/datasciencewithdaniel/beluga?style=plastic)]()
[![Issues](https://img.shields.io/github/issues/datasciencewithdaniel/beluga?style=plastic)](https://github.com/datasciencewithdaniel/beluga/issues)
[![Discord](https://img.shields.io/discord/851059417562742854?style=plastic)](https://discord.gg/D3KfXbdZgk)

Beluga is a Python library that provides easy access to all of the metrics you need in your multiclass classification tasks. We were inspired by [this](https://www.youtube.com/watch?v=0qRgWubbPxQ) friendly Beluga whale to help others in their Machine Learning projects.

Check out the [Issues](https://github.com/datasciencewithdaniel/beluga/issues) for future functionality and progress such as support for regression tasks and metric visualisations.

## Overview

  - Get various metrics on your predictions
  - ...
  - ...

## Installation [TODO]

To install this library you can use Pypi via pip

```
pip install beluga
```

## Usage

Import beluga into your project

```py
import beluga
```


## Documentation

Methods in metrics have following parameters:

* **predictions** - (Iterable) predictions output from your model
* **ground_truth** - (Iterable) ground truth values to compare against
* **raw** - (bool). *Optional*. Use to get metrics in a dictionary instead of printing. Default: *False*.

### Methods list:

**true_positive**: description

**true_negative**: ...

**false_positive**: ...

**false_negative**: ...

**precision**: ...

**recall**: ...

**sensitivity**: ...

**specificity**: ...

**f1**: ...

**accuracy**: ...

### Examples

```py
beluga.metrics.true_positive([1, 1, 1, 0, 0], [1, 0, 1, 0, 0])
>>> True Positive
    ==========
    0   2.0000
    1   2.0000
    ==========

beluga.metrics.recall(['cat', 'dog', 'dog'], ['cat', 'dog', 'dog'])
>>> Recall
    ============
    cat   1.0000
    dog   1.0000
    ============

beluga.metrics.f1(['Elon Musk', 'Tim Cook', 'robot'], ['Elon Musk', 'Tim Cook', 'Mark Zuckerberg'])
>>> F1 score
    ========================
    Elon Musk         1.0000
    Mark Zuckerberg   0.0000
    Tim Cook          1.0000
    ========================
```

## Running Code
Run the code from the home direcotry for any development as follows:
```
python -m beluga.metrics
```
This should return nothing as all development tests have been removed.
## Tests
Run the tests from the library home directory with the following:
```
python -m setup pytest
```
Check the coverage of these tests using:
```
pytest --cov=beluga tests/ --cov-report term-missing
```

## License

GPL-3.0 License

#
Beluga uses open source packages to work properly:

* [numpy](https://github.com/numpy/numpy) - The fundamental package for scientific computing with Python.

And of course **beluga** itself is open source with a [public repository](https://github.com/datasciencewithdaniel/beluga) on GitHub.
