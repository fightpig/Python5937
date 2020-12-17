

def closure():
    re = list()

    def add(e):
        re.append(e)
        return re

    return add


if __name__ == '__main__':
    c1 = closure()
    c1(1)
    c1(2)
    c1(3)
    print(c1(4))

    c2 = closure()
    c2(2)
    print(c2(5))
