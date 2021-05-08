from setuptools import setup, find_packages

setup(
    name = 'aigpyqt',
    version = '2021.3.25.1',
    license = "MIT Licence",
    description = "Python QT Common Tool",

    author = 'Yaronzz',
    author_email = "yaronhuang@foxmail.com",

    packages=find_packages(exclude=[]),
    platforms = "any",
    include_package_data = True,
    install_requires=["aigpy"],
)
