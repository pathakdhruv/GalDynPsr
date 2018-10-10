import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="GalDynPsr",
    version="0.0.1",
    author="Dhruv Pathak",
    author_email="pathakdhruv9786@gmail.com",
    license='New BSD',
    description="A practise package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pathakdhruv/GalDynPsr",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
