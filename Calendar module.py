import calendar
print(calendar.weekheader(3))
print(calendar.firstweekday())
print(calendar.month(2020, 1, w = 3))


x = 1
while x > 11:
    x += 1
    matrix = calendar.monthcalendar(2020, x)
    print(matrix)


#print(calendar.monthcalendar(2020, x))
print(calendar.calendar(2020, w=3))
is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_days = calendar.leapdays(2010,2020)
print(how_many_leap_days)

l = "hello world"
print(l [10::-1])
data = 'xbox360 | 150 | New'
print(data[9:data.index('|')])
product = data[:data.index('|')]
price = data[data.index('| '):data.index('| ')]
price = data[data.index('|')+2:data.rindex('|')]
condition = data[data.rindex('|')+1:]
print(product, price, condition)
word = 'hello'
print(word[4::-1])