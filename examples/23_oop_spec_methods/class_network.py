import ipaddress
from rich import print, inspect
from operator import add


class Network:
    def __init__(self, net: str, mask: int):
        self.net = net
        self.mask = mask
        ipv4net = ipaddress.ip_network(f'{self.net}/{self.mask}')
        self.hosts: list = [str(ip) for ip in ipv4net.hosts()]

    def __str__(self):
        return f'{self.net}/{self.mask}'

    def __repr__(self):
        return f"Network({self.net}, {self.mask})"

    def __len__(self):
        return len(self.hosts)

    def __getitem__(self, item):
        """
        Позволяет обращаться к списку по индексу.
        Без этого метода нет возможности брать элементы списка и выполнять срезы, перебирать в for.
        Этот дандер нужно делать для всех классов, где есть элементы последовательности.
        """
        print('__getitem__ works ..')
        return self.hosts[item]

    def __iter__(self):
        """
        Отвечает за создание итератора.
        Т.е. позволяет обработать объект данного класса,
        и получить новый объект-итератор.
        Для создания используется функция iter()
        """
        print('__iter__ works ..')
        return iter(self.hosts)  # возвращает объект-итератор


# Итерируемый объект конечен по количеству элементов.
# Итератор может генерировать значения бесконечно.
class Repeat:
    def __init__(self, value):
        self.value = value

    def __next__(self):
        """
        Итератор - это объект, который содержит метод __next__
        """
        return self.value  # бесконечно выдает значение value

    def __iter__(self):
        return self


class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self._last = start

    def __next__(self):
        print('__next__ works ..')
        value = self._last
        if value == self.stop:
            raise StopIteration
        self._last += 1
        return value

    def __iter__(self):  # добавлен так как положено
        return self


if __name__ == '__main__':
    net1 = Network('10.1.1.0', 29)
    # print(net1)
    # print(net1.hosts)
    # print(dir(net1))
    # print(net1[0])  # требует наличия __getitem__ в классе
    # for ip in net1:
    #     print(f'{ip=}')
    #
    rep1 = Repeat(101)
    print(type(rep1))
    print(next(rep1))
    print(next(rep1))
    print(list(zip([1, 2, 3], Repeat(111), Repeat(222))))
    print(list(map(add, list(range(1, 7)), Repeat(10))))
