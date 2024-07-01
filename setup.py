from setuptools import find_packages ,  setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file__path:str)->List[str] : 
    
    '''this fn will return the list of req'''
    requirement=[]
    with open(file__path) as file_obj :
        requirement=file_obj.readlines()
        requirement=[req.replace("/n","") for req in requirement]
        
        if HYPEN_E_DOT in requirement :
            requirement.remove(HYPEN_E_DOT)
            
    return requirement
    
setup (
    
    name = 'mlproject',
    version= '0.0.7',
    author = 'sachin',
    author_email='sachinbhai7990@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
    
    
    )


