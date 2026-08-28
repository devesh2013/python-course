temperature = int(input("Enter todays temperature in celsius: "))
if temperature < 20:
    outfit = "jacket"
    print("it is cold today.")
    print("Wear a", outfit)
    is_raining = input("is it raining today? (yes/no): ")
    if is_raining == "yes":
        print("bring a umbrella")
    wind_speed = int(input("eneter the wind speed in km/h: "))
    if wind_speed > 30:
        needs_windbreaker = "yes"
        print("it is windy today")
        print("wear a windbreaker over your, outfit")
    else:
        needs_windbreaker = "no"
        print("it is calm today.")
        print("no windbreaker needed over your, outfit")
        has_puddles = input("are there puddles on the ground? (yes/no): ")
        if has_puddles == "yes":
            shoes = "boots"
            print("the gound is wet.")
            print("wear", shoes)
            print("")
            print("weather check complete")
            print("==== WEATHER OUTFIT PICKER ====")
            print("temperature:",temperature)
            print("outfit chosen:",outfit)
            print("raining:", is_raining)
            print("windbreaker needed:" , needs_windbreaker)
            print("shoes chosen:", shoes)
            print("===============================================")
