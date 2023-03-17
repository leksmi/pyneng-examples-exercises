from baseclass_telnet import BaseTelnet


class CiscoTelnet(BaseTelnet):
    """
    Production class to work with Cisco_ios device
    """

    def __init__(self,
                 ip,
                 username,
                 password,
                 enable,
                 prompt='#',
                 short_sleep=1,
                 long_sleep=5
                 ):
        super().__init__(ip, username, password, prompt, short_sleep=1, long_sleep=5)
        self._enable = enable

    def _enter_enable(self):
        self._telnet.write(self._encode('enable'))
        self._telnet.read_until(b'Password')
        self._telnet.write(self._encode(self._enable))
        self._read_until_prompt()
