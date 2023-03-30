import subprocess
from class_network import Network  # класс созданного ранее модуля
from concurrent.futures import ThreadPoolExecutor


class NetworkScanner:
    """
    Проверка доступности IP адресов
    """

    def __init__(self, network: Network):
        self.network = network

    def _ping_ip(self, ip: str) -> bool:
        """
        Проверка ping доступности адреса
        Args:
            ip: str

        Returns: bool

        """
        result = subprocess.run(f'ping -c 3 {ip}'.split(),
                                stdout=subprocess.PIPE)
        return True if not result.returncode else False

    def scan(self, max_workers=10):
        success, not_success = [], []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            result = executor.map(self._ping_ip, self.network)
            for ip, status in zip(self.network, result):
                success.append(ip) if status else not_success.append(ip)
        return success, not_success


if __name__ == '__main__':
    net1: Network = Network('192.168.10.0', 28)
    scanner: NetworkScanner = NetworkScanner(net1)
    success, no_success = scanner.scan()
    print(f'{success=}\n{no_success=}')
