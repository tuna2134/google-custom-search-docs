import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()

setuptools.setup(
    name="google-custom-search",
    version="0.1.3",
    author="DMS",
    author_email="masato190411@gmail.com",
    description="This is for google custom search api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuna2134/google-custom-search",
    install_requires=_requires_from_file('rqs.txt'),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)