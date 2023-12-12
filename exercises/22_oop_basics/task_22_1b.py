# -*- coding: utf-8 -*-

"""
Задание 22.1b

Изменить класс Topology из задания 22.1a или 22.1.

Добавить метод delete_link, который удаляет указанное соединение.
Метод должен удалять и "обратное" соединение, если оно есть (ниже пример).

Если такого соединения нет, выводится сообщение "Такого соединения нет".

Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление линка:
In [9]: t.delete_link(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление "обратного" линка:
в словаре есть запись ``('R3', 'Eth0/2'): ('R5', 'Eth0/0')``, но вызов delete_link
с указанием ключа и значения в обратном порядке, должно удалять соединение:

In [11]: t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))

In [12]: t.topology
Out[12]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3')}

Если такого соединения нет, выводится сообщение:
In [13]: t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
Такого соединения нет

"""

import copy
from pprint import pprint


class Topology:
    """
    :param: raw_topology network topology with doubles
    """

    def __init__(self, raw_topology: dict) -> None:
        self.topology: dict = self._normalize(raw_topology)

    def _normalize(self, in_topology: dict) -> dict:
        """
        Delete doubles
        """
        cleared_topology = copy.deepcopy(in_topology)
        for key in in_topology:
            if key in cleared_topology.values():
                del cleared_topology[key]
        return cleared_topology

    def delete_link(self, link_a: tuple, link_b: tuple) -> None:
        """
        Delete links from self.topology
        """
        # for key, value in self.topology.items():
            # print(f"Key: {key} Value: {value}")
        # print(f'Looking for: {link_a}: {self.topology.get(link_a)}')
        # print(f'Looking for: {link_b}: {self.topology.get(link_b)}')
        if self.topology.get(link_a) == link_b:
            print(f'It is going to be deleted: {link_a} <-> {self.topology[link_a]}')
            del self.topology[link_a]
        elif self.topology.get(link_b) == link_a:
            print(f'It is going to be deleted: {link_b} <-> {self.topology[link_b]}')
            del self.topology[link_b]
        else:
            print(f'There are no links with: {link_a} <-> {link_b} and vice versa.')




topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

t = Topology(topology_example)
pprint(t.topology)
print('\n')
t.delete_link(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
print('\nNow:')
pprint(t.topology)
t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
print('\nNow:')
pprint(t.topology)
t.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
print('\nNow:')
pprint(t.topology)
