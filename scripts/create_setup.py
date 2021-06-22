
# TODO: Run poetry build using python interpreter, unzip tar file, copy setup.py to root folder
# TODO: Root dir is cwd
#
"poetry build"
"tar -xvf dist/*.tar.gz '*/setup.py'"
"cp -R $(find . -name setup.py) setup.py"