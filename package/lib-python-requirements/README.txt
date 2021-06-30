
$ ck install package --tags=lib,python-package,requirements --env.PYTHON_REQUIREMENTS_PATH=${HOME}/CK/ck-env/package/lib-python-requirements/requirements_a.txt --extra_tags=for.project.alpha --force_version=alpha

$ ck install package --tags=lib,python-package,requirements --env.PYTHON_REQUIREMENTS_PATH=${HOME}/CK/ck-env/package/lib-python-requirements/requirements_b.txt --extra_tags=for.project.beta --force_version=beta

$ ck show env --tags=python-package,requirements

$ ck virtual env --tags=requirements,for.project.alpha --shell_cmd="python3 -c 'import numpy; print(numpy.__version__)'"
1.16.2

$ ck virtual env --tags=requirements,for.project.beta --shell_cmd="python3 -c 'import numpy; print(numpy.__version__)'"
1.16.4
