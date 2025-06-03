def main():
    sentence = input('Sentence to shorten: \n')
    parts = [shorten(x) for x in sentence.split(' ')]

    print(' '.join(parts))
    return ''


def shorten(word):
    vowels = 'aeiou'
    output = str(word)

    for i in word:
        if i.lower() in vowels:
            output = output.replace(i, '')

    return output




if __name__ == "__main__":
    print(main())