from setuptools import find_packages,setup
from typing import List

hyp_e='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if hyp_e in requirements:
            requirements.remove(hyp_e)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Swaroop',
author_email='swarooppnayar@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)