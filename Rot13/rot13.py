#!/usr/env python3


ALPHA = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plain_text):
    cipher_text = ""

    for ch in plain_text:
        if ch.lower() not in ALPHA:
            cipher_text += ch
            continue

        nch = ALPHA[(ALPHA.index(ch.lower())+13) % 26]
        cipher_text += nch.upper() if ch.isupper() else nch

    return cipher_text


def decrypt(cipher_text):
    plain_text = ""

    for ch in cipher_text:
        if ch.lower() not in ALPHA:
            plain_text += ch
            continue

        nch = ALPHA[(ALPHA.index(ch.lower())-13) % 26]
        plain_text += nch.upper() if ch.isupper() else nch

    return plain_text


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Rot13 encryption and decryption")
    parser.add_argument("-e", "--encrypt", help="To encrypt")
    parser.add_argument("-d", "--decrypt", help="To decrypt")

    args = parser.parse_args()

    if plain_text := args.encrypt:
        cipher_text = encrypt(plain_text)
        print(cipher_text)

    elif cipher_text := args.decrypt:
        plain_text = decrypt(cipher_text)
        print(plain_text)

    else:
        parser.print_help()
