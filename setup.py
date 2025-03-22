from setuptools import setup, find_packages

setup(
    name='fpt_gic_auto_driving',
    version=open('VERSION').read(),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'crash=crash.__init__:main',  # or whichever function handles CLI
        ],
    },
)