import datetime

def print_header():
    print('----------------------------')
    print('       BIRTHDAY APP')
    print('----------------------------')
    print()

def get_birthday_info():
    print('When were you born?')
    user_year = int(input("Year [YYYY]: "))
    user_month = int(input("Month [MM]: "))
    user_day = int(input("Day [DD]: "))
    user_bday = datetime.date(user_year, user_month, user_day)
    return user_bday


def compute_date_diff(user_bday):
    today = datetime.date.today()
    this_yr_bday = datetime.date(today.year, user_bday.month, user_bday.day)
    days = this_yr_bday - today
    return days.days


def print_bday_info(days):
    if days < 0:
        print('You had your birthday {} days ago.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days.'.format(days))
    else:
        print('Happy Birthday!!!')

def main():
    print_header()
    bday = get_birthday_info()
    days = compute_date_diff(bday)
    print_bday_info(days = days)


main()