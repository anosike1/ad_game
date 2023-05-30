# You are an explorer on an expedition to discover the ancient secrets of an ancient temple
# get ASCII art from www.ascii.co.uk/art

print ("""
888                                888         
888                                888         
888                                888         
888888 .d88b. 88888b.d88b. 88888b. 888 .d88b.  
888   d8P  Y8b888 "888 "88b888 "88b888d8P  Y8b 
888   88888888888  888  888888  88888888888888 
Y88b. Y8b.    888  888  888888 d88P888Y8b.     
 "Y888 "Y8888 888  888  88888888P" 888 "Y8888  
                           888                 
                           888                 
                           888    
""")

chooz = input ("You are embarking on an expedition to discover the hidden secrets of an ancient forgotten temple and find three items: a MATCH, a FLASHLIGHT, and a WINDOW. Which one do you want to choose? ")

if chooz.lower() == 'match':
    python = input ("You pick up the  match and strike it, and for an instant, the room around you is illuminated. You see a large python, and then the match burns out. Do you want to RUN away, GO forward, or STRIKE another match? ")

    if python.lower() == 'run':
        print ("Good bye, Coward.")

    elif python.lower() == 'go':
        print ("Good luck, Soldier.")

    elif python.lower() == 'strike':
        print ("Hope you killed a snake before, mate.")

    else:
        print ("Wrong choice...")

elif chooz.lower() == "flashlight":
    pathway = input ("You pick up the flashlight and turn it on. You see a door lit up on your right side, but you thought you also heard something right in front of you. Do you want to ENTER the room or LOOK ahead for the thing that made the noise? ")

    if pathway.lower() == 'enter':
        print ("Howdy Explorer, hope you find something nice.")

    elif pathway.lower() == 'look':
        print ("Hey there, Curious Cat. Don't get yourself killed.")

    else:
        print ("Wrong choice...")


elif chooz.lower() == "window":
    window = input ("You find a window and try to open it, but a vampire appears and begs you to leave it shut. Do you want to open the window and let the sunlight KILL him or leave it shut and SPARE his life?  ")

    if window.lower() == 'kill':
        print ("You must be Van Helsing. Cos you just killed Dracula.")

    elif window.lower() == 'spare':
        print ("Good day Mr. Renfield. Dracula owes you his life.")

    else:
        print ("Wrong choice...")

    
else:
    print ("Wrong Choice...")
