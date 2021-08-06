## Steps to Release as a Python Library

Full guide can be found [here](https://packaging.python.org/tutorials/packaging-projects/).

1. Set the version number by editing the ```setup.py``` file

2. Create the Build:
```
python -m build
```

2. Upload the build to testpypi:
```
python -m twine upload --repository testpypi dist/beluga_ml-<X.X.X>*
```

3. Upload the build to pypi:
```
python -m twine upload --repository pypi dist/beluga_ml-<X.X.X>*
```
