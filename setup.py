import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "monitoring-plugins-apparmor",
	version = "1.0",
	author = "Mathieu Grzybek",
	author_email = "mathieu@grzybek.fr",
	description = "This script checks the state of resources and nodes.",
	license = "GPLv3",
	keywords = "monitoring check apparmor activity",
	url = "https://github.com/mgrzybek/monitoring-plugins-apparmor",
	packages = ['monitoring_plugins_apparmor'],
	data_files = [('/usr/lib/nagios/plugins',['bin/check_aa_profile', 'bin/check_aa_status'])],
	install_requires = ['pynagios', 'sudo'],
	long_description = read('README.md'),
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Topic :: Utilities",
		"Environment :: Console",
		"License :: OSI Approved :: GPLv3 License"
	],
)
