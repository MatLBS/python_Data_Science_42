import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package but above all my first python package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    url=(
        'https://github.com/MatLBS/python_Data_Science_42/tree/main/python_0_Starting/ex09/src/ft_package'
    ),
    author='matle-br',
    author_email='matle-br@student.42.fr',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires=">=3.6"
)
