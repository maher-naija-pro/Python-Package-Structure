###########################
#venv
###########################

python3 -m venv nom_environnement
source venv/bin/activate
pour quitter deactivate



###########################
#description
###########################
under Readme.rst update desc


###########################
#install
###########################

sudo pip uninstall py_package
#not use sudo python setup.py develop
#to install package
sudo pip install .



###########################
# test
###########################
execute sous py_package : 
nosetests

or run under py_package

python setup.py test


###########################
# bin generated
###########################
this bin will be generated and accesible on linux as cmd

py_package_my_function
