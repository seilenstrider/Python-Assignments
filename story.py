def begin_story():
	user_response = 0
	print("You are at home on a Saturday with your sick son when the Nuclear Warning Siren goes off. What do you do?")
	user_response = int(input("1.Grab your .44 magnum revovlver from your safe. \n2.Run to your sons room\n3. Grab your sons medicine."))
	decision1(user_response)
	
def decision1(user_response):
	print("You hear the screams of women and children outside your window.")
	if user_response == 1:
		print("What do you do next?")
		user_response = int(input("1.Grab extra ammo\n2.Call your wife\n3.Run to your sons room"))
		decision2_1(user_response)
	elif user_response == 2:
		print("You see that your son is having a mental breakdown.What do you do next?")
		user_response = int(input("1.Calm him down\n2.Grab him\n3.Leave him"))
	elif user_response == 3:
		print("You forgot what specific medicine he uses. What do you do next?")
		user_response = int(input("1.Grab all in the cabinet\n2.Guess and take one\n3.Screw it and leave."))
		decision2_3(user_response)
		
def decision2_1(user_response):
	if user_response == 1:
		print("What do you do next?")
		user_response = int(input("1.Begin to run to the vault\n2.Call your wife\n3.Go to your sons room"))
		decision2_1_1(user_response)
	elif user_response == 2:
		print("What do you do next?")
		user_response = int(input("1.Tell her you love her\n2.Tell her you will take care of their son \n3.Tell her you never loved her"))
	elif user_response == 3:
		print("He is having a mental breakdown.What do you do next?")
		user_response = int(input("1.Calm him down\n2.Grab him\n3.Leave him"))
		

def decision2_1_1(user_response):
  if user_response == 1:
    print("what do you do next?")
    user_response = int(input("1.Go back for your son\n2.Help others\n3.Force your way into vault"))
  if user_response == 2:
    print("What do you do next?")
    user_response = int(input("1.Help children\n2.Help elderly\n3.Help animals"))
  if user_response == 3:
    print("what do you do next?")
    user_response = int(input("1.Comfort him\n2.Play with him\n3.Grab him"))

def decision2_2_2(user_response):
  if user_response == 1:
    print("What do you do next?")
    user_response = int(input("1. Help others such as the elderly and children.\n2.Wait in the line for entry\3.Shove your way in."))
  if user_response == 2:
    print("What do you do next?")
    user_response = int(input("1.Tell her you love her.\n2.Tell her you will protect their son\3.Admit to not loving her."))
  if user_response == 3:
    print("What do you do next?")
    user_response = int(input("1.Tell him you love him\n2.Grab him\3.Leave him."))

def decision2_3(user_response):
	if user_response == 1:
		print("You notice there are too many pill bottles to hold. What do you do next?")
		user_response = int(input("1.Grab a bag to hold them\n2.Shove them in your pockets \n3.Just drop them"))
		decision3_1(user_response)
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.Read the back of the bottle\n2.Run to your son\n3.Hope your right."))
		decision3_2(user_response)
	elif user_response == 3:
		print("What do you do next?")
		user_response = int(input("1.Realize your mistake and go back\n2.Run to your son\n3.Look at your phone and research the medicine."))
		decision3_3(user_response)
		
def decision3_1(user_response):
  if user_response == 1:
    print("What do you do next?")
    user_response = int(input("1.Run to your son\n2.Get your gun\n3.Call your wife."))
    decision3_1(user_response)
  elif user_response == 2:
    print("What do you do next?")
    user_response = int(input("1.Run to your son\n2.Get your gun\n3.Call your wife"))
    decision3_2(user_response)
  elif user_response == 3:
    print("What do you do next?")
    user_response = int(input("1.Run to your son\n2.Get your gun\n3.Call your wife"))
    decision3_3(user_response)

def decision3_2(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.Grab him\n2.Talk to him\n3.Play with him"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.Grab more bullets\n2.Grab another gun\n3.Look for gun case"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.Tell her the truth\n2.Comfort her\n3.Hang up"))
    decision3_3(user_response)
    
def decision3_3(user_response):
  if user_response == 1:
    print("What do you do next?")
    user_response = int(input("1.Grab one bottle\n2.Grab two bottles\n3.Grab all"))
    decision3_1(user_response)
  elif user_response == 2:
    print("You see your son is in panic.What do you do next?")
    user_response = int(input("1.Grab him\n2.Comfort him\n3.Leave him"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.Search little kid medicine\n2.Search cough medicine\n3.Search antibiotics"))
    decision3_3(user_response)
	
#This runs the game
user_name = input("Enter your name")
begin_story()
