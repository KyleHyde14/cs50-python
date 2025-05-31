def main():
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    camel_case = input('Enter your Camel variable: \n')

    if all(x not in upper for x in camel_case):
        return camel_case
    
    for x in range(len(camel_case)):
        if camel_case[x] in upper:
            temp = camel_case[x].lower()
            camel_case = f'{camel_case[0:x]}_{temp}{camel_case[x+1:]}'

    return camel_case

if __name__ == '__main__':
    print(main())