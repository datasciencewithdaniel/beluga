from setuptools import find_packages, setup

setup(
    name="beluga",
    packages=find_packages(include=["beluga"]),
    version="0.1.0",
    description="A Python library to help make your Machine Learning easier",
    author="Data Science with Daniel",
    license="MIT",
    install_requires=["numpy"],
    setup_requires=["pytest-runner", "pytest-cov"],
    tests_require=["pytest"],
    test_suite="tests",
)
