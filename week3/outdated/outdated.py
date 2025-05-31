def main():
    MONTHS = {
       "January": 1,
       "February": 2,
       "March": 3,
       "April": 4,
       "May": 5,
       "June": 6,
       "July": 7,
       "August": 8,
       "September": 9, 
       "October": 10,
       "November": 11,
       "December": 12,
    }   

    while True:
        bad_year = input('Date: \n').strip()

        if any(x in bad_year for x in MONTHS.keys()):
            try:
                month, day, year = bad_year.split(' ')
                if ',' not in day:
                    continue
                else:
                    month, day, year = MONTHS[month.capitalize()], int(day.strip(',')), int(year)
            except (KeyError, ValueError):
                continue
        else:
            try:
                month, day, year = bad_year.split('/')
                month, day, year = int(month), int(day), int(year)
            except ValueError:
                continue

        if 0 < day < 32 and 0 < month < 13:
            break

    return f'{year}-{month:02}-{day:02}'

if __name__ == '__main__':
    print(main())
