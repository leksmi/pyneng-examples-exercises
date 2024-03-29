import ipaddress


class Network:
    all_allocated_ip = []

    def __init__(self, network: str, mask: int):
        self.network = network
        self.mask = mask
        self.allocated = []
        ipv4net = ipaddress.ip_network(f"{self.network}/{self.mask}")
        self.hosts = [str(ip) for ip in ipv4net.hosts()]

    def allocate_ip(self, ip):
        if ip in self.hosts:
            if ip not in self.allocated:
                self.allocated.append(ip)
                # Network.all_allocated_ip.append(ip)
                type(self).all_allocated_ip.append(ip)
            else:
                raise ValueError(
                    f"IP-адрес {ip} уже находится в allocated "
                    f"\n{self.allocated}"
                )
        else:
            raise ValueError(
                f"IP-адрес {ip} не входит в сеть "
                f"{self.network}/{self.mask}"
            )

    def __str__(self):
        print("Вызываю Network __str__")
        return f"{self.network}/{self.mask}"

    def __repr__(self):
        print("Вызываю Network __repr__")
        return f"Network('{self.network}', {self.mask})"

    def __len__(self):
        print("Вызываю Network __len__")
        return len(self.hosts)

    def __getitem__(self, item):
        print(f"Вызываю Network __getitem__ index {item}")
        return self.hosts[item]
