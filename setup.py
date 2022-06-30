#!/usr/bin/env python
"""Setup script for the py-pip-install-test package."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = ["pytest==7.1.1"]

test_requirements = [
    "pandas",
    "matplotlib",
    "sql",
    "pytest>=3",
]

setup(
    author="Ermias",
    email="jermitesh20@gmail.com",
    python_requires=">=3.6",
    description="CAUSAL_INFERENCE",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="Agritech, lidar, USGS, pytest",
    name="CAUSAL-INFERENCE",
    packages=find_packages(include=["src", "src.*"]),
    test_suite="Tests",
    tests_require=test_requirements,
    url="https://github.com/Jeremy-Tesh/causal-inference",
    version="0.1.0",
    zip_safe=False,
)