def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(f"{year} is leap year.")
            else:
                print(f"{year} is not leap year.")
        else:
            print(f"{year} is leap year.")
    else:
        print(f"{year} is not leap year.")
        
is_leap_year(int(input("enter the year.")))