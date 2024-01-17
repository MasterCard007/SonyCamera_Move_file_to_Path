
from setuptools import setup, find_packages

setup(
    name='DiskVolumeFileOrganizer',
    version='1.0.0',
    author='MasterCard007',
    author_email='',
    description='A utility script for organizing and copying files from specific disk volumes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/yourusername/your-repo-name',
    packages=find_packages(),
    install_requires=[
        'tqdm',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
