from baseclass_telnet import BaseTelnet


class CiscoTelnet(BaseTelnet):
    """
    Production class to work with Cisco_ios device
    """

    def __init__(self,
                 ip: str,
                 username: str,
                 password: str,
                 enable: str,
                 prompt='#',
                 disable_paging: bool = True,
                 short_sleep: int = 1,
                 long_sleep: int = 5
                 ):
        super().__init__(ip, username, password, prompt, short_sleep=1, long_sleep=5)
        self._enable = enable
        if disable_paging:
            self._read_until_prompt()
            self._telnet.write(self._encode('term length 0'))
            self._read_until_prompt()
            print('\nPaging has disabled.\n')

    def _enter_enable(self):
        self._telnet.write(self._encode('enable'))
        self._telnet.read_until(b'Password')
        self._telnet.write(self._encode(self._enable))
        self._read_until_prompt()


if __name__ == '__main__':
    dev_params = {
        'ip': input('Enter mgmt ip: '),
        'username': 'test',
        'password': 'test',
        'enable': input('Enter enable: ')
    }
    with CiscoTelnet(**dev_params) as conn:
        command = input('\nEnter command: ')
        print(conn.send_command(command=command))
