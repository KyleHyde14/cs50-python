def main():
    expression = input('Enter a math expression: \n')

    x, y, z = expression.split()
    x, z = int(x), int(z)

    if y == '+':
        result = float(x + z)
    elif y == '-':
        result = float(x - z)
    elif y == '*':
        result = float(x * z)
    elif y == '/':
        result = float(x / z)
    
    return result

if __name__ == '__main__':
    print(main())
