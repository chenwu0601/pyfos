#!/usr/bin/env python3

# Copyright 2017 Brocade Communications Systems LLC.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may also obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""

:mod:`port_trunk_area_create_add` - PyFOS util for adding or creating a \
port trunk.
************************************************************************\
************
The :mod:`port_trunk_area_create_add` - PyFOS util for adding port members to \
a port area trunk group or creating new port area trunk group.

This module is a stand-alone script for adding port members to \
a port area trunk group or creating new port area trunk group.

* Input:

| Infrastructure options:

|   -i,--ipaddr=IPADDR     The IP address of FOS switch.
|   -L,--login=LOGIN       The login name.
|   -P,--password=PASSWORD The password.
|   -f,--vfid=VFID         The VFID to which the request is \
                           directed [OPTIONAL].
|   -s,--secured=MODE      The HTTPS mode "self" or "CA" [OPTIONAL].
|   -v,--verbose           Verbose mode [OPTIONAL].

* Util Script Options:
    --trunk-index=VALUE    The trunk index of the port area trunk group.
    --trunk-members=PORTS  Ports in slot/port format to be added \
                           to the group. For example: "0/1;0/2"

* Output:
    * Python dictionary content with RESTCONF response data.

"""

import sys
from pyfos import pyfos_auth
from pyfos.pyfos_brocade_fibrechannel_trunk import trunk_area
from pyfos import pyfos_util
from pyfos.utils import brcd_util


def _create_add_port_trunk_area(session, trunk_object):
    return trunk_object.post(session)


def main(argv):
    """ filters = ["trunk_index", "trunk_members_trunk_member"] """
    filters = ["trunk_index", "trunk_members_trunk_member"]
    inputs = brcd_util.parse(argv, trunk_area, filters)

    fc_object = inputs['utilobject']
    if fc_object.peek_trunk_index() is None:
        print("Missing options in the commandline:")
        print(inputs['utilusage'])
        sys.exit(1)
    session = brcd_util.getsession(inputs)
    print(fc_object.peek_trunk_members_trunk_member())
    result = _create_add_port_trunk_area(session, fc_object)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
