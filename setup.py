from setuptools import setup, find_packages


def requires():
    with open("requirements.txt") as f:
        return [i.strip() for i in f.readlines()]


setup(
    name="findit", # changed name because a buddy just told me apples file manager is called Finder
    author="Pinwheel",
    author_email="pnwheelz0x13@gmail.com",
    version="0.0.3", # ahahaa
    description="finds whatever you need :eyes:",
    url="htts://github.com/P1nwheels/finder",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requires(),
    entry_points="""
        [console_scripts]
        findit=findit.main:cli
    """
)