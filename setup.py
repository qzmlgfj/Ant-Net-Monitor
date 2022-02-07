from gettext import install
from setuptools import setup, find_packages

setup(
    name='ant_net_monitor',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask_cors',
        'click',
        'psutil',
        'dataclasses',
    ]
)