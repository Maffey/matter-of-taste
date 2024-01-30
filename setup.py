from setuptools import setup, find_packages

# TODO make it a pyproject.toml
# TODO C:\Users\matiu\PycharmProjects\matter-of-taste\matter_of_taste does not contain any element
setup(
    name="matter-of-taste",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "matter-of-taste = main:run",
        ],
    },
)
