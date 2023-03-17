import time
import telnetlib
from rich import print, inspect


class BaseTelnet:
    """
    Base class for connection with telnet protocol.
    It uses by over classes to work with specific device, e.g. Cisco_IOS.
    """

    def __init__(self, ip, username, password, prompt, short_sleep=1, long_sleep=5):
        print('BaseTelnet __init__ works:')
        self.ip = ip
        self.prompt = prompt
        self._login = self._encode(username)
        self._password = self._encode(password)
        self._short_sleep = short_sleep
        self._long_sleep = long_sleep
        # Connect to device with ip, _login, _password
        self._telnet = telnetlib.Telnet(host=ip)
        self._telnet.read_until(b'Username')
        self._telnet.write(self._login)
        self._telnet.read_until(b'Password')
        self._telnet.write(self._password)
        time.sleep(self._short_sleep)
        self._telnet.read_very_eager()

    def send_command(self, command):
        self._telnet.write(self._encode(command))
        time.sleep(self._short_sleep)
        result = self._telnet.read_very_eager().decode('utf-8')
        return result.replace('\r\n', '\n')

    def send_config(self, command):
        self._telnet.write(self._encode(command))
        # time.sleep(self._long_sleep)
        # output = self._telnet.read_very_eager().decode('utf-8')
        output = self._read_until_prompt()
        return output.replace('/r/n', 'n')

    def _read_until_prompt(self):
        """
        Read console output while # does not appear.
        """
        result = self._telnet.read_until(self._encode(self.prompt))
        return result.decode('utf-8')

    @staticmethod
    def _encode(text: str) -> bytes:
        """
        Convert text to byte string
        """
        return text.encode('utf-8') + b'\n'

    def _close(self):
        self._telnet.close()

    def __enter__(self):
        """
        The Class is going to work with context manager.
        """
        print('__enter__ works:')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ works:')
        self._close()
