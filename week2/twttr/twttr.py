def main():
    vowels = 'aeiou'
    sentence = input('Enter your tweet: \n')
    output = str(sentence)
    
    for i in sentence:
        if i.lower() in vowels:
            output = output.replace(i, '')

    return output

if __name__ == '__main__':
    print(main())
