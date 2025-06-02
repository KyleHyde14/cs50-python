import emoji

def main():
    string = input('Input: \n')

    parts = string.split(' ')
    for i in range(len(parts)):
        parts[i] = emoji.emojize(parts[i], language='alias')

    output = ' '.join(parts)

    return f'Output: {output}'

if __name__ == '__main__':
    print(main())
