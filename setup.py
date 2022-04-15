from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dehqaan/__init__.py
from dehqaan import __version__ as version

setup(
	name="dehqaan",
	version=version,
	description="Dehqaan",
	author="Dehaqan",
	author_email="erpnextaddon@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
