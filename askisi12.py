import datetime
import random

current_date = datetime.datetime.now()
random_date = datetime.datetime.strptime('{} {}'.format(random.randint(1, 366), random.randint(1900, 2019)), '%j %Y')
day_difference = abs(current_date - random_date).days
hour_difference = abs(current_date - random_date).seconds//60%60
second_differnce = abs(current_date - random_date).seconds
print(random_date, "Απέχει: ", day_difference, "ημέρες", hour_difference, "ώρες και", second_differnce, "δευτερόλεπτα")
month = int(random_date.strftime("%m"))
if month == 0o2:
    print("Ο μήνας έχει 28 μέρες")
elif month == 0o4 or month == 0o6 or month == 9 or month == 11:
    print("Ο μήνας έχει 30 μέρες")
elif month == 0o1 or month == 0o3 or month == 0o5 or month == 0o7 or month == 8 or month == 10 or month == 12:
    print("Ο μήνας έχει 31 μέρες")
