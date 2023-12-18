# -*- coding: utf-8 -*-

"""
Задание 22.1c

Изменить класс Topology из задания 22.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

"""


import copy
from pprint import pprint


class Topology:
    """
    :param: raw_topology network topology with doubles
    """

    def __init__(self, raw_topology: dict) -> None:
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
        :return: None
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
print("\n" * 2)
t.delete_node("SW1")
pprint(t.topology)
t.delete_node("SW1")
