from setuptools import setup, find_packages

setup(
    name='Flask App Ed',
    version='1.6',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)