def main():
    greeting = input('Greeting: ').strip()

    print(f'${value(greeting)}')
    return ''

def value(greeting):

    if greeting.lower().startswith('hello'):
        return 0
    elif greeting.lower().startswith('h'):
        return 20
    
    return 100


if __name__ == "__main__":
    main()