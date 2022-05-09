
from setuptools import setup, find_packages

setup(
    name='hunga_bunga',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Brute-Force All of sklearn!',
    long_description=open('README.txt').read(),
    install_requires=['numpy', 'scipy', 'joblib', 'scikit-learn', 'tabulate', 'tqdm'],
    url='https://github.com/Bruno81930/HungaBunga',
    author='Yam Peleg',
    author_email='yam@deeptrading.com'
)
