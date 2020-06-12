#                                        FOR DATE
import datetime
import pytz #we are using module for date time
today = datetime.date.today() #example for today date we can pass (int,string) inside.
print(today)

birthday = datetime.date(1994,7,14)  #here the format is YY-MM-DD
print(birthday)

daysSinceBirth = (today - birthday).days
print(daysSinceBirth)

tadd = datetime.timedelta(days=10)  #timedelta is use to assign days value to a variable and use it later like add subtract
print(today - tadd)

print(today.month)   #it gives today month
print(today.day)     #it gives today day information
print(today.weekday())   #it gives today weekday information i.e : 0 - Monday, 1- Tuesday ....so on....6- Sunday
datetimeToday = datetime.datetime.now(tz=pytz.UTC)
datetimeasia = datetimeToday.astimezone(pytz.timezone('Asia/Kolkata'))
print(datetimeasia)
for tz in pytz.all_timezones:
	print(tz)

print(datetime_aisa.strftime('%B %d,%Y'))

