from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='xenditclient',
    version='0.0.3',
    packages=['tests', 'xenditclient'],
    url='https://github.com/dwisulfahnur/python-xendit-client',
    license='BSD 3-Clause',
    author='Dwi Sulfahnur',
    author_email='dwisulfahnur@gmail.com',
    description='Xendit REST API Client for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.6',
    install_requires=['requests>=2.3.0'],
    tests_requires=['pytest>=3.0.6']
)
