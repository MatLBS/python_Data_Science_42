# ft_package

**ft_package** is a beginner-friendly Python project aimed at helping you understand how to build, structure, and distribute your own Python package.

## 📦 What is ft_package?

This package was created as an educational exercise to:

- Learn how Python packages are structured.
- Create reusable code in modules.
- Build and install your package locally using `setuptools`.

## Build

```
python(3) setup.py sdist bdist_wheel
```

## Install

```
pip3 install ./dist/ft_package-0.0.1.tar.gz
```

## Display

```
pip3 show -v ft_package
```

## Test

```
python(3) tester.py
```

## Uninstall

```
pip3 uninstall ft_package
```