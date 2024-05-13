from setuptools import setup, find_packages

setup(
    name='shopping_page',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'shopping_page = shopping_page.main:main'
        ]
    },
    install_requires=[
        # Por el momento sin dependencias
    ]
)
