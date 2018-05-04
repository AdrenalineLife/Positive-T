# coding: utf-8

import time
import paramiko


class SSHTransport(paramiko.SSHClient):
    def __init__(self, host=None, port=None, login=None, password=None, **kwargs):
        super().__init__()
        self.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connect(hostname=host,
                     port=port,
                     username=login,
                     password=password)

    def eval_command(self):
        pass

    def get_file(self, path):
        pass



if __name__ == '__main__':
    pass