def main():
    fraction = input('Fraction: \n')
    
    while True:
        try:
            x, y = fraction.split('/')
            x, y = int(x), int(y)

            percent = round(x/y * 100)

            if x > y:
                fraction = input('Fraction: \n')
                continue

            if percent >= 99:
                return 'F'
            elif percent <= 1:
                return 'E'
            else:
                return f'{percent}%' 
        except (ValueError, ZeroDivisionError):
            fraction = input('Fraction: \n')


if __name__ == '__main__':
    print(main())