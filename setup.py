import setuptools

with open("setup.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='unbabel-cli',
    version='1.0',

    author="Ketan Singh",
    author_email="KetanSingh_vsec@yahoo.com",

    description="Coding task for Unbabel",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/KetanSingh11/backend-engineering-challenge",
    packages=setuptools.find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.7',

)