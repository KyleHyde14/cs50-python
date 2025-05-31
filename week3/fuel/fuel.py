def main():
    fraction = input('Fraction: \n')
    
    while True:
        try:
            x, y = fraction.split('/')
            x, y = int(x), int(y)
            if x > y:
                fraction = input('Fraction: \n')
            else: 
                break

        except (ValueError, ZeroDivisionError):
            fraction = input('Fraction: \n')

    percent = round(x/y * 100)

    if percent >= 99:
        return 'F'
    elif percent <= 1:
        return 'E'
    else:
        return f'{percent}%' 


if __name__ == '__main__':
    print(main())