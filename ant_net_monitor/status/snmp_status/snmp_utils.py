from time import sleep

from pysnmp.hlapi import *


def snmp_get_value(host, community, mib_module, mib_object):
    """Using `pysnmp.getCmd()` like `SNMPGET` to get the value of a SNMP object.

    Args:
        host (str): snmp host address
        community (str): snmp community
        mib_module (str): snmp mib module
        mib_object (str): name of the mib object

    Returns:
        int: snmp value
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
            return int(varBind[1])


def snmp_walk(host, community, mib_module, mib_object):
    """Using `pysnmp.nextCmd()` like `SNMPWALK`

    Args:
        host (str): snmp host address
        community (str): snmp community
        mib_module (str): snmp mib module
        mib_object (str): name of the mib object

    Yields:
        int: value of snmp object
    """
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=1),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(mib_module, mib_object)),
        lexicographicMode=False,
    ):
        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print(
                "%s at %s"
                % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
                )
            )
            break
        else:
            for varBind in varBinds:
                yield int(varBind[1])


if __name__ == "__main__":
    #while True:
    #    print(
    #        snmp_get_value("localhost", "antrol", "UCD-SNMP-MIB", "memCached")
    #        / 1024**2
    #    )
    #    sleep(1)

    #a = snmp_get_value("localhost", "antrol", "UCD-DISKIO-MIB", "diskIONRead") / 1024**2
    #sleep(1)
    #while True:
    #    b = snmp_get_value("localhost", "antrol", "UCD-DISKIO-MIB", "diskIONRead") / 1024**2
    #    print(b - a)
    #    a = b
    #    sleep(1)


    a = sum([value for value in snmp_walk("localhost", "antrol", "UCD-DISKIO-MIB", "diskIONRead")]) / 1024**2
    sleep(1)
    while True:
        b = sum([value for value in snmp_walk("localhost", "antrol", "UCD-DISKIO-MIB", "diskIONRead")]) / 1024**2
        print(b - a)
        a = b
        sleep(1)
