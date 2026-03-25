weather = input("Weather (sunny/rainy): ")
temp = input("Temperature (hot/cool): ")
humidity = input("Humidity (high/normal): ")
wind = input("Wind (strong/weak): ")

if weather == "sunny":
    if humidity == "high":
        print("Do not play")
    else:
        print("Play")
elif weather == "rainy":
    if wind == "strong":
        print("Do not play")
    else:
        print("Play")
else:
    print("Play")