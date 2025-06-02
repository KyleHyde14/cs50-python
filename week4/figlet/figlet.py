import sys
import random 
from pyfiglet import Figlet

def main():
    args = sys.argv[1:]
    figlet = Figlet()
    valid_fonts = figlet.getFonts()

    if len(args) == 0:
        text = input('Input: \n')
        font = random.choice(valid_fonts)
        figlet.setFont(font=font)
        return figlet.renderText(text)
    
    elif len(args) == 2:
        if args[0] != '-f' and args[0] != '--font':
            sys.exit('Invalid usage')
        if args[1] not in valid_fonts:
            sys.exit('Invalid usage')

        text = input('Input: \n')
        font = args[1]
        figlet.setFont(font=font)

        return figlet.renderText(text)
    
    else:
        sys.exit('Invalid usage')

if __name__ == '__main__':
    print(main())