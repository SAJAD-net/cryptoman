#!/usr/env python3


LOOKUP = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D':'aaabb',
          'E': 'aabaa', 'F': 'aabab', 'G': 'aabba','H': 'aabbb',
          'I': 'abaaa', 'J': 'abaab', 'K': 'ababa', 'L': 'ababb',
          'M': 'abbaa', 'N': 'abbab', 'O': 'abbba', 'P': 'abbbb',
          'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
          'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb',
          'Y': 'bbaaa', 'Z': 'bbaab'}


def encrypt(plain_text):
    cipher_text = ""

    for ch in plain_text:
        if ch == " ":
            cipher_text += " "
            continue

        cipher_text += LOOKUP[ch]

    return cipher_text


def decrypt(cipher_text):
    plain_text = ""
    i = 0

    while True:
        if i < len(cipher_text)-4:
            substr = cipher_text[i:i+5]
            if substr[0] == " ":
                plain_text += " "
                i += 1
                continue

            plain_text += list(LOOKUP.keys())[list(LOOKUP.values()).index(substr)]
            i += 5

        else:
            break

    return plain_text


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Baconian Cipher")
    parser.add_argument("-e", "--encrypt", help="To encrypt")
    parser.add_argument("-d", "--decrypt", help="To decrypt")

    args = parser.parse_args()

    if args.encrypt:
        result = encrypt(args.encrypt.upper())
        print(result)

    elif args.decrypt:
        result = decrypt(args.decrypt.lower())
        print(result)

    else:
        parser.print_help()
