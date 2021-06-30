#
# Collective Knowledge (individual environment - setup)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#

import os
import sys

##############################################################################

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


    # Get variables
    ck=i['ck_kernel']

    iv=i.get('interactive','')

    cus=i.get('customize',{})

    hosd=i['host_os_dict']
    tosd=i['target_os_dict']

    winh=hosd.get('windows_base','')

    full_path               = cus.get('full_path','')
    path_lib                = os.path.dirname(full_path)
    path_build              = os.path.dirname(path_lib)

    env                     = i['env']
    env['PYTHONPATH']       = path_build + ( ';%PYTHONPATH%' if winh=='yes' else ':${PYTHONPATH}')

    # The following assumes the package has been installed (rather than detected) :
    #
    path_install            = os.path.dirname(path_build)
    path_bin                = os.path.join(path_install, 'python_deps_site', 'bin')

    if os.path.isdir(path_bin):
        env['PATH']         = path_bin + ( ';%PATH%' if winh=='yes' else ':${PATH}')

    return {'return':0, 'bat':''}
