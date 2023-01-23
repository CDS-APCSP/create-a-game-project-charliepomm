import os, time, random


# Level 1
def level_1():
    print("You are trying to sneak onto the Death Star and destroy it")
    time.sleep(2)
    print("There are stormtroopers infront of you.")
    time.sleep(2)
    user_input = input("Do you want to fight the stormtroopers or sneak past them? (fight/sneak) ")
    if user_input == "fight":
        print("You engage in a fierce battle and defeat the stormtroopers.")
        lvl1=True
    elif user_input == "sneak":
        print("You successfully sneak past the stormtroopers.")
        (lvl1)=True
    else:
        print("Invalid input. You are caught and fail the mission.")
        return
    print("You move on to the next level.")

# Level 2
def level_2():
    print("You have snuck onto the Death Star.")
    print("There is a maze infront of you")
    time.sleep(2)
    user_input = input("Do you want to go left or right at the fork in the maze? (left/right) ")
    if user_input == "left":
        print("You choose the left path and find yourself in a dead end.")
        print("You fail the mission.")
        return
    elif user_input == "right":
        print("You choose the right path and successfully navigate the maze.")
    else:
        print("Invalid input. You are lost in the maze and fail the mission.")
        return
    print("You reach the control room.")
    time.sleep(2)
    user_input = input("Do you want to sabotage the Death Star's systems? (yes/no) ")
    if user_input == "yes":
        print("You sabotage the Death Star's systems and move on to the final level.")
        (lvl2)=True
    elif user_input == "no":
        print("You fail to sabotage the Death Star's systems and fail the mission.")
        return
    else:
        print("Invalid input. You fail the mission.")
        return

# Level 3
def level_3():
    print("You have made it to the final battle.")
    print("You are in the middle of a dogfight against the Empire's TIE fighters.")
    time.sleep(2)
    user_input = input("Do you want to fly aggressively or defensively? (aggressive/defensive) ")
    if user_input == "aggressive":
        print("You fly aggressively and successfully destroy all the TIE fighters.")
    elif user_input == "defensive":
        print("You fly defensively and successfully destroy all the TIE fighters.")
    else:
        print("Invalid input. You are shot down and fail the mission.")
        return
    print("You are ready to fire the final shot.")
    time.sleep(2)
    user_input = input("Do you want to fire the final shot? (yes/no) ")
    if user_input == "yes":
        print("You fire the final shot and successfully destroy the Death Star.")
        print("Congratulations! You have completed the game.")


def main():
  level_1()
  level_2()
  level_3()

main()