import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Derivatives-YDAI47", # Replace with your own username
    version="0.0.1",
    author="Yu Dai",
    author_email="ydai49@fordham.edu",
    description="Option Pricng Package for European/American/Bermuda/Asian option with Closed Form or Numerical Solution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ydai49/Derivatives",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
