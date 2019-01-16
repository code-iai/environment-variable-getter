from setuptools import setup

setup(
    name='environment-variable-getter',
    version='0.0.0',
    url='https://github.com/code-iai/environment-variable-getter',
    license='MIT',
    author='University of Bremen; Navid Jadid',
    author_email='jadid.navid@yahoo.de',
    description='A package to safely retrieve environment variables',
    py_modules=['environment_variable_getter'],
    tests_require=['pytest']
)
