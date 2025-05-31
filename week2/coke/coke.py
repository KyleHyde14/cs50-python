def main():
    cost = 50
    inserted = 0
    
    accepted = [50, 25, 10, 5]

    while inserted < cost:
        print(f'Amount due: {cost - inserted}')
        amount = int(input('Insert coin: \n'))

        if amount in accepted:
            inserted += amount
        else: 
            continue

    return f'Change owed: {inserted - cost}'

if __name__ == '__main__':
    print(main())
