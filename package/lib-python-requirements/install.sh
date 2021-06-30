#! /bin/bash

#
# CK installation script
#
# See CK LICENSE for licensing details.
# See CK COPYRIGHT for copyright details.
#

# PACKAGE_DIR
# INSTALL_DIR
# PYTHON_REQUIREMENTS_PATH
# PIP_INSTALL_OPTIONS

if [ -z "$PYTHON_REQUIREMENTS_PATH" ]; then
    echo "PYTHON_REQUIREMENTS_PATH does not have a value"
    echo "Please install with --env.PYTHON_REQUIREMENTS_PATH=/path/to/requirements.txt --extra_tags=for.project.alpha"
    exit 1
fi

if [ -d "$PYTHON_REQUIREMENTS_PATH" ]; then
    PYTHON_REQUIREMENTS_PATH=${PYTHON_REQUIREMENTS_PATH}/requirements.txt
fi

if [ ! -f "$PYTHON_REQUIREMENTS_PATH" ]; then
    echo "PYTHON_REQUIREMENTS_PATH='${PYTHON_REQUIREMENTS_PATH}' does not exist"
    echo "Please install with --env.PYTHON_REQUIREMENTS_PATH=/path/to/requirements.txt --extra_tags=for.project.alpha"
    exit 1
fi

echo "**************************************************************"
echo ""
echo "Cleanup: removing ${INSTALL_DIR}"
rm -rf ${INSTALL_DIR:-nonexistent_dir}/*

    # This is where pip will install the modules.
    # It has its own funny structure we don't control :
    #
EXTRA_PYTHON_SITE=${INSTALL_DIR}/python_deps_site
mkdir -p ${EXTRA_PYTHON_SITE}/lib
ln -s lib ${EXTRA_PYTHON_SITE}/lib64

SHORT_PYTHON_VERSION=`${CK_ENV_COMPILER_PYTHON_FILE} -c 'import sys;print(sys.version[:3])'`
export PACKAGE_LIB_DIR="${EXTRA_PYTHON_SITE}/lib/python${SHORT_PYTHON_VERSION}/site-packages"
export PYTHONPATH=$PACKAGE_LIB_DIR:$PYTHONPATH

######################################################################################
echo "Installing python requirements from '${PYTHON_REQUIREMENTS_PATH}' to '${PACKAGE_LIB_DIR}' ..."

${CK_ENV_COMPILER_PYTHON_FILE} -m pip install -r ${PYTHON_REQUIREMENTS_PATH} --prefix=${EXTRA_PYTHON_SITE} ${PIP_INSTALL_OPTIONS}

if [ "${?}" != "0" ] ; then
  echo "Error: installation failed!"
  exit 1
fi

cp ${PYTHON_REQUIREMENTS_PATH} ${INSTALL_DIR}/installed_requirements.txt

    # Because we have to provide a fixed name via meta.json ,
    # and $PACKAGE_LIB_DIR depends on the Python version,
    # we solve it by creating a symbolic link with a fixed name.
    #
ln -s $PACKAGE_LIB_DIR ${INSTALL_DIR}/build
