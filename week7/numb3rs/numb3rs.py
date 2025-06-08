import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = r'\d'

    try:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        if all(re.search(regex, x) for x in parts):
            if all( 0 <= int(x) <= 255 for x in parts):
                return True
    except:
        return False

        
    return False


if __name__ == "__main__":
    main()