from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs
                    if 'git+' not in x]

setup(
    name='package-deploy',
    description='An effective CLI tool to simplify the process of creating, updating and distributing a python package',
    version='1.0.0',
    packages=find_packages(),  # list of all packages
    install_requires=install_requires,
    python_requires='>=3.0',
    entry_points='''
        [console_scripts]
        pkgdeploy=pkgdeploy.__main__:main
    ''',
    author="Dhanush Eashwar",
    keyword="package, deploy, pypi, publish, make-package",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='',
    download_url='',
    dependency_links=dependency_links,
    author_email='dhanush.eashwar@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
)
