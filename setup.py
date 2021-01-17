from setuptools import setup, find_packages

# Changes between releases or new pypi projects
__VERSON__ = "20200116.2"
__package_name__ = "comment_header_creator"
__url__ = "https://github.com/daxm/python_comment_header_creator"
__description__ = "Create nicely formatted comment strings to be used as headers/seperators in your code."

# Stays the same (for me).
__username__ = "daxm"
__author__ = "Dax Mickelson"
__author_email = "dmickels@cisco.com"
__license__ = "BSD"
__name__ = f"{__package_name__}"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=__name__,
    version=__VERSON__,
    author=__author__,
    author_email=__author_email,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
