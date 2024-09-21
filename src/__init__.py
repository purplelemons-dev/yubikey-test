from random import getrandbits as grb
from requests import get
from hashlib import sha1


class YubiKeyTest:

    def __init__(self) -> None:
        self.auth_servers = {"", "2", "3", "4", "5"}

    def get_input(self):
        i = input("> ").lower()
        assert (32 <= len(i) <= 48) and all(
            (ord(char) in range(97, 123)) or (char == ".") for char in i
        ), "Invalid input"
        self.input = i
        return self.input

    def split_input(self):
        self.otp = self.input[-32:]
        self.identity = self.input[: -len(self.otp)]
        return self.identity, self.otp

    @staticmethod
    def int_to_bytes(n: int) -> bytes:
        return n.to_bytes((n.bit_length() + 7) // 8, "big")

    def auth(self):
        nonce = sha1(self.int_to_bytes(grb(160))).hexdigest()
        responses = {}
        id = grb(16)
        otp = self.input
        for server in self.auth_servers:
            r = get(
                f"https://api{server}.yubico.com/wsapi/2.0/verify?{id=}&{otp=}&{nonce=}"
            )
            responses[server] = r.text
        return responses
