#
# Collective Knowledge (individual environment - setup)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer(s):
# - Leo Gordon, lg4@krai.ai
#
#   This generic soft entry
#       * floats anchor_depth times up the filesystem tree from the anchor file
#       * expands local path variables like .MODEL_PATH=<relative_path> to CK_ENV..._MODEL_PATH=<absolute_path>
#       * expands local non-path variables like _WINDOW_WIDTH=<value> to CK_ENV..._WINDOW_WIDTH=<value>

##############################################################################
# setup environment setup

def setup(i):
    """
    Input:  {
              cfg              - meta of this soft entry
              self_cfg         - meta of module soft
              ck_kernel        - import CK kernel module (to reuse functions)

              host_os_uoa      - host OS UOA
              host_os_uid      - host OS UID
              host_os_dict     - host OS meta

              target_os_uoa    - target OS UOA
              target_os_uid    - target OS UID
              target_os_dict   - target OS meta

              target_device_id - target device ID (if via ADB)

              tags             - list of tags used to search this entry

              env              - updated environment vars from meta
              customize        - updated customize vars from meta

              deps             - resolved dependencies for this soft

              interactive      - if 'yes', can ask questions, otherwise quiet
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              bat          - prepared string for bat file
            }

    """

    import os

    ck              = i['ck_kernel']
    iv              = i.get('interactive','')

    cus             = i.get('customize',{})
    env_prefix      = cus['env_prefix']
    full_path       = cus.get('full_path','')
    install_env     = cus.get('install_env', {})

    anchor_depth    = int(cus.get('anchor_depth', 0))
    install_root    = full_path
    for _ in range(anchor_depth):       # float that many dir.levels up
        install_root = install_root 
        install_root = os.path.dirname(install_root)

    env             = i['env']
    env[env_prefix] = full_path

    ## Run through hidden/local ienv variables and promote them into env_prefix namespace of the environment being built:
    #
    for varname in install_env.keys():
        if varname.startswith('__'):    # relative paths become absolute paths here
            env[env_prefix + varname[1:] ] = os.path.join(install_root, install_env[varname])
        elif varname.startswith('_'):   # local ienv variables simply get imported into env_prefix namespace
            env[env_prefix + varname] = install_env[varname]

    return {'return':0, 'bat':''}
