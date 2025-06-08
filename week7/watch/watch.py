import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r'src="(http|https)://(www\.)?youtube\.com/embed/\w+"'
    regex_2 = r'youtube\.com/embed/\w+'

    if not s.startswith('<iframe ') or not s.endswith('></iframe>'):
        return None

    try:
        source = re.search(regex, s)[0]
        link = source.split('=')[-1].strip('"')
    except: 
        return None

    embeded_link = re.search(regex_2, link)[0].replace('youtube.com/embed', 'youtu.be')
    
    return f'https://{embeded_link}'

    


if __name__ == "__main__":
    main()
