from tabulate import tabulate
import csv
import sys

def main():
    args = sys.argv

    if len(args) != 2:
        sys.exit('Expected exactly 1 command-line argument')
    elif args[1][-4:] != '.csv':
        sys.exit('Must provide a csv file')

    try:
        table = create_table(args[1])
    except FileNotFoundError:
        sys.exit('File not found')

    print(table)

def create_table(file):
    arr = []
    try:
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                arr.append(row)
    except FileNotFoundError:
        raise FileNotFoundError
    
    table = tabulate(arr, headers='firstrow', tablefmt='grid')

    return table


if __name__ == '__main__':
    main()
