def main():
    time = input('Enter current time: \n')

    decimal = convert(time)

    if (7 <= decimal <= 8):
        return 'breakfast time'
    elif (12 <= decimal <= 13):
        return 'lunch time'
    elif (18 <= decimal <= 19):
        return 'dinner time'
    
    return ''

def convert(time):
    hour, minute = time.split(':')
    hour, minute = float(hour), float(minute)

    return hour + minute / 60



if __name__ == "__main__":
    print(main())
