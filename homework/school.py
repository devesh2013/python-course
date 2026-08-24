name = input("enter ur name, club member: ")

club = input("enter ur school club: ")

member_number = 7

club_rating = 9.5

events_count = 12

height_m = 1.65

is_active = True

print("Name:", name, "-> type:", type(name))

print("Club:", club, "-> type:", type(club))

print("Member Number:", member_number, "-> type:", type(member_number))

print("Club Rating:", club_rating, "-> type:", type(club_rating))

print("Events Count:", events_count, "-> type:", type(events_count))

print("Height (m):", height_m, "-> type:", type(height_m))

print("Is Active:", is_active, "-> type:", type(is_active))

member_number_text = str(member_number)

events_count_text = str(events_count)

club_rating_text = str(club_rating)

status_text = str(is_active)

print("Member Number as text:", member_number_text, "-> type:", type(member_number_text))

print("Events Count as text:", events_count_text, "-> type:", type(events_count_text))

print("Club Rating as text:", club_rating_text, "-> type:", type(club_rating_text))

print("Status as text:", status_text, "-> type:", type(status_text))

first_three = name[0:3]

last_letter = name[-1:]

member_code = first_three + last_letter

print("First 3 letters of name:", first_three)

print("Last letter of name:", last_letter)

print("Member Code:", member_code)

reversed_club = club[::-1]

print("Reversed Club Name:", reversed_club)

badge_line_1 = "MEMBER " + member_code.upper()

badge_line_2 = "ID: " + member_number_text + " | EVENTS: " + events_count_text

badge_line_3 = "CLUB RATING: " + club_rating_text + " | ACTIVE: " + status_text

badge_line_4 = "CLUB CODE: " + reversed_club.upper()

print("")

print("===== SCHOOL CLUB MEMBER BADGE =====")

print(badge_line_1)

print(badge_line_2)

print(badge_line_3)

print(badge_line_4)

print("====================================")