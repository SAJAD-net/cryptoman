#!/usr/env python3


ALPHA = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plain_text, shift):
    cipher_text = ""

    for ch in plain_text.lower():
        if ch not in ALPHA:
            cipher_text += ch
            continue

        cipher_text += ALPHA[(ALPHA.index(ch) + shift) % 26]

    print(cipher_text)


def decrypt(cipher_text, shift):
    plain_text = ""

    for ch in cipher_text:
        if ch not in ALPHA:
            plain_text += ch
            continue

        plain_text += ALPHA[(ALPHA.index(ch) - shift) % 26]

    print(plain_text)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description = "Ceaser Cipher")
    parser.add_argument('-e', '--encrypt', help = "To encrypt")
    parser.add_argument('-d', '--decrypt', help = "To decrypt")
    parser.add_argument('-s', '--shift', type = int, help = "The length to shift")

    args = parser.parse_args()

    if shift:=args.shift:
        if plain_text:=args.encrypt:
            encrypt(plain_text, shift)

        elif cipher_text:=args.decrypt:
            decrypt(cipher_text, shift)

        else:
            parser.print_help()
    else:
        parser.print_help()
