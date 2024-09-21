from . import YubiKeyTest
from json import dumps


while True:
    yb = YubiKeyTest()

    yb.get_input()
    print(yb.split_input())

    print(dumps(yb.auth(), indent=2))
