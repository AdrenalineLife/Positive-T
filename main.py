# coding: utf-8

import time
import sys
import os
import random
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('here')
client.connect(hostname='192.168.99.100', port=22022, username='root', password='pwd')
print('here 2')

def f():
    pass


if __name__ == '__main__':
    pass