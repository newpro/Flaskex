"""Import application as package
"""
from setuptools import setup

setup(
    name='flaskex',
    packages=['flaskex'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
