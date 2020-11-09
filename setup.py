from setuptools import find_packages, setup
import sys

if __name__ == "__main__":

    with open("requirements.txt") as f:
        reqs = f.read()

    ms = find_packages(where=".")
    setup(
        name="aflr_client",
        version="0.0.1",
        description="Aflorithmic Client",
        url="git@https://github.com/aflorithmic/aflr_client.git",
        author="Aflorithmic Team",
        author_email="volodymyr@aflorithmic.ai",
        license="unlicense",
        packages=find_packages(),
        install_requires=reqs.strip().split("\n"),
        include_package_data=True,
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Natural Language :: English",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.8",
        ],
    )