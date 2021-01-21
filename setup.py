from setuptools import setup, find_packages


def requires():
    with open("requirements.txt") as f:
        return [i.strip() for i in f.readlines()]


setup(
    name="finder",
    author="Pinwheel",
    author_email="redacted for now, I didn't make that email in time. Got taken.", # oops
    version="0.0.1", # ahahaa
    description="finds whatever you need :eyes:",
    url="htts://github.com/P1nwheels/finder",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requires(),
    entry_points="""
        [console_scripts]
        finder=finder.main:cli
    """
)