from setuptools import setup

setup(
    name='NFC commit footer validation',
    version='0.1.0',
    py_modules=['main'],
    license='MIT',
    long_description='this is a long description',
    install_requires=['gitpython'],
    entry_points = {
        'console_scripts': ['commit_footer=cli:main'],
    },
)
