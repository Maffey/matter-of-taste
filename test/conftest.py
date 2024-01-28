from src.recipe_translator import install_nltk_modules


def pytest_configure(config):
    install_nltk_modules()
