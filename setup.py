import os
from setuptools import setup, find_packages

with open('README.rst') as fd:
    long_description = fd.read()


def get_version():
    p = os.path.join(os.path.dirname(
                     os.path.abspath(__file__)), "django_datatools/__init__.py")
    with open(p) as f:
        for line in f.readlines():
            if "__version__" in line:
                return line.strip().split("=")[-1].strip(" '")
    raise ValueError("could not read version")


def main():
    setup(
        name='django-datatools',
        description='Data Tools for Django models',
        include_package_data=True,
        long_description=long_description,
        version=get_version(),
        license='MIT license',
        platforms=['unix', 'linux', 'osx', 'win32'],
        author='Michael Chiciak',
        author_email='mchicia1@gmail.com',
        url='https://github.com/MChiciak/django-datatools',
        python_requires='>=3.0',
        packages=find_packages(),
    )


if __name__ == '__main__':
    main()
