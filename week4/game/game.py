import random

def main():
    while True:
        try:
            n = int(input('Level: \n'))
            if n <= 0:
                continue

            ans = random.randint(1, n)
            break
                
        except ValueError:
            continue

    while True:
        try:
            guess = int(input('Guess: \n'))
            if guess <= 0:
                continue

            if guess == ans:
                print('Just right!')
                return ''
            elif guess < ans:
                print('Too small!')
                continue
            else:
                print('Too large!')
                continue
        except ValueError:
            continue
            

if __name__ == '__main__':
    print(main())
