def life_in_weeks(x):
    age_left = 90 - x
    in_weeks = age_left*52
    print(f"There are only {in_weeks} weeks left in your life!")



age = int(input("Enter your current age:"))

life_in_weeks(age)