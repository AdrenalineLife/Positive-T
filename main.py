# coding: utf-8

import time
import sys
import json
import paramiko

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
        raise UnknownTransport

    conf = dict(host=glob_config['host'])
    conf.update(transp_conf)
    conf.update(**kwargs)
    transport = transp_classes.get(name, None)
    if transport is None:
        raise UnknownTransport
    return transport(**conf)


def main_func():
    print(get_transport('SSD'))


if __name__ == '__main__':
    main_func()
    #print(get_config())