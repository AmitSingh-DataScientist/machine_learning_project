from setuptools import setup, find_packages
from typing import List

## Decalring variables for setup function
PROJECT_NAME = "hosuing-predictor"
VERSION = "0.0.3"
AUTHOR = "Amit Kumar Singh" 
DESCRIPTION = "This is a first FSDS Nov batch Machine Learning Project"
#PACKAGES = ["housing"] #it could be a list of folders name, here we have only one
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mentioned in requirements.txt file
    Return : This function is going to return a list which contains name of libraries mentioned
    in requirements.txt file 
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name = PROJECT_NAME,
version = VERSION,
author  = AUTHOR,
description = DESCRIPTION,
packages = find_packages(), #PACKAGES : #find_packages() returns all the folder name where __init__ is there
install_requires = get_requirements_list() #External libraries required to run and function will return those one by one as a list
)