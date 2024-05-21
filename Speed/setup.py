
from setuptools import setup, find_packages

setup(
    name='optimized_sony_cam_transfer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'exifread',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'optimized_sony_cam_transfer=optimized_sony_cam_transfer:main',
        ],
    },
    author='MasterCard007',
    author_email='',
    description='A script to automate transferring photos and videos from a Sony camera to a computer, organizing by date and extracting EXIF data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MasterCard007/SonyCamera_Move_file_to_Path',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
