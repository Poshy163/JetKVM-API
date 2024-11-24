from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="JetKVM",
    version="0.0.1",
    author="Joshua Leaper",
    author_email="poshernater@outlook.com",
    description="A Python library to access your JetKVM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Poshy163/JetKVM-API",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
