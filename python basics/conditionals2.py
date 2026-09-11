print("=== Smart School Day Planner ===")
print("answer 3 questions and i will tell ur day! \n")
day = input("What day it is?(Monday to Sunday): ").strip().capitalize()  
weather = input("What is the weather?(sunny / rainy / cloudy): ").strip().lower() 
homework = input("Is ur homework done?(yes / no): ").strip().lower() 
print()
print(f"=== ur plan for (day) ===")
print("-" * 35)
if day in ("friday","saturday"):
    print("day type : weekand - enjoy ur free time")
elif day == "Sunday" :
    print("day type : first day of the week.be absent.")
elif day == "Thursday":
    print("day type : last day of school,freedom awaits!")
elif day == ("Monday", "Tuesday", "Wednesday") :
    print("day type : another boring school day, stay focused")
else :
    print("day type : stop lying,tell the truth")
    if weather == "sunny" and homework == "yes":
        print("After school: go home straight away and sleep for the whole day if u finished ur homework.")
if weather == "rainy" and (homework == "yes"):
        print("After school: go to ur friends house and play games.")

if not  (homework == "yes"):
        print("After school: finish ur homework then go to play.")

if weather == "rainy" and not (homework == "yes") :
    print("Best plan : stay insied and finish homework")
elif weather == "sunny" and  (homework == "yes") and not (day in("saturday", "friday")) :
    print("Best plan : All set for a great school day - u are prepared")
if day in ("saturday","friday") and weather == "sunny" :
    print("Best plan : just sleep all day")

else:
    print("best plan : take it one step at one time - u got this ")
    
    print()
    print("plan done! time to sleep")

