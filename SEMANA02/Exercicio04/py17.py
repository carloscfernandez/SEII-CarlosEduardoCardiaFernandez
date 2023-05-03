
import datetime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.timezone('America/Sao_Paulo'))
#dt_mtn = dt_utcnow.astimezone(pytz.timezone('America/Sao_Paulo'))
#print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))                     # strftime - datetime to string

dt_str='May 03, 2023'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')     #  strptime - string to datetime
print(dt)

#dt = datetime.datetime(2016, 7, 26, 9, 20, 45, tzinfo=pytz.UTC)
#print(dt)

#dt_today = datetime.datetime.today()
#dt_now = datetime.datetime.now(tz=pytz.UTC)
#print(dt_now)

#dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
#print(dt_utcnow)

#dt_mtn = dt_utcnow.astimezone(pytz.timezone('America/Sao_Paulo'))
#print(dt_mtn)

#for tz in pytz.all_timezones:
  #  print (tz)


#dt = datetime.datetime(2016, 7, 26, 9, 20, 45, 100000)
#tdelta = datetime.timedelta(hours=12)
#print(dt + tdelta)


#t = datetime.time(9, 20, 45, 100000)       Horas, minutos, segudos e milesimos



#tday = datetime.date.today()
#print(tday.day)
#print(tday.weekday())
#print(tday.issoweekday())

#tdelta = datetime.timedelta(delta=7)
#print(tday - tdelta)

#bday = datetime.date(2024, 2, 6)
#till_bday = bday - tday
#print(till_bday.total_seconds())
#print(till_bday.days)
#print(till_bday)
