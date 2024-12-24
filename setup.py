from setuptools import setup, find_packages

setup(
    name="execA",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'executable-file=execA.main:main',
        ],
    },
)
