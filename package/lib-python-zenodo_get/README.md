# a CK entry for instsalling the zenodo_get package

Installation:
```
$ ck install package --tags=lib,python-package,zenodo_get
```

Usage:
```
$ ck virtual env --tags=python-package,zenodo_get --shell_cmd="zenodo_get"
```

Cleanup (removal of the CK entry together with the package itself) :
```
$ ck clean env --tags=python-package,zenodo_get -f
```
