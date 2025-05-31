def main():
    invoice = input('Please type something here using uppercase: \n')

    invoice_low = invoice.lower()

    return invoice_low


if __name__ == '__main__':
    print(main())