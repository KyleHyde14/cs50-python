
def main():
    groceries = {}

    while True:
        try:
            item = input('')
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except EOFError:
            break

    sorted_groceries = dict(sorted(groceries.items()))

    output = ''

    for k, v in sorted_groceries.items():
        output += f'{v} {k.upper()}\n'

    return output

if __name__ == '__main__':
    print(main())