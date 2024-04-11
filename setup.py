
from setuptools import setup, find_packages

setup(
    name='SonyCamToPath',
    version='0.2.1',
    packages=find_packages(),
    description='A script to process images from Sony Cameras',
    author='Your Name',
    author_email='enochliliwy@gmail.com',
    install_requires=[
        'Pillow',   # For PIL.Image
        'tqdm',     # For progress bar
        'exifread'  # For reading EXIF data
    ],
    python_requires='>=3.6',
)
