from setuptools import find_packages,setup
import typing from List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    ''''
    This function returns the list of requirements
    ''''
    requirements=[]
    with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace("\n","") for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
name='BISystem',
version='0.1',
author='Jona',
author_mail='kimanthijona@gmail.com',
packages=find_packages()
install_requires=get_requirements('requirements.txt')

)
