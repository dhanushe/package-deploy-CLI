from __future__ import print_function, unicode_literals
import regex
import os
from termcolor import colored
from datetime import date

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

questions = [
    {
        'type': 'input',
        'name': 'p-name',
        'message': 'What\'s your package name?',
    },
    {
        'type': 'list',
        'name': 'license',
        'message': 'What license do you need?',
        'choices':
        [
            'MIT license',
            'Apache License, Version 2.0',
            'GNU General Public License',
            'GNU LGPL',
            'Common Development and Distribution License 1.0',
            'Creative Commons Zero v1.0 Universal',
            'Skip for now',
        ],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'input',
        'name': 'version',
        'message': 'Provide project version (such as 0.0.1):',
        'default': '0.0.1'
    },
    {
        'type': 'input',
        'name': 's-description',
        'message': 'Provide a sentence description:',
        'default': ''
    },
    {
        'type': 'input',
        'name': 'l-description',
        'message': 'Provide a long description:',
        'default': ''
    },
    {
        'type': 'input',
        'name': 'author-name',
        'message': 'Provide Creator Name:',
        'default': ''
    },
    {
        'type': 'input',
        'name': 'author-email',
        'message': 'Provide Creator Email:',
        'default': ''
    },
    {
        'type': 'input',
        'name': 'url',
        'message': 'Provide Website URL (Optional):',
        'default': ''
    },
    {
        'type': 'list',
        'name': 'pythonver',
        'message': 'Select Python Version',
        'choices':
        [
            'V2',
            'V3',
            'V4',
        ],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'input',
        'name': 'keywords',
        'message': 'Provide Keywords (pertaining to package) separated by space:',
        'default': ''
    },
    {
        'type': 'input',
        'name': 'filetypes',
        'message': 'Provide file types in module code (.txt .py) seperated by space:',
        'default': ''
    },
    {
        'type': 'list',
        'name': 'devstatus',
        'message': 'Select Your Current Development Status',
        'choices':
        [
            '1 - Planning Copy',
            '2 - Pre-Alpha Copy.',
            '3 - Alpha Copy',
            '4 - Beta Copy',
            '5 - Production/Stable Copy',
            '6 - Mature Copy',
            '7 - Inactive Copy',
        ],
        'filter': lambda val: val.lower()
    },
]


def main():
    owd = os.getcwd()
    print(colored('Welcome to package-deploy. Create Your Python Package Files', 'green'))
    print('This will create files in the current directory you are in')
    answers = prompt(questions, style=style)
    pprint(answers)

    # Create the folder
    if answers['p-name'] is not None and len(answers['p-name']) > 0:
        os.mkdir(answers['p-name'])
    else:
        print(colored('Package name is required', 'red'))
        print(colored('Program Terminated', 'red'))
        return

    # Create the README.txt File
    try:
        file = open('README.txt', 'x')
        file.close()
    except:
        print(colored("README.txt Already Exists", 'red'))
    try:
        file = open('README.md', 'x')
        file.close()
    except:
        print(colored("README.md Already Exists", 'red'))

    # Add Title and Long Description to README.md File
    try:
        file = open('README.md', 'a')
        file.write('# ' + answers['p-name'] + '\n')
        file.write(answers['l-description'] + '\n')
        file.close()
    except:
        print(colored(
            "README.md could not be edited. Add title and description manually.", 'red'))

    # Add Title and Long Description to README.txt File
    try:
        file = open('README.txt', 'a')
        file.write(answers['p-name'] + '\n')
        file.write(answers['l-description'] + '\n')
        file.close()
    except:
        print(colored(
            "README.txt could not be edited. Add title and description manually.", 'red'))

    # Create the LICENSE.txt File
    try:
        file = open('LICENSE.txt', 'x')
        file.close()
    except:
        print(colored("LICENSE.txt Already Exists", 'red'))

    # Change first line of LICENSE.txt to have the current year and author
    os.chdir(r"{}/licenses".format(os.getcwd()))
    if answers['license'] == 'mit license':
        file = open('mit.txt', 'r')
        lines = file.readlines()
        lines[0] = f"Copyright {date.today().year} {answers['author-name']}"
        file.close()
    elif answers['license'] == 'apache license, version 2.0':
        file = open('apache.txt', 'r')
        lines = file.readlines()
        file.close()
    elif answers['license'] == 'gnu general public license':
        file = open('gpl.txt', 'r')
        lines = file.readlines()
        file.close()
    elif answers['license'] == 'gnu lgpl':
        file = open('lgpl.txt', 'r')
        lines = file.readlines()
        file.close()
    elif answers['license'] == 'common development and distribution license 1.0':
        file = open('cddl.txt', 'r')
        lines = file.readlines()
        file.close()
    elif answers['license'] == 'creative commons zero v1.0 universal':
        file = open('cc0.txt', 'r')
        lines = file.readlines()
        file.close()
    elif answers['license'] == 'skip for now':
        lines = ["all rights are reversed"]

    os.chdir(owd)  # Change back to original directory

    file = open('LICENSE.txt', 'w')
    file.writelines(lines)
    file.close()

    # Create the setup.py File
    try:
        file = open('setup.py', 'x')
        file.close()
    except:
        print(colored("setup.py Already Exists", 'red'))

    # Create the __init__.py File
    try:
        os.chdir(r"{}/{}".format(os.getcwd(), answers['p-name']))
        file = open('__init__.py', 'x')
        file.close()
    except:
        print(colored("__init__.py Already Exists", 'red'))

    os.chdir(owd)  # Change back to original directory
    print(os.getcwd())

    try:
        file = open('setup.py', 'a')
        file.write('from setuptools import setup, find_packages\n')
        file.write('setup(\n')
        file.write('    name="' + answers['p-name'] + '",\n')
        file.write('    version="' + answers['version'] + '",\n')
        file.write('    description="' + answers['l-description'] + '",\n')
        file.write('    long_description=open("README.md").read(),\n')
        file.write('    long_description_content_type="text/markdown",\n')
        file.write('    url="' + answers['url'] + '",\n')
        file.write('    author="' + answers['author-name'] + '",\n')
        file.write('    author_email="' + answers['author-email'] + '",\n')
        file.write('    license="' + answers['license'] + '",\n')
        file.write('    packages=find_packages(),\n')
        file.write('    keywords="' + answers['keywords'] + '",\n')
        file.write("    install_requires=[''],\n")
        file.write('    classifiers=[\n')
        file.write('        "Programming Language :: Python :: ' +
                answers['pythonver'] + '",\n')
        file.write('    ],\n')
        file.write(')')
        file.close()
    except:
        print(colored("setup.py could not be edited. Add all the information manually.", 'red'))


if __name__ == '__main__':
    main()
