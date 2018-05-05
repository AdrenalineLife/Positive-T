# coding: utf-8

import time
import paramiko

from exceptions import TransportError, TransportConnectionError


class SSHTransport(paramiko.SSHClient):
    def __init__(self, host=None, port=None, login=None, password=None, **kwargs):
        super().__init__()
        self.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connect(hostname=host,
                     port=port,
                     username=login,
                     password=password)

    def exec(self, command: str, **kwargs):
        stdin, stdout, stderr = self.exec_command(command, **kwargs)
        err = stderr.read().decode()
        stderr.close()
        if err:
            raise TransportError(err)
        resp = stdout.read().decode()
        stdout.close()
        return resp

    def get_file(self, filepath) -> bytes:
        sftp = self.open_sftp()
        try:
            with sftp.open(filepath, 'r') as f:
                result = f.read()
        except IOError as e:
            raise TransportError(str(e), filepath)
        except Exception as e:
            raise TransportConnectionError(str(e), filepath)
        return result


if __name__ == '__main__':
    pass