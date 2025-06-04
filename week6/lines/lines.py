import sys

def main():
    args = sys.argv
    
    if len(args) != 2:
        sys.exit('Only 1 command-line argument is accepted')    
    elif args[1][-3:] != '.py':
        sys.exit('Not a python file')

    try:
        line_count = count_lines(args[1])
    except FileNotFoundError:
        sys.exit('File does not exist')

    print(line_count)


def count_lines(file):
    count = 0

    try:
        with open(file, 'r') as fhand:
            for line in fhand:
                if line.lstrip().startswith('#'):
                    continue
                elif len(line.strip()) == 0:
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        raise FileNotFoundError

    return count

if __name__ == '__main__':
    main()
