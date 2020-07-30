import os
import re
import shutil
import sys

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('xenditclient')

if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    if os.system("twine check dist/*"):
        print("twine check failed. Packages might be outdated.")
        print("Try using `pip install -U twine wheel`.\nExiting.")
        sys.exit()
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('xenditclient.egg-info')
    sys.exit()

setup(
    name='xenditclient',
    version=version,
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
