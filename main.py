# coding: utf-8

import time
import sys
import json

from transports.ssh_transport import SSHTransport
from transports.mysql_transport import MySqlTransport
from exceptions import *


# a dict to map transport name to its class
transp_classes = {  # all keys are uppercase
    'SSH': SSHTransport,
    'MYSQL': MySqlTransport
}
_CONFIG = None

def get_config() -> dict:
    global _CONFIG
    if _CONFIG is not None:
        return _CONFIG
    else:
        with open('env.json', 'rt', encoding='utf-8') as f:
            _CONFIG = json.load(f)
            return _CONFIG


def get_transport(name: str, **kwargs):
    glob_config = get_config()
    transp_conf = glob_config['transports'].get(name, None)
    if transp_conf is None:
        raise UnknownTransportError('"{}" transport was not found in config file'.format(name))

    conf = dict(host=glob_config['host'])
    conf.update(transp_conf)
    conf.update(**kwargs)
    transport = transp_classes.get(name, None)
    if transport is None:
        raise UnknownTransportError('Can not find a class for "{}" transport'.format(name))
    return transport(**conf)


def main_func():
    ssh_client = get_transport('SSH')
    a = ssh_client.exec('cat ../etc/lsb-release')
    b = ssh_client.get_file('../etc/lsb-release')
    print(a==b)


if __name__ == '__main__':
    main_func()
    #print(get_config())