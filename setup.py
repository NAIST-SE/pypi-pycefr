from setuptools import setup, find_packages

setup(
    name='pycefr',
    packages=find_packages(),
    package_data={'pycefr': ['data/*']}
    install_requires=['requests'],
    python_requires='>=3'
)