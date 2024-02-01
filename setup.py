from setuptools import setup, find_packages

setup(
    name="matter-of-taste",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "matter-of-taste = matter_of_taste.main:app",
        ],
    },
)
