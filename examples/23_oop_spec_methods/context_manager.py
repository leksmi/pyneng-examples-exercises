# Методы __enter__ и __exit__ в классе указывают, что можно использовать менеджер контекста.
# Работают только в паре.
# Преимущество: __exit__ отработает даже если возникло исключение, тогда код завершит открытые сессии.
# Добавим в ранее созданный класс CiscoTelnet эти методы:

import telnetlib
import time


class CiscoTelnet:
    """
    Подключение к циско по телнет
    """

    def __init__(self, ip, username, password, enable, disable_paging=True):
        """
        Инициализация экземпляра: создание атрибутов экземпляра
        """
        print('__init__ works:')
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b'Username:')
        self.telnet.write(username.encode('utf-8') + b'\n')
        self.telnet.read_until(b'Password:')
        self.telnet.write(password.encode('utf-8') + b'\n')
        self.telnet.write(b'enable\n')
        self.telnet.read_until(b'Password:')
        self.telnet.write(enable.encode('utf-8') + b'\n')
        if disable_paging: self.telnet.write(b'terminal length 0\n')
        time.sleep(1)
        self.telnet.read_very_eager()

    def send_show_command(self, command):
        """
        Отправка команд show
        """
        self.telnet.write(command.encode('utf-8') + b'\n')
        time.sleep(2)
        command_output = self.telnet.read_very_eager().decode('utf-8')
        return command_output

    def close(self):
        self.telnet.close()

    # добавим методы для реализации менеджера контекста:
    def __enter__(self):
        print('__enter__ works:')
        return self  # возвращает сам экземпляр, он и присваивается через "as" в переменную

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ works:')
        self.close()  # закрытие выполнится даже в случае Traceback


if __name__ == '__main__':
    with CiscoTelnet(ip='10.10.10.1', username='test', password='test', enable='test') as conn:
        conn.send_show_command('sh clock')

