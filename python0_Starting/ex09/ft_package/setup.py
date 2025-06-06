import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name='ft_package',
	version='0.1.0',
	description='A sample test package but above all my first python package',
	long_description = long_description,
	long_description_content_type = "text/markdown",
	# url='https://github.com/eagle/ft_package',
	author='matle-br',
	author_email='matle-br@student.42.fr',
	license='MIT',
	packages=['pyexample'],
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	package_dir = {"": "src"},
	packages = setuptools.find_packages(where="src"),
	python_requires = ">=3.6"
)