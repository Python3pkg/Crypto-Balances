import cryptobalances
from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='cryptobalances',
    version=cryptobalances.__version__,
    author='Aliaksandr Leonau',
    author_email='leonov.aleksandr.1987@gmail.com',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={
        'cryptobalances': ['data/*.json'],
    },
    description='Python module for getting the balance of a various crypto currency',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    url='https://github.com/AleksandrLeonov/Crypto-Balances',
    platforms='Linux',
    entry_points={
        'console_scripts': ['main=cryptobalances.main:main'],
    },
    test_suite='tests'
)
