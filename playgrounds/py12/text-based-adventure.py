def intro():
    i = str(input("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.\nA. Grab a nearby rock and throw it at the orc\nB. Lie down and wait to be mauled\nC. Run\n"))
    
    match i.upper():
        case "A":
            option_rock()
        case "B":
            print("Welp, that was quick. You died!")
        case "C":
            option_run()
        case _:
            print("error: not an option")
    
def option_rock():
    k = input("The orc is stunned, but regains control. He begins running towards you again.\nA. Run\nB. Throw another rock\nC. Run towards a nearby cave\n")
    
    match k.upper():
        case "A":
            option_run()
        case "B":
            print("The rock flew well over the orcs head. You missed. You died!")
        case "C":
            option_cave()
        case _:
            print("error: not an option")

def option_run():
    r = input("You run as quickly as possible.\nA. Hide behind boulder\nB. Trapped, so you fight\nC. Run towards an abandoned town\n")
     
    match r.upper():
        case "A":
            print("You're easily spotted. You died!")
        case "B":
            print("You're no match for an orc. You died!")
        case "C":
            option_town()
        case _:
            print("error: not an option")

def option_cave():
    choiceSword = input('Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?\n')
    if choiceSword.upper() == "Y":
        hasSword = True
    
    c = input("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.\nA. Grab a nearby rock and throw it at the orc\nB. Lie down and wait to be mauled\nC. Run\n")
    
    match c.upper():
        case "A":
            print("I think orcs can see very well in the dark, right? You died!")
        case "B":
            if hasSword:
                print("As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!")
            else: 
                print("You're defenseless. You died!")
        case "C":
            option_run()
            print('The orc turns around and sees you running.')
        case _:
            print("error: not an option")

def option_town():
    choiceFlower = input("You notice a purple flower near your foot. Do you pick it up? Y/N")
    if choiceFlower.upper() == "Y":
        print("You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!")
    elif choiceFlower.upper() == "N":
        print("Maybe you should have picked up the flower. You died!")
    else: print("error: not an option")
  
intro()