def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '1234567890'
    allowed = abc + nums
    
    if len(s) > 6:
        return False
    elif len(s) < 2:
        return False
    
    if any(x not in allowed for x in s):
        return False
    
    if s[0] not in abc or s[1] not in abc:
        return False
    
    for i in range(len(s)):
        if s[i] == '0' and s[i-1] in abc:
            return False
        if s[i] in nums:
            return all(x in nums for x in s[i+1:])
    
    return True


if __name__ == "__main__":
    main()