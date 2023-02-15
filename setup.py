from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in power_stuffs/__init__.py
from power_stuffs import __version__ as version

setup(
	name="power_stuffs",
	version=version,
	description="calculate power total of site, inverter, add record site, inveter power pwer hour",
	author="Tung",
	author_email="phuongtung0801@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
