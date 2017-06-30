all: deb rpm

build:
	python setup.py build

rpm:
	which rpm && python setup.py bdist_rpm || exit 0

deb:
	which apt-get && python setup.py --command-packages=stdeb.command bdist_deb || exit 0
