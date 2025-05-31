def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")

    return sentence

def main():
    original = input('Hi! can you put a sentence usign an emoji? Only :) and :( for now \n')
    converted = convert(original)

    return converted

if __name__ == '__main__':
    print(main())
    