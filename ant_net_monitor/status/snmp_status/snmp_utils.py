from pysnmp.hlapi import *


def get_snmp_value(host, community, mib_module, mib_object):
    """Using `pysnmp.getCmd()` like `SNMPGET` to get the value of a SNMP object.

    Args:
        host (str): snmp host address
        community (str): snmp community
        mib_module (str): snmp mib module
        mib_object (str): name of the mib object

    Returns:
        value: snmp value
    """
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=1),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(mib_module, mib_object, 0)),
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print(
            "%s at %s"
            % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
            )
        )
    else:
        for varBind in varBinds:
            return varBind[1]
