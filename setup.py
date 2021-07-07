from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="beluga-ml",
    packages=find_packages(include=["beluga"]),
    version="1.0.0",
    description="A Python library to help make your Machine Learning easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Data Science with Daniel",
    url="https://github.com/datasciencewithdaniel/beluga",
    license="GPL-3.0",
    install_requires=["numpy"],
    setup_requires=["pytest-runner", "pytest-cov"],
    tests_require=["pytest"],
    test_suite="tests",
)
