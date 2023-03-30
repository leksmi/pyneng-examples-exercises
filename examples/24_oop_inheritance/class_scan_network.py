import subprocess
from class_network import Network  #  класс созданного ранее модуля
from concurrent.futures import ThreadPoolExecutor

class NetworkScanner:
    """
    Аргументом принимает объект импортированного класса Network
    """
    def __init__(self, network: Network):
        self.network = network


if __name__ == '__main__':
    net: Network = Network()