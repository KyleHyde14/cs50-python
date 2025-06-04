def main():
    fraction = input('Fraction: \n')
    
    while True:
        try:
            percent = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            fraction = input('Fraction: \n')
    
    print(gauge(percent))


def convert(fraction):
    try:
        x, y = fraction.split('/')
        x, y = int(x), int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        elif x < 0 or y < 0:
            raise ValueError

    except ValueError:
        raise ValueError
    
    return round(x/y * 100)


def gauge(percentage):

    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return f'{percentage}%' 


if __name__ == "__main__":
    main()