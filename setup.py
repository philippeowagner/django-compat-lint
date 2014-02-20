from setuptools import setup, find_packages


setup(
    name='django-compat-lint',
    url='https://github.com/ubernostrum/django-compat-lint',
    zip_safe=True,
    packages=find_packages(),
    include_package_data=True,
    scripts=['bin/django_compat_lint.py'],
)
