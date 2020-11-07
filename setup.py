import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='purge',  
    version='0.1',
    scripts=['dokr'] ,
    author="Abdul Aleem Qureshi",
    author_email="aleem75321@gmail.com",
    description="Delete temp file as per patthen",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aleem75321/Purge.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
