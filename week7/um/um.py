import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    sentence = s.lower()
    regex = r'\b(\W)?um(\W)?\b'

    counted = re.findall(regex, sentence)

    return len(counted)


if __name__ == "__main__":
    main()
