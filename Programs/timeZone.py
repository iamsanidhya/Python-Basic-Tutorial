import datetime
import pytz
datetimeToday = datetime.datetime.now(tz=pytz.UTC)
datetimePacific = datetimeToday.astimezone(pytz.timezone('Asia/Kolkata'))
print(datetimePacific)

