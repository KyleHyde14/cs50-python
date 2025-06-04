import sys
from PIL import Image, ImageOps

def main():
    args = sys.argv

    accepted = ['jpeg', 'jpg', 'png',]

    if len(args) != 3:
        sys.exit('Expected exactly 2 command-line arguments')

    fmt_1 = args[1].split('.')[-1]
    fmt_2 = args[2].split('.')[-1]
    
    if fmt_1 not in accepted or fmt_2 not in accepted:
        sys.exit('Invalid file format')
    elif fmt_1 != fmt_2:
        sys.exit('Both files must be the same file format')

    try:
       put_shirt(args[1], args[2])
    except FileNotFoundError:
        sys.exit('Input file not found')
        
    
def put_shirt(input_file, output_file):
        shirt = Image.open('shirt.png')
        size = shirt.size

        try:
            with Image.open(input_file) as img:
                fit_img = ImageOps.fit(img, size)
                fit_img.paste(shirt, shirt)
                fit_img.save(output_file)
        except FileNotFoundError:
            raise FileNotFoundError
            

if __name__ == "__main__":
    main()
