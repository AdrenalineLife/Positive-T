# coding: utf-8

import pytest

from exceptions import TransportError, TransportConnectionError
from main import get_transport, get_config


def test_get_config():
    get_config()

def test_get_transport():
    tr = get_transport('SSH')
    tr.close()

ssh = get_transport('SSH')

def test_command_cat():
    assert ssh.exec('cat ../etc/lsb-release').startswith('DISTRIB_ID=')

def test_get_file_decoding():
    assert ssh.get_file('../etc/lsb-release').decode() == ssh.exec('cat ../etc/lsb-release')

def test_invalid_command():
    with pytest.raises(TransportError):
        ssh.exec('asdff')

def test_no_such_file():
    with pytest.raises(TransportError):
        ssh.get_file('../etc/LSB-')