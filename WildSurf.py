import Firebase
exit = 'no'
listofPossibleAnimals=[]
listofPossiblePlants = []
plantsArray = []
otherLst = []
outputList = []
outputFacts = []
allList = []
uniqueList = []
while True:
    firstQuestion = input("Did you see a plant or an animal? ")
    shapeVal = ""
    colorVal = ""
    poisonVal = ""
    categoryVal = ""
    
    # colorAnimalVal = ""
    # attributeAnimalVal = ""
    # sizeAnimalVal = ""
    # threatAnimalVal = ""
    # tailAnimalVal = ""
    # wingAnimalVal = ""

    if firstQuestion == "plant":
        listofPossiblePlants = Firebase.plantLstDict
        color = input("What color is the plant? ")
        for dictionary in listofPossiblePlants:
            listOfColors = dictionary['Color']
            for colorD in listOfColors:
                
                if(color == colorD):
                    outputList.append(dictionary)
                    colorVal = colorD
        listofPossiblePlants = outputList
        outputList = []
        
        shape = input("What is the shape? ")
        for dictionary in listofPossiblePlants:
            listOfShape = dictionary['Shape']
            for shapeD in listOfShape:
                if(shape == shapeD):
                    outputList.append(dictionary)
                    shapeVal = shapeD
        listofPossiblePlants = outputList
        outputList = []
        
        for dictionary in listofPossiblePlants:
            listOfPoison = dictionary['Poisonous']
            for poisonD in listOfPoison:
                poisonVal = poisonD

        category = input("What is the category of the specimen (berry, flower, plant)? ")
        for dictionary in listofPossiblePlants:
            listOfCategories = dictionary['Category']
            for categoryD in listOfCategories:
                if(category == categoryD):
                    outputList.append(dictionary)
                    categoryVal = categoryD
        listofPossiblePlants = outputList
        outputList = []
        print("\n")

        if len(listofPossiblePlants)==1:
            finalGuess = listofPossiblePlants[0]['name']
            print("The plant you spotted may potentially be " + finalGuess + ".")
            print("Some characteristics of " + finalGuess + " include: ")
            # for dictionary in listofPossiblePlants:
            #     outputFacts.append(dictionary)
            print("- Usually has a " + shapeVal + " shape.")
            print("- Usually found in the color " + colorVal + ".")
            if poisonVal == "yes":
                print("- Considered a poisonous type of " + categoryVal + ".")
            elif poisonVal == "no":
                print("- Considered a non-poisonous type of " + categoryVal + ".")
            print('\n')
            exit = input("Would you like to describe another plant or animal?")
            if exit == "yes":
                continue
            elif exit == "no":
                break
        elif len(listofPossiblePlants)==0:
            print("Could not match with a " + category + " in our database")
            exit = input("Want to describe another plant or animal?")
            if exit=='yes' or exit =='sure':
                continue
            elif exit=='no':
                break

    if firstQuestion == "animal":
        listofPossibleAnimals = Firebase.animalLstDict
        color = input("What color is the animal? ")
        for dictionary in listofPossibleAnimals:
            lst = dictionary['color']
            if color in lst:
                otherLst.append(dictionary)
        listofPossibleAnimals = otherLst
        otherLst = []
        tails = input("Does it have a tail, yes or no?: ")
        if tails == 'yes':
            tail = input("Is the tail long or short?: ")
            for dictionary in listofPossibleAnimals:
                lst = dictionary['physical attribute']
                if tail == 'short':
                    if 'short tail' in lst:
                        otherLst.append(dictionary)
                elif tail == 'long':
                    if 'long tail' in lst:
                        otherLst.append(dictionary)
        elif tails == 'no':
            for i in range(len(listofPossibleAnimals)):
                lst = listofPossibleAnimals[i]['physical attribute']
                if 'long tail ' not in lst and 'short tail' not in lst:
                    otherLst.append(listofPossibleAnimals[i])
        listofPossibleAnimals = otherLst
        otherLst = []
        wings = input("Does your animal have wings? ")
        if wings == 'yes':
            for dictionary in listofPossibleAnimals:
                lst = dictionary['physical attribute']
                if 'wings' in lst:
                    otherLst.append(dictionary)
        elif wings == 'no':
            for dictionary in listofPossibleAnimals:
                lst = dictionary['physical attribute']
                if 'wings' not in lst:
                    otherLst.append(dictionary)
        listofPossibleAnimals = otherLst
        otherLst = []
        size = input("What is the size of the animal: big, small, medium? ")
        if size == 'big':
            for dictionary in listofPossibleAnimals:
                lst = dictionary['size']
                if 'big' in lst:
                    otherLst.append(dictionary)
        elif size == 'small':
            for dictionary in listofPossibleAnimals:
                lst = dictionary['size']
                if 'small' in lst:
                    otherLst.append(dictionary)
        elif size == 'medium':
            for dictionary in listofPossibleAnimals:
                lst = dictionary['size']
                if 'medium' in lst:
                    otherLst.append(dictionary)
        listofPossibleAnimals = otherLst
        otherLst = []
        # Finished general questions
        if len(listofPossibleAnimals) == 1:
            WildSurfGUI.py
            finalGuess = listofPossibleAnimals[0]['name']
            print("You might have seen a " + finalGuess)
            import WildSurfGUI
            exit = input("Want to describe another plant or animal?")
            if exit == 'yes':
                continue
            elif exit == 'no':
                break
        elif len(listofPossibleAnimals) == 0:
            print("Could not match with an animal in our database")
            exit = input("Want to describe another plant or animal?")
            if exit == 'yes':
                continue
            elif exit == 'no':
                break
        # take out this if statement when we implement while loop
        otherLst = []
        beak = input("Does the animal have a beak?: ")
        if beak == 'yes':
            beakLength = input("Is the beak short or long?: ")
            if beakLength == 'long':
                for i in range(len(listofPossibleAnimals)):
                    beakL = listofPossibleAnimals[i]['physical attribute']
                    if 'long beak ' in beakL:
                        otherLst.append(listofPossibleAnimals[i])
            elif beakLength == 'short':
                for i in range(len(listofPossibleAnimals)):
                    beakL = listofPossibleAnimals[i]['physical attribute']
                    if 'short beak' in beakL:
                        otherLst.append(listofPossibleAnimals[i])
        elif beak == 'no':
            for dictionary in listofPossibleAnimals:
                if 'long beak' not in dictionary['physical attribute'] and 'short beak' not in dictionary[
                    'physical attribute']:
                    otherLst.append(dictionary)
        listofPossibleAnimals = otherLst
        otherLst = []
        hair = input("Does the animal have fur, feathers, or hairless: ")
        if hair == 'fur':
            for dictionary in listofPossibleAnimals:
                attributeList = dictionary['physical attribute']
                if hair in attributeList:
                    otherLst.append(dictionary)
            listofPossibleAnimals = otherLst
            otherLst = []
            pattern = input("What pattern is on its fur (spotted, smooth, striped): ")
            if pattern == 'spotted':
                for dictionary in listofPossibleAnimals:
                    attributeList = dictionary['physical attribute']
                    if 'spotted' in attributeList:
                        otherLst.append(dictionary)
            elif pattern == 'striped':
                for dictionary in listofPossibleAnimals:
                    attributeList = dictionary['physical attribute']
                    if 'striped' in attributeList:
                        otherLst.append(dictionary)
            elif pattern == 'smooth':
                for dictionary in listofPossibleAnimals:
                    attributeList = dictionary['physical attribute']
                    if 'smooth' in attributeList:
                        otherLst.append(dictionary)
        elif hair == 'feathers':
            for dictionary in listofPossibleAnimals:
                attributeList = dictionary['physical attribute']
                if hair in attributeList:
                    otherLst.append(dictionary)
            listofPossibleAnimals = otherLst
            otherLst = []
            pattern = input("What pattern is on its feathers (spotted, smooth, striped): ")
            if pattern == 'spotted':
                for dictionary in listofPossibleAnimals:
                    attributeList = dictionary['physical attribute']
                    if 'spotted' in attributeList:
                        otherLst.append(dictionary)
            elif pattern == 'striped':
                for dictionary in listofPossibleAnimals:
                    attributeList = dictionary['physical attribute']
                    if 'striped' in attributeList:
                        otherLst.append(dictionary)
            elif pattern == 'smooth':
                for dictionary in listofPossibleAnimals:
                    attributeList = dictionary['physical attribute']
                    if 'smooth' in attributeList:
                        otherLst.append(dictionary)
        elif hair == 'hairless':
            for dictionary in listofPossibleAnimals:
                attributeList = dictionary['physical attribute']
                if hair in attributeList:
                    otherLst.append(dictionary)
            listofPossibleAnimals = otherLst
            otherLst = []
            pattern = input("What pattern is on its skin (spotted, smooth, striped): ")
            if pattern == 'spotted':
                for dictionary in listofPossibleAnimals:
                    attributeList = dictionary['physical attribute']
                    if 'spotted' in attributeList:
                        otherLst.append(dictionary)
            elif pattern == 'striped':
                for dictionary in listofPossibleAnimals:
                    attributeList = dictionary['physical attribute']
                    if 'striped' in attributeList:
                        otherLst.append(dictionary)
            elif pattern == 'smooth':
                for dictionary in listofPossibleAnimals:
                    attributeList = dictionary['physical attribute']
                    if 'smooth' in attributeList:
                        otherLst.append(dictionary)
        listofPossibleAnimals = otherLst
        otherLst = []
        if len(listofPossibleAnimals) == 1:
            WildSurfGUI.py
            finalGuess = listofPossibleAnimals[0]['name']
            print("\nYou might have seen a " + finalGuess + '\n')
            import WildSurfGUI
            exit = input("Want to describe another plant or animal?")
            if exit == 'yes':
                continue
            elif exit == 'no':
                break
        elif len(listofPossibleAnimals) == 0:
            print("Could not match with an animal in our database")
            exit = input("Want to describe another plant or animal?")
            if exit == 'yes':
                continue
            elif exit == 'no':
                break
        if len(listofPossibleAnimals) > 1:
            antlers = input("Does the animal have antlers?: ")
            if antlers == 'yes':
                for dictionary in listofPossibleAnimals:
                    if 'antlers' in dictionary['physical attribute']:
                        otherLst.append(dictionary)
            elif antlers == 'no':
                for dictionary in listofPossibleAnimals:
                    if 'antlers' not in dictionary['physical attribute']:
                        otherLst.append(dictionary)
            listofPossibleAnimals = otherLst
            otherLst = []
            ears = input("Does the animal have short ears, long ears, or medium ears?: ")
            if ears == 'short':
                for dictionary in listofPossibleAnimals:
                    if 'short ears' in dictionary['physical attribute']:
                        otherLst.append(dictionary)
            elif ears == 'long':
                for dictionary in listofPossibleAnimals:
                    if 'long ears' not in dictionary['physical attribute']:
                        otherLst.append(dictionary)
            elif ears == 'medium':
                for dictionary in listofPossibleAnimals:
                    if 'medium ears' not in dictionary['physical attribute']:
                        otherLst.append(dictionary)
            listofPossibleAnimals = otherLst
            otherLst = []
            if len(listofPossibleAnimals)==1:
                finalGuess = listofPossibleAnimals[0]['name']
                print("\nYou might have seen a " + finalGuess + '\n')
                import WildSurfGUI
                exit = input("Want to describe another plant or animal?")
                if exit == 'yes':
                    continue
                elif exit == 'no':
                    break
            elif len(listofPossibleAnimals)==0:
                print("Could not match with an animal in our database")
                exit = input("Want to describe another plant or animal?")
                if exit == 'yes':
                    continue
                elif exit == 'no':
                    break
            elif len(listofPossibleAnimals)>1:
                print("\nCould not narrow down the list, here is the list of animals you could have possibly seen: \n")
                for dictionary in listofPossibleAnimals:
                    print(dictionary['name'] + '\n')
                import WildSurfGUI
                exit = input("Want to describe another plant or animal?")
                if exit == 'yes':
                    continue
                elif exit == 'no':
                    break