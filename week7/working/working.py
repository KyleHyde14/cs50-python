import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit('ValueError')
        


def convert(s): 
    if not validate_input(s):
        raise ValueError
    
    hours = s.split('to')
    start = hours[0].strip().split()
    end = hours[1].strip().split()
    
    if 'PM' in start:
        time = start[0].split(':')
        if len(time) < 2:
            h, m = time[0], '00'
        else:
            h, m = time

        PM = int(h) + 12
        if PM == 24:
            PM = 12
        start[0] = f'{PM:02d}:{m}'
    else:
        time = end[0].split(':')
        if len(time) < 2:
            h, m = time[0], '00'
        else:
            h, m = time
        PM = int(h) + 12
        if PM == 24:
            PM = 12
        end[0] = f'{PM:02d}:{m}'

    if 'AM' in start:
        time = start[0].split(':')
        if len(time) < 2:
            h, m = time[0], '00'
        else:
            h, m = time
        
        if h == '12':
            h = '00'
        
        start[0] = f'{int(h):02d}:{m}'
    else:
        time = end[0].split(':')
        if len(time) < 2:
            h, m = time[0], '00'
        else:
            h, m = time
        
        if h == '12':
            h = '00'
        
        end[0] = f'{int(h):02d}:{m}'

    return f'{start[0]} to {end[0]}'

        


    

    


def validate_input(s):
    regex = r'\b(?:1[0-2]|[1-9])(?::[0-5][0-9])?\b'

    parts = s.split(' ')
    if len(parts) != 5:
        return False
    if not ('AM' in parts and parts[2] == 'to' and 'PM' in parts):
        return False
    if not re.fullmatch(regex, parts[0]) or not re.fullmatch(regex, parts[3]):
        return False
    
    return True


if __name__ == "__main__":
    main()