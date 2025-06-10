from datetime import date, datetime, time
import sys
import inflect


def main():
    try:
        birthday = input('Birthday: ')
        dob = Custom_date(birthday)
        minutes = dob.minutes_from_today()
        print(make_song(minutes))
    except:
        sys.exit('Invalid date')

class Custom_date:
    def __init__(self, d):
        parts = d.split('-')

        self.year = int(parts[0])
        self.month = int(parts[1])
        self.day = int(parts[2])
        self.datetime = datetime(self.year, self.month, self.day, 0, 0, 0)
    
    def from_epoch(self):
        return self.datetime.timestamp()
    
    def minutes_from_today(self):
        today = date.today()
        midnight = time(0, 0, 0)
        now = datetime.combine(today, midnight)

        return int((now.timestamp() - self.from_epoch()) / 60)

    

def make_song(minutes):
    p = inflect.engine()

    song = p.number_to_words(minutes, andword='').capitalize()

    return f'{song} minutes'


        
        



if __name__ == "__main__":
    main()
