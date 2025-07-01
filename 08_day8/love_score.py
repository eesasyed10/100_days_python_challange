def calculate_love_score(name1,name2):
    names_combined=name1 + name2
    lower_case_names=names_combined.lower()
    
    t=lower_case_names.count("t")
    r=lower_case_names.count("r")
    u=lower_case_names.count("u")
    e=lower_case_names.count("e")
    first_digit= t+r+u+e
        
    l=lower_case_names.count("l")
    o=lower_case_names.count("o")
    v=lower_case_names.count("v")
    e=lower_case_names.count("e")
    second_digit=l+o+v+e
    
    print(f"your love score is {first_digit }{second_digit}.")
    
calculate_love_score(input("enter the first name: "),input("enter second name: "))
