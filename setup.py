from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

with open("requirements.txt", 'r') as f:
    requires = f.read()


setup(
    name='library_name',
    version='0.1.0',
    description='library description',
    license="MIT",
    long_description=long_description,
    author='My Name',
    author_email='My EMail',
    packages=['library name'],
    python_requires=">=3.7,<3.11",
    install_requires=requires
)
