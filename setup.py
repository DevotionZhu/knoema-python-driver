from setuptools import setup

def readme():
    with open('README.rst') as readme_file:
        return readme_file.read()

setup(
  name = 'knoema',
  packages = ['knoema'],
  version = '1.0.21b1',
  description = "Official Python package for Knoema's API",
  long_description=readme(),
  author = 'Knoema',
  author_email = 'info@knoema.com',
  license='MIT',
  url = 'https://github.com/Knoema/knoema-python-driver',
  keywords = ['API', 'knoema'],
  classifiers = ['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only'],
  install_requires=['pandas']
)
