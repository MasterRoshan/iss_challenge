from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='iss_io',
    version='0.1',
    description='Get some information about the ISS over REST',
    long_description=long_description,
    url='https://github.com/MasterRoshan/iss_challenge',
    author='TJ Johnson',
    classifiers=[
        'Development Status :: Alpha',
        'Intended Audience :: Hiring Manager',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    py_modules=["iss_io"],
    python_requires='>=3.6, <4',
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'iss_io=iss_io:main',
        ],
    }
)
