from setuptools import setup, find_packages

setup(
    name='crash',
    description='Crash! auto driving simulation.',
    version=open('VERSION').read(),
    packages=find_packages(),
    install_requires=[
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'crash=crash.__init__:main',  # or whichever function handles CLI
        ],
    },
)