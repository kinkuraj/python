#Heater - 2000Wt - 3hrs - 2000wt/1000wt = 2unit - 6
#Light - 40Wt - 18hrs - 40/1000 = 0.04 unit - 
#Fan - 75Wt - 24hrs - 75/1000 = 0.075 u
#Computer - 500 wt - 18hrs = 0.5 u
#What's the total bill for a month?
#Unit- 2.5R
# 1 Unit - 1000Wt/hr
list = {'H':2, 'L':0.04, 'F':0.075,'C':0.5}
heater = float(input("How many hours a day heater runs?"))
light = float(input("How many hours a day light runs?"))
fan = float(input("How many hours a day fan runs?"))
computer = float(input("How many hours a day computer runs?"))
#print(type(heater))

totalconsmpution_day = heater * list.get('H') + light * list.get('L') + fan * list.get('F') + computer * list.get('C')
#print(totalconsmpution_day)
#per day total bill
tot_bill_day = totalconsmpution_day * 2.5

list_30 = [4,6,9,11]
days = 30 if(datetime.datetime.now().month in list_30) else 28 if(datetime.datetime.now().month == 2) else 31
print(days)

tot_bill_month = tot_bill_day * days
print("Total bill for the month {0} is {1}".format(datetime.datetime.now().strftime("%x"),tot_bill_month))
