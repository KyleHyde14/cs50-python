import csv
import sys

def main():
    args = sys.argv

    if len(args) != 3:
        sys.exit('Expected 2 command-line arguments')
    
    if any(x[-4:] != '.csv' for x in args[1:]):
        sys.exit('Both files must be csv')
    try:
        arr = clean_data(args[1])
        write_data(args[2],  arr)
    except FileNotFoundError:
        sys.exit(f'Could not read {args[1]}')

    return
    

def clean_data(file):
    dics = []
    try:
        with open(file, newline='') as fhand:
            reader = csv.DictReader(fhand)
            for line in reader:
                cleaned_line = {}
                cleaned_line['first'] = line['name'].split(',')[1].strip()
                cleaned_line['last'] = line['name'].split(',')[0].strip()
                cleaned_line['house'] = line['house'].strip()
                dics.append(cleaned_line)

    except FileNotFoundError:
        raise FileNotFoundError
    
    return dics

def write_data(file, arr):
    with open(file, 'w', newline='') as fhand:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(fhand, fieldnames=fieldnames)

        writer.writeheader()
        for line in arr:
            writer.writerow(line)

if __name__ == "__main__":
    main()