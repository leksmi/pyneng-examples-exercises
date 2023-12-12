# -*- coding: utf-8 -*-

"""
Задание 22.1a

Скопировать класс Topology из задания 22.1 и изменить его.

Перенести функциональность удаления "дублей" в метод _normalize.
При этом метод __init__ должен выглядеть таким образом:
"""

import copy
from pprint import pprint


class Topology:
    """
    :param: raw_topology network topology with doubles
    """

    def __init__(self, raw_topology: dict) -> None:
        self.topology = self._normalize(raw_topology)

    def _normalize(self, in_topology: dict):
        """
        Delete doubles
        """
        cleared_topology = copy.deepcopy(in_topology)
        for key in in_topology:
            if key in cleared_topology.values():
                del cleared_topology[key]
        return cleared_topology


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

top = Topology(topology_example)
pprint(top.topology)
