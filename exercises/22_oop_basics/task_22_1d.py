# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Соединение с одним из портов существует"


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

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Соединение с одним из портов существует


"""

import copy
from pprint import pprint


class Topology:
    """
    To do different manipulates with network topology
    """
    def __init__(self, raw_topology: dict) -> None:
        """
        :param raw_topology: network topology with doubles
        :type  raw_topology: dict
        """
        self.raw_topology = raw_topology
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
            print(f"It is going to be deleted: {link_a} <-> {self.topology[link_a]}")
            del self.topology[link_a]
        elif self.topology.get(link_b) == link_a:
            print(f"It is going to be deleted: {link_b} <-> {self.topology[link_b]}")
            del self.topology[link_b]
        else:
            print(f"There are no links with: {link_a} <-> {link_b} and vice versa.")

    def delete_node(self, dev_name: str) -> None:
        """
        Delete all items for a particular device
        :param dev_name: Node to be deleted
        :type  dev_name: str
        :returns: None
        """
        garbage_keys = []
        for key, value in self.topology.items():
            if dev_name in key or dev_name in value:
                garbage_keys.append(key)
        if garbage_keys:
            for key in garbage_keys:
                del self.topology[key]
        else:
            print(f"\nThere is no device {dev_name} here.")
    
    def add_link(self, new_link_1: tuple, new_link_2: tuple) -> None:
        """
        Добавляет указанное соединение, если его нет в топологии.
        Если соединение существует, вывести сообщение "Такое соединение существует",
        Если одна из сторон есть в топологии, вывести 
        сообщение "Соединение с одним из портов существует"
        :param new_link_1: The first link of the new connection
        :type  new_link_1: tuple
        :param new_link_2: The responding link of the new connection
        :type  new_link_2: tuple
        :returns: None
        """
        if (self.topology.get(new_link_1) == new_link_2 or 
            self.topology.get(new_link_2) == new_link_1):
            print(f'\nThere is a connection {new_link_1} <-> {new_link_2}\nNothing to change.')
        
        elif (self.topology.get(new_link_1) or self.topology.get(new_link_2)):
            print(f'\nThere is a connection with those links: {new_link_1}, {new_link_2}')
        else:
            self.topology[new_link_1] = new_link_2
        


# check working:
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
print('\n'*2)
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
pprint(t.topology)
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
