# write a program to print interval in leap year

lowyear=int(input("please input your first year : "))
highyear=int(input("please input your last year : "))

for year in range(lowyear,highyear):
    if(year%4==0) and (year%100!=0) or year%400==0:
        print(year,"is leap year")