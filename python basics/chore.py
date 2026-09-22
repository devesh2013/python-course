total_chores = 4
original_count = total_chores
print(f"you have {original_count} chores to finish today!\n")
completed_count = 0
chore_num = 1
if chore_num == 1: next_chore = "make your bed"
elif chore_num == 2: next_chore = "feed the pet"
elif chore_num == 3: next_chore = "take out the trash"
else: next_chore = "wash the dishes"
answer = input(f"have u finished :{next_chore}? (yes/no): ")
if answer == "yes":
    completed_count += 1
    chore_num += 1
    print("great job! time to sleep")
else:
        print("do ur chores then go to sleep")
print("==== ALL CHORES COMPLETED! ====")
print("great work finishing ur chores today!\n")
print("now lets safely peek at an infinite loop")
test_value = 0
safety_value = 0
while test_value <= 0:
        print("this condition never changes,so this would run forever!")
        safety_counter += 1
if safety_counter == 3 :
        print("(stoping here on purpose - a real infinite loop never stops on its own!)")
print("\n==== CHORE CHECKLIST SUMMARY ================================")
print("Chores Assigned today:", original_count)
print("print completed:", completed_count)
print("chores remaining:",total_chores - completed_count)
print("================================================")