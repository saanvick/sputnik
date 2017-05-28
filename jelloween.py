print "Welcome, Player. What is your name?"

name = raw_input(">>> ")

print "Thanks. Just a hint, make sure that all your word answers are in capital letters. Press Enter to begin."

raw_input()

while True:
    print "It's New Year's Eve! You're at your friend's house when you all start playing Truth or Dare. When it's your turn, you bravely say - 'Dare.' They reply, 'You have to go inside the haunted house across the street, alone.'"

    raw_input()

    print "You're absolutely terrified, but a dare is a dare. You and you friends put on your shoes and in the dead of night, walk across the street towards the haunted house. They wait by the gate while you enter the house. It's cold and dark. You're about to leave when you feel a hand clutching your shoulder!"

    raw_input()

    print "You immediately start running, petrified, and when you think you've shaken them off, you stop. Then it dawns on you that you are completely lost, in the middle of the enormous house. You know your friends are awaiting your return and you have to get out!"

    raw_input()

    print "You weave through corridors and trudge up staircases until you enter a room with three doors, labelled #1, #2 and #3. Which door do you pick?"

    door = raw_input(">>> ")

    if door == "1":
        print "The room is dark, but you can see a map. However, in the corner you can see a rhinoceros. They have poor vision, so it can't see you yet, but if you pick up the map which is in the centre of the room, it will chase after you. What do you do?"
        print "1. You pick up the map."
        print "2. Chase after the rhino to make it leave."
    
        rhino = raw_input(">>> ")
    
        if rhino == "1":
            print "You sprint towards the map at full speed, but the rhino gets there first. It pierces you in the chest with its horns and you die. The End."
            print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
    
            restart = raw_input(">>> ")
    
            if restart == "NO": 
                break
            
        elif rhino == "2":
            print "You charge at the rhino, but it kills you. For obvious reasons. The End."
            print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
    
            restart = raw_input(">>> ")
    
            if restart == "NO": 
                break
        
    elif door == "2":
        print "The room is bright and in the middle you find a witch busily adding ingredients to her cauldron. What do you do?"
        print "1. You approach the witch and ask how to leave the house."
        print "2. Explore the rest of the room."
           
        witch = raw_input(">>> ")
            
        if witch == "1":
            print "The witch looks up, a nasty grin on her face. Laughing nastily, she cuts up your body and adds your body parts to the cauldron. The End."
            print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
    
            restart = raw_input(">>> ")
    
            if restart == "NO": 
                break
            
        elif witch == "2": 
            print "Careful not to draw the attention of the witch to yourself, you quietly walk across the room to a large fountain. What do you do?"
            print "1. You step inside the fountain."
            print "2. You move on."
            print "3. You go back to the witch and ask for directions."
        
            fountain = raw_input(">>> ")
             
            if fountain == "1":
                print "The fountain transports you to a secret lair under the house. You have landed on the edge of a volcano! It seems empty and inactive but you can't be sure. Looking around, it is a short slide down the side of the volcano. What will you do?"
                print "1. You slide down the edge of the volcano."
                print "2. You step inside the volcano."
        
                volcano = raw_input(">>> ")
        
                if volcano == "1":
                    print "After sliding into a large rock, you flip over, break your neck, damage your spinal cord and die at the foot of the volcano. The End."
                    print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                    restart = raw_input(">>> ")
        
                    if restart == "NO": 
                        break
                    
                elif volcano == "2":
                    print "You carefully climb your way down the inside of the volcano. It's dark, so you can't see much. You can also hear a faint buzzing at the bottom. You stumble on a rock and are hanging on for dear life. It could be dangerous to go on. What do you do?"
                    print "1. Grab hold of the rock and climb your way down again."
                    print "2. Go back up and slide down the edge of the volcano."
            
                    volcano2 = raw_input(">>> ")
            
                    if volcano2 == "1":
                        print "You swing your arm and grab hold of the rock again. After this encounter, it's a pretty smooth journey down and you land both feet firmly planted on the floor of the volcano."
                        print "Once down, you realise that the volcano is not what it seems, and has multiple passages, presumably leading to different rooms. They are labelled A, B and C. Which do you pick?"
                
                        passage = raw_input(">>> ")
                
                        if passage == "A":
                            print "The path winds on and on and on and on and on. And on. And on. You feel yourself getting dizzy, and thoroughly overcome with fatigue, you accidentally stumble into an abyss. The End."
                            print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                            restart = raw_input(">>> ")
        
                            if restart == "NO":
                                break
                            
                        elif passage == "B":
                            print "As you walk on, you start hearing a loud blaring announcement. 'Welcome ladies and gentlemen, boys and girls! Witness a spectacle of a lifetime! A thrilling sight has been lined up for you today!'"
                            print "'Today, the Colosseum hosts the vicious beast of the East, the Bengal tiger!' You hear cheering as you listen from the sidelines. 'Versus your favourite gladiator... {}!".format(name)
                            print "You are in a state of shock, but a guard drags you out into the arena to hoots and cheers from the audience. You are totally unarmed, and you are unsure of how to fight the tiger. Dead bodies are strewn across the sand. You spot bronze weapons in the corner."
                            print "The gate behind you closes and you are trapped in with the ferocious beast. What do you do?"
                            print "FIGHT"
                            print "TAME"
                    
                            tiger = raw_input(">>> ")
                    
                            if tiger == "FIGHT":
                                print "You grab a spear at the edge of the arena, and tentatively wave it around at the animal. It starts running towards you. Do you want to STAB or PARRY?"
                            
                                fight = raw_input(">>> ")
                            
                                if fight == "STAB":
                                    print "Do you want to STAB or PARRY?"
                                
                                    fight2 = raw_input(">>> ")
                                
                                    if fight2 == "STAB":
                                        print "You stab the animal in the chest and it falls to the ground, defeated. There is a shocked silence in the crowd, but the gate rises and you quickly make your escape."
                                        print "Once through the gate, you can hear a buzzing sound, the same one you heard at the volcano. You move further in to investigate and stumble across a large, mystical forest. You feel yourself getting drowsy, and fall asleep on a large mushroom."
                                        print "When you awaken, you find a woman standing over you. She seems friendly, but you haven't exactly had many friendly encounters here, have you? What do you do?"
                                        print "1. Run away."
                                        print "2. Ask the woman questions."
                                    
                                        woman = raw_input(">>> ")
                                    
                                        if woman == "1":
                                            print "You run as fast as you can away from the woman, scared. However, you trip over another large mushroom and fall headfirst into a marsh. The End."
                                            print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                            restart = raw_input(">>> ")
        
                                            if restart == "NO": 
                                                break
                                        elif woman == "2":
                                            print "Ask these questions, in order."
                                            print "1. Who are you?"
                                            print "2. Who built this?"
                                            print "3. How do I get out of here?"
                                            
                                            question = raw_input(">>> ")
                                            
                                            if question == "1":
                                                print "'Me?' she says. 'I am a witch, but not like the other creatures in this house. I am not a creation. I,' she says, 'I am real.'"
                                                print "Ask another question."
                                                print "2. Who built this?"
                                                print "3. How do I get out of here?"
                                                
                                                question2 = raw_input(">>> ")
                                                
                                                if question2 == "2":
                                                    print "'An old vampire, who hated the world we came from. He wished to plague this world with dark creatures. But,' she says. 'He loved me. And dragged me off to this Earth, where I now live in solitude, for I have put him to sleep."
                                                    print "Ask the last question."
                                                    print "3. How do I get out of here?"
                                                    
                                                    question3 = raw_input(">>> ")
                                                    
                                                    if question3 == "3":
                                                        print "'Why,' she exclaims. 'I can take you. If you wish, I will transport you to the world outside.' You agree, excited. You feel the world spinning, and land outside on the pavement, to find your friends once again."
                                                        print "Well done {}! You escaped the house! Want to meet this old vampire? Have another go. If you want to, press any key, If not, type NO into the prompt.".format(name)
                                                        
                                                        restart = raw_input(">>> ")
        
                                                        if restart == "NO": 
                                                            break
                                    
                                    elif fight2 == "PARRY":
                                        print "Parrying doesn't work too well on large Bengal tigers, as you soon find out. The End."
                                        print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                        restart = raw_input(">>> ")
        
                                        if restart == "NO": 
                                            break
                                
                                elif fight == "PARRY":
                                    print "Parrying doesn't work too well on large Bengal tigers, as you soon find out. The End."
                                    print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                    restart = raw_input(">>> ")
        
                                    if restart == "NO": 
                                        break
                                
                            if tiger == "TAME":
                                print "You are totally grossed out, but pick up a hunk of rotten human flesh and throw it, a little distance away from the tiger. The tiger sniffs it, and then takes a huge bite of it. What do you do?"
                                print "The tiger seems entranced for a few moments, but a shout from the audience kicks in its animal instincts. It pounces on you and you die. The End."
                                print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                restart = raw_input(">>> ")
        
                                if restart == "NO":
                                    break
            
                        elif passage == "C":
                            print "You walk on, and find an empty cavern. As you walk in, you realise that something is not right. You can hear heavy breathing at the end of the cave. You try to turn back, but your exit has been blocked by a number of heavy boulders. What do you do?"
                            print "1. Walk further on and find out what it is."
                            print "2. Try and move the boulders."
                        
                            cave = raw_input(">>> ")
                        
                            if cave == "1":
                                print "You walk deeper into the cave. As you delve further, you can make out the faint shape of a dragon at the very end. Its eyes suddenly pop open, and it spots you. You try making a break for it but it catches and kills you. The End."
                                print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                restart = raw_input(">>> ")
        
                                if restart == "NO": 
                                    break
                            elif cave == "2":
                                print "You try moving some of the boulders, but as you push them, one falls on top of you and crushes you to a pulp. The End."
                                print "Nice try {}, do you want to try again. If so press any key. If not, type NO into the prompt.".format(name)
                    
                    elif volcano2 == "2":
                        print "Whoops! I lied. You injure yourself. After sliding into a large rock, you flip over, break your neck, damage your spinal cord and die at the foot of the volcano. The End."
                        print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                        restart = raw_input(">>> ")
        
                        if restart == "NO": 
                            break   
               
            elif fountain == "2":
                print "You carry on your journey, and find another door. However when you open it, there is a giant tarantula that attacks and kills you. The End."
                print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                restart = raw_input(">>> ")
        
                if restart == "NO": 
                        break
            elif fountain == "3":
                print "The witch looks up, a nasty grin on her face. Without a word, she cuts up your body and adds your body parts to the cauldron. The End."
                print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                restart = raw_input(">>> ")
        
                if restart == "NO": 
                    break
                    
    elif door == "3":
        print "Room #3 is quite small but you can see a door at the end of the room! However, there is a sphinx standing in your way. She says to you, 'You can only pass if you answer my riddle correctly. Answer wrongly, and I will attack. Say nothing, and I will let you walk away from me unscathed.' What do you do?"
        print "1. Ask for the riddle."
        print "2. Look for an alternative option."
        print "3. Squeeze past the sphinx."
    
        sphinx = raw_input(">>> ")
    
        if sphinx == "1":
            print "The sphinx smiles and says,"
            print "What is the creature that walks on four legs in the morning,"
            print "Two legs in the afternoon,"
            print "And three legs in the evening?"
        
            riddle = raw_input(">>> ")
        
            if riddle == "A MAN" or "MAN" or "A HUMAN" or "A PERSON" or "HUMANS" or "MEN" or "PEOPLE" or "MANKIND":
                print "The sphinx smiles again, and lets you pass. You go down some stairs until you enter a dungeon full of squeaking rats and spiders. Sickened, you explore the place, trying to avoid stepping on anything. Eventually you find a torch lying around."
                print "You find an old key as well. It's quite rusty, but it can still open doors."
            
                raw_input()
            
                print "You walk on. The room is getting narrower and narrower and you have to sidestep to get past. After a while, you find a door that leads to an old temple. There are many inscriptions on the wall, but just as you learn that the temple is cursed, a centaur appears from the shadows."
                print "The centaur stares at you and says, 'What are you doing here, child?'"
            
                raw_input()
            
                print "You tell him the truth and when he speaks, his voice echoes around the temple.'Foolish child! There's no escaping this house. Your only hope is to defeat the vampire. He is indestructible, but his weakness is light.' He sighs, 'There has not been light in this place for many years.'"
                print "1. Ask the centaur how to reach the vampire."
                print "2. Explore the rest of the temple."
            
                centaur = raw_input(">>> ")
            
                if centaur == "1":
                    print "The centaur speaks. 'It is useless to try, but I daresay you can leave. Walk along the corridor where you will find an old room. I cannot tell you anymore, as I have personally never dared to go.' You ask him whether he hopes to escape too. 'Someday, child.'"
                    print "Thanking him, you walk along the corridor as he instructed you. You find a door, but it is locked. Pulling out your key, you shove it in the keyhole. To your surprise, it swings open. Carefully, you enter the room."
                    print "You spot a large cupboard that fills up an entire side of the dusty room and a set of stairs in the ground. Which do you take?"
                    print "1. You go down the set of stairs."
                    print "2. You open the cupboard cautiously."
                
                    cupboard = raw_input(">>> ")
                
                    if cupboard == "1":
                        print "You walk on and on. And on. And on. As the stairs wind ever more, you slowly spiral into insanity. The End."
                        print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                        restart = raw_input(">>> ")
        
                        if restart == "NO": 
                            break
                    elif cupboard == "2":
                        print "Scared but determined, you fling open the door. You find only a few mice... and a glinting sword! As you step into the cupboard to take it, your world starts spinning."
                        print "You end up in a musty room, with ragged curtains and two doors, #1 and #2. Which do you choose?"
                    
                        door2 = raw_input(">>> ")
                    
                        if door2 == "1":
                            print "Door 1 leads into a long but narrow corridor. As you walk further and further along it, you realise that the walls are closing in on you. Terrified, you run and run, only just making it."
                            print "Catching your breath, you spot a coffin in the middle of the room and you realise that this is home of the vampire."
                            print "You try not to wake him up, but as the lid of the coffin rises, you know that you're doomed. A ghostly, pale figure sits up and says coldly, 'Who dares awaken me from my slumber?"
                            print "His head turns slowly, to face you. You're shivering from head to toe. 'And who,' he booms, 'are you? Foul, putrid human!' His voice rises to a shout!"
                            print "The vampire gets up, and glides to you. He raises one hand and prepares to curse you. What do you do?"
                            print "1. Pull out your sword and charge at him."
                            print "2. Pull out your torch and shine it in his face."
                            print "3. Run and hide behind a nearby chest of drawers."
                        
                            vampire = raw_input(">>> ")
                        
                            if vampire == "1":
                                print "You run at the vampire confidently and push the sword in his chest. However, he pulls it out of him, laughing hysterically. 'Idiot!' he shrieks. ' I am indestructible!' He seizes you by the neck, until you start to suffocate and he holds your lifeless body. The End."
                                print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                restart = raw_input(">>> ")
        
                                if restart == "NO": 
                                    break
                            elif vampire == "2":
                                print "Hastily, you pull out your torch and shine it in his face. A look of terror crosses it and you watch him wither away to a pile of dust before your eyes. Suddenly, a door appears in the corner of the room."
                                print "You quickly open it and, to your horror, you see a hydra right in front of your eyes! Taking out your sword, you slice the hydra's heads off, one by one, with surprising ease."
                                print "However, you quickly find out that the more heads you slice off, the more heads it grows! What should you do?"
                                print "1. Run away."
                                print "2. Look for a weapon you can use."
                        
                                hydra = raw_input(">>> ")
                            
                                if hydra == "1":
                                    print "You're too slow! The hydra twists around your neck and suffocates you. The End."
                                    print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                    restart = raw_input(">>> ")
        
                                    if restart == "NO": 
                                        break
                                elif hydra == "2":
                                    print "You're too slow! The hydra twists around your neck and suffocates you. The End."
                                    print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                    restart = raw_input(">>> ")
        
                                    if restart == "NO": 
                                        break
                            
                            elif vampire == "3":
                                print "Laughing manically, the vampire sends a hex that shatters the chest of drawers into a million fragments. He then aims at you, and fires a painful curse, killing you. The End."
                                print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                restart = raw_input(">>> ")
        
                                if restart == "NO": 
                                    break
                    
                        if door2 == "2":
                            print "This leads into a rather luxurious room, with a golden gramophone and a black leather couch. You see a very old man sitting there and you wonder how long he has been there, until he speaks."
                            print "'What are you doing here?' he asks. 'Don't you know this is a dangerous house?'"
                            print "You explain your predicament to him. 'Fool. With foolish friends,' he mutters. 'There is, however, a way to escape without killing the vampire. I can make that happen. But,' he says 'I demand something in return.'"
                            print "He asks, 'Have you a sword in your possession?' You ask him how he knows about it but he laughs and says, 'Quick! Give it here and I'll let you pass!' You're unsure. You might need the sword later on. What do you do?"
                            print "1. Give him the sword."
                            print "2. Say no and hold on to it."
                        
                            sword = raw_input(">>> ")
                        
                            if sword == "1":
                                print "'Right. Well done. I suppose I ought to keep my promise then.' Suddenly, the floor starts spinning and you fall into what seems to be a vat of water. However, on further inspection you realise it is hydroflouric acid, and you wither away painfully. The End."
                                print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                restart = raw_input(">>> ")
        
                                if restart == "NO": 
                                    break
                                    
                            elif sword == "2":
                                print "'Fool!' he shouts. Suddenly, you find yourself hit by what seems to be a bolt of lightning and fall to the ground, dead. The End."
                                print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                                restart = raw_input(">>> ")
        
                                if restart == "NO": 
                                    break
                        
                if centaur == "2": 
                    print "You walk on. However, you find yourself stumbling across quicksand. It pulls you down into the depths of the temple where you suffocate. The End."
                    print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                    restart = raw_input(">>> ")
        
                    if restart == "NO": 
                        break
            else:
                print "The sphinx smiles, then leaps out at you and digs her claws into your heart. The End."
                print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
        
                restart = raw_input(">>> ")
        
                if restart == "NO": 
                    break
            
        elif sphinx == "2":
            print "You can see nothing else which will aid your escape until you spot a little trapdoor in the ground. You pull it open, heaving, and a swarm of bees fly out, stinging you all over your face until you die in horrendous pain. The End."
            print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name) 
            
        elif sphinx == "3":
            print "The sphinx smiles sickeningly at you. She leaps out and digs her claws into your heart. The End."
            print "Nice try {}, do you want to try again? If so, press any key. If not, type NO into the prompt.".format(name)
            
            restart = raw_input(">>> ")
        
            if restart == "NO": 
                break
