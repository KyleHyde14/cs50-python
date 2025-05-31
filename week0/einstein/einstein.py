def main():
    mass = int(input('Enter the mass to calculate energy: '))
    c = 300000000

    return mass * (c)**2

if __name__ == '__main__':
    print(main())