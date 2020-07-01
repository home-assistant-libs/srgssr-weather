from setuptools import setup, find_packages


long_description = open("README.md").read()

setup(
    name="srgssr-weather",
    version="0.1.0",
    license="Apache License 2.0",
    url="https://github.com/home-assistant-libs/srgssr-weather",
    author="Pascal Vizeli",
    author_email="pvizeli@syshack.ch",
    description="Python module to talk to SRGSSR weather API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["srgssr_weather"],
    zip_safe=True,
    platforms="any",
    install_requires=list(val.strip() for val in open("requirements.txt")),
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
