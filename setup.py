from setuptools import setup, find_packages

# Package metadata
NAME = 'CipherFlex'
VERSION = '1.0.0'
DESCRIPTION = 'Python package for medium encryption and decryption'
AUTHOR = 'Your Name'
EMAIL = 'your.email@example.com'
URL = 'https://github.com/your-username/CipherFlex'
LICENSE = 'MIT'
KEYWORDS = ['encryption', 'decryption', 'security']
PYTHON_REQUIRES = '>=3.6'  # Minimum Python version required

# Read the README file for the long description
with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

# Define the dependencies
install_requires = []

# Define the entry points (optional)
entry_points = {
    'console_scripts': [
        'cipherflex-cli = CipherFlex.cli:main',  # Replace CipherFlex.cli with your CLI module
    ],
}

# Setup configuration
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license=LICENSE,
    keywords=KEYWORDS,
    python_requires=PYTHON_REQUIRES,
    packages=find_packages(),
    install_requires=install_requires,
    entry_points=entry_points,
)
