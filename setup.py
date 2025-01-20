from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(filepath)->List[str]:
    
    requirements = []
    with open(filepath,'r') as f:
        requirements =f.readlines()
        requirements =[req.replace("/n","") for req in requirements]
        if (HYPHEN_E_DOT) in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
            return requirements

setup(
    name='Second_hand_car_prices',
    version='0.1',
    packages=find_packages(),
    install_requires =get_requirements('requirements.txt'),
    author='Robin Aluma',
    author_email='alumarobin@gmail.com'
)
