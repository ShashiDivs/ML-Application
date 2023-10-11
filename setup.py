import os,sys
from setuptools import setup,find_packages
from typing import List


NAME = "cost_prediction"
AUTHOUR = "shashi"
AUTHOUR_MAIL= "shashilisas@gmail.com"
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_DOT_E = "-e ."

def get_rquirements()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

    if HYPHEN_DOT_E in requirement_list:
        requirement_list.remove(HYPHEN_DOT_E)

    return requirement_list


setup( name = NAME,
      version = "0.0.1",
      description="Data Science project",
      author=AUTHOUR,
      author_email=AUTHOUR_MAIL,
      packages=find_packages(),
      install_requires = get_rquirements()

)
