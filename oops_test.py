class car:
    # brand=car_brand
    def __init__(self,name,brand,max_speed):
        self.name=name
        self.brand=brand
        self.speed=max_speed

    def info(self):
        print(f"""CAR NAME : {self.name}\nCAR BRAND : {self.brand}\nCAR SPEED : {self.speed} """)


car_brand=input("enter your car's brand: ")
car_name=input("enter your car's name: ")
car_colour=input("enter your car's colour : ")
car_speed=input("enter your car's speed: ")

car_name=car(name=car_name,brand=car_brand,max_speed=car_speed)
on=True
while on:
    ui=input("enter ")
car_name.info()