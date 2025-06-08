from validator_collection import validators

def main():
    try:
        check = validators.email(input('Email: '))
        if check:
            print('Valid')
        else:
            print('Invalid')
    except:
        print('Invalid')


if __name__ == "__main__":
    main()
