#calender for particular year
import calendar
y=int(input("enter the value of the year"))
m=1
cal=calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=12:
    cal.prmonth(y,i)
    i=i+1
