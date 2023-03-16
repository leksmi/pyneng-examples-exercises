# Методы __enter__ и __exit__ в классе указывают, что можно использовать менеджер контекста.
# Работают только в паре.
# Преимущество: __exit__ отработает даже если возникло исключение, тогда код завершит открытые сессии.
# Добавим в ранее созданный класс CiscoTelnet эти методы:

import time
import telnetlib
from netmiko import ConnectHandler


class CiscoTelnet:
    """
    Подключение к Cisco по telnet,
    С использованием менеджера контекста:
    """

    def __init__(self, ip, username, password, enable, disable_paging=True):
        """
        Инициализация экземпляра: создание атрибутов экземпляра.
        Выполнение входа на устройство, вход в режим enable.
        """
        print('__init__ works:')
        self._login = self._encoder(username)
        self._password = self._encoder(password)
        self._enable = self._encoder(enable)
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b'Username:')
        self.telnet.write(self._login)
        self.telnet.read_until(b'Password:')
        self.telnet.write(self._password)
        self.telnet.write(b'enable\n')
        self.telnet.read_until(b'Password:')
        self.telnet.write(self._enable)
        if disable_paging:
            self.telnet.write(b'terminal length 0\n')
        time.sleep(1)
        self.telnet.read_very_eager()

    @staticmethod
    def _encoder(text: str):
        """
        Сервисная вспомогательная функция, не привязывается к объектам Класса:
        Нет ссылок "self" или "cls".
        Можно вызвать как у самого класса, так и объектов Класса.
        """
        return text.encode('utf-8') + b'\n'

    def send_show_command(self, command):
        """
        Отправка команд show
        """
        self.telnet.write(self._encoder(command))
        time.sleep(2)
        command_output = self.telnet.read_very_eager().decode('utf-8')
        return command_output

    def close(self):
        self.telnet.close()

    # добавим методы для реализации менеджера контекста:
    def __enter__(self):
        print('__enter__ works:')
        return self  # возвращает сам экземпляр, он и присваивается через "as" в переменную после as.

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ works:')
        self.close()  # выполнится даже в случае Traceback, при этом исключение следует после работы __exit__


class TotalTime:
    """
    Менеджер контекста для,
    расчета времени выполнения кода выполняющегося внутри менеджера контекста
    """

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        print(f'\nTotal execution time: {round(self.stop - self.start, 2)}')


if __name__ == '__main__':
    # with CiscoTelnet(ip='10.10.10.1', username='test', password='test', enable='test') as conn:
    #     commands = ('show clock', 'show invent', 'show cdp neigh')
    #     for command in commands:
    #         print(conn.send_show_command(command))
    #
    with TotalTime():
        # Нет конструкции "as variable" так как не было инициализатора и нет действий с атрибутами.
        time.sleep(3)  # тело менеджера контекста

    sw_params = {'device_type': 'cisco_ios_telnet',
                 'host': '10.252.135.34',
                 'username': 'test',
                 'password': 'test',
                 'secret': 'test'
                 }
    with TotalTime():
        # внутри менеджера контекста можно запустить другой менеджер контекста:
        with ConnectHandler(**sw_params) as conn:
            print(conn.send_command('show clock'))
