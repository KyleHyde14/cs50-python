def main():
    correct = ['42', 'forty-two', 'forty two']

    answer = input("What is the answer to life, the universe, and everything? ").strip()
    if answer.lower() in correct:
        return 'yes'
    return 'no'

if __name__ == '__main__':
    print(main())
