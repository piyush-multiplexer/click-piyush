from setuptools import setup

setup(
    name='clickpiyush',
    version='0.1.0',
    py_modules=['clickpiyush'],
    install_requires=['Click', ],
    entry_points={
        'console_scripts': [
            'clickpiyush = clickpiyush:cli'
        ]
    }
)
