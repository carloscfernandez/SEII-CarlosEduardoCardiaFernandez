#def hello_func(greeting, name = 'YOu'):
    #print('Hello Function!')
    #return'Hello Function!'
    #return '{}, {}'.format(greeting, name)

#print(hello_func('Hi', name = 'Corey'))

#print(hello_func().upper())
#hello_func()


#def student_info(*args, **kwargs):
 #   print(args)
  #  print(kwargs)

#courses = {'Math', 'Art'}
#info={name: 'John', age: 22}
#student_info(*courses, **info)


#student_info('Math', 'Art', name='John', age=22)


month_days={0, 31, 28, 31, 30, 31, 31, 31, 30, 31, 30, 31}

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017,2))
