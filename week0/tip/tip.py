def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = float(d[1:])

    return dollars


def percent_to_float(p):
    number = int(p[:-1])
    percentage = float(number/100)

    return percentage

if __name__ ==  '__main__':
    main()