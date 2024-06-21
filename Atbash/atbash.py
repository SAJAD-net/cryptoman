#!/usr/env python3


ALPHA = "abcdefghijklmnopqrstuvwxyz"


def atbash(text):
    output = ""

    for ch in text:
        if ch.lower() not in ALPHA:
            output += ch
            continue

        nch = ALPHA[-(ALPHA.index(ch.lower())+1)]
        output += nch.upper() if ch.isupper() else nch

    return output


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Atbas encryption and decryption")
    parser.add_argument("-t", "--text", help="To encrypt/decrypt")

    args = parser.parse_args()

    if text := args.text:
        output = atbash(text)
        print(output)

    else:
        parser.print_help()
