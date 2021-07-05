# a CK entry for detection/setup of the environment for pip zenodo_get package

Installation using pip ( external to CK ) :
```
$ python3 -m pip install zenodo_get --user
```

Detection:
```
$ ck detect soft --tags=lib,python-package,zenodo_get
```

Usage:
```
$ ck virtual env --tags=python-package,zenodo_get --shell_cmd="zenodo_get"
```

Cleanup (removal of the CK entry only) :
```
$ ck clean env --tags=python-package,zenodo_get -f
```

Uninstallation using pip ( external to CK ) :
```
$ python3 -m pip uninstall zenodo_get
```
