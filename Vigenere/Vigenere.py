#!/usr/env python3


ALPHA = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plain_text, key):
    cipher_text = ""

    for ch in plain_text.lower():
        ind = key[plain_text.index(ch) % len(key)]
        shift = ALPHA.index(ind)
        cipher_text += ALPHA[(ALPHA.index(ch) + shift) % 26]

    print(cipher_text)


def decrypt(cipher_text, key):
    plain_text = ""

    for ch in cipher_text.lower():
        ind = key[cipher_text.index(ch) % len(key)]
        shift = ALPHA.index(ind)
        plain_text += ALPHA[(ALPHA.index(ch) - shift) % 26]

    print(plain_text)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description = "Vigenere encryption and decryption.")
    parser.add_argument('-e', '--encrypt', help = "To encrypt")
    parser.add_argument('-d', '--decrypt', help = "To decrypt")
    parser.add_argument('-k', '--key', help = "Key")

    args = parser.parse_args()

    if key:=args.key:
        if plain_text:=args.encrypt:
            encrypt(plain_text, key)

        elif cipher_text:=args.decrypt:
            decrypt(cipher_text, key)

        else:
            parser.print_help()
    else:
        parser.print_help()
