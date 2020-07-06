from setuptools import find_packages, setup

from beakertron import __version__

setup(
    name='beakertron',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-Migrate',
        'Flask-SQLAlchemy',
    ],
)
