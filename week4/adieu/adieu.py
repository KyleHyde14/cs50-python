import inflect

def main():
    p = inflect.engine()
    names = []
    adieu = 'Adieu, adieu, to '
    while True:
        try:
            new_name = input('Name: \n')
            names.append(new_name)
        except EOFError:
            break

    return adieu + p.join(names)
    
if __name__ == '__main__':
    print(main())
