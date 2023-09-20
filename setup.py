from setuptools import find_packages, setup



setup(name= 'MLproject1', 
      version = '0.0.1', 
      author= 'Abhishek Patel', 
      author_email='patelabhi2192@gmail.com',
      packages=find_packages(),
      install_requires = ['pandas','numpy','seaborn']
      )