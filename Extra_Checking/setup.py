from setuptools import setup, find_packages

setup(
    name='FileStatsAnalyzer',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/yourusername/FileStatsAnalyzer',
    license='MIT',
    author='MasterCard007',
    author_email='',
    description='A utility script to analyze file statistics in directories or external drives.',
    install_requires=[
        'humanize',
    ],
    entry_points={
        'console_scripts': [
            'filestatsanalyzer=filestatsanalyzer.main:main',
        ],
    },
)
