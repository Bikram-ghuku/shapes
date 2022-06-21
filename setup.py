from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='GeometricShapes',
    packages=find_packages(include=['shapes']),
    version='0.1.4',
    description='Making calculations of geometric shapes easier',
    author='BikramGhuku',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Bikram-ghuku/shapes",
    license='MIT',
    install_requires=['scipy==1.8.1'],
    tests_require=['pytest==4.4.1'],
    test_suite='test.py',
)
