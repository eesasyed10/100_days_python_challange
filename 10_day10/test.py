# def split_bill_print(total_amount, num_people):
#     each_share = total_amount / num_people
#     print(f"Each person owes ₹{each_share:.5f}")

# # Call the function
# split_bill_print(2400, 4)   # Prints: Each person owes ₹600.00

# # Suppose one friend wants to pay double:
# # You cannot write something like:
# #   double_share = split_bill_print(2400, 4) * 2
# # Because split_bill_print(...) returns None, not 600.


def full_name(first_name,last_name):
    if first_name=="" or last_name=="":
        return "you haven't written anything yet?"
    format1=first_name.title()
    format2=last_name.title()
    print(f"your name is {format1} {format2}.")
    
full_name(input("enter your first name?"),input("enter your last name?"))