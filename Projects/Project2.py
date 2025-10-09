introvert_points = 0
extrovert_points = 0


answer = input("On a weekend would you rather A nap all day, or B go on a hike?")
if answer == "A":
	introvert_points += 1
elif answer == "B":
	extrovert_points += 1
print

answer = input("Would you rather A spend time alone, or B spend time in a group")
if answer == "A" or answer == "a":
	introvert_points += 1
elif answer == "B":
	extrovert_points += 1


answer = input("Would you rather work A by yourself, or B with a group?")
if answer == "A":
	introvert_points += 1
elif answer == "B":
	extrovert_points += 1
	

answer = input("Would you rather A be the center of attention, or B be out of the spotlight")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points += 1
	

answer = input("would you rather A go to the park and see friends, or stay at home all day")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points += 1
	

answer = input("Do you prefer A make decisions in private, or B make decisions in a group setting")
if answer == "A" and introvert_points > 3:
	print("you are an introvert")
	introvert_points += 1
if answer == "B" and extrovert_points > 3:
	print("You are an extrovert")
	extrovert_points += 1


