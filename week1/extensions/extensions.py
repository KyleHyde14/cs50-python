def main():
    MIMES = {
        'jpeg': 'image/jpeg',
        'jpg': 'image/jpeg',
        'gif': 'image/gif',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip',
    }

    file = input('Enter a file name with or without extension: \n').lower().strip()

    extension = file.split('.')[-1]
    if extension in MIMES:
        return MIMES[extension]
    
    return 'application/octet-stream'

if __name__ == '__main__':
    print(main())
