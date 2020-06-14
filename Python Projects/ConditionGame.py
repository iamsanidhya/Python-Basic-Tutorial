print("Welcome to my game!")
name = input("What is your name? ")
age = int(input("What is your age? "))
health = 10

print("You are starting with ", health,"health")
if age >= 18 :
	print("You are eligible to play:) ")
	wants_to_play = input("Do you want to play: ").lower()
	if wants_to_play =="yes":
		print("Lets play!")
		left_or_right = input("First choice... Left or Right (left/right)? ").lower()
		if left_or_right == "left":
			ans = input("Nice, you followed the right path and reach a lake...Will you swim across or around (across/around)").lower()
			if ans == "around":
				print("You went around and reached other side of the lake ")
			elif ans == "across":
				print("You managed to get across, but were bit by a fish and lost 5 health.")
				health -=5
			ans = input("You notice a house and a river. What will you choose (house/river)? ").lower()
			if ans == "house":
				print("You go to the house and greeted the owner... he didn't like you and now you lost 5 health")
				if health <= 0:
					print("You have a health of 0 so you lost the game...")
				else:
				    print("You survived and won!!!")	


			else:
			    print("You fell in the river and lost....")	

		else:
			print("You fell down and lost...")
	else:
		print(";/")         
else:
	print("You are not eligible;( ")	    
