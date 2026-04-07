#Full name: Ahsan Mohammed
#Date: 2/12/26
#CHapter number: 3
#Assignment name: Weather Category
#Description: Determine weather category based on user-chose wind speed
wind_speed = int(input("Enter wind speed: "))#ask for the wind speed -AM
if wind_speed<74:#check if category 1 -AM
    print("Storm is not a hurricane")
elif wind_speed >=74 and wind_speed <= 95:#check if category 2 -AM
    print("Category 1")
elif wind_speed >=96 and wind_speed <= 110:#check if category 3 -AM
    print("Category 2")
elif wind_speed >=111 and wind_speed <= 130:#check if category 4 -AM
    print("Category 3")
elif wind_speed >=131 and wind_speed <= 155:#check if category 5 -AM
    print("Category 4")
elif wind_speed >=156:#check if category 5-AM
    print("Category 5")