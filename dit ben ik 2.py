print("mijn naam is Adnan Rajeh ik ben naar nederland gevlucht \nhoe ben ik gevlucht? \nA met de boot \nB met vliegtuig? \nKies je antwoord:")
gevlucht = input("-")
if gevlucht == "A" or gevlucht == "a" or gevlucht == " a" or gevlucht == " A":
    print("Mijn vader is met de boot naar Nederland gevlucht \nsinds wanneer is mijn vader hier? \nA 5jaar \nB 6jaar \nkies je antwoord:")
    jaren = input("-")
    if jaren == "A" or jaren == "a" or jaren == " a" or jaren == " A":
        print("Ik ben hier al 5 jaren in Nederland \nhoe zo spreek ik goed Nederlands? \nA Van straat \nB door school? \n kies je antwoord:")
        taal = input("-")

        if taal == "A" or taal == "a" or taal == " a" or taal == " A":
            print("Ik heb veel vrienden ontoemt op straat en dat heeft mijn ook geholpen met nederland leren \nWaar komen mijn vrienden vandaan? \nA Nederlands  \nB Turkije? \n kies je antwoord:")
            vandaan = input("-")

            if vandaan == "A" or vandaan == "a" or vandaan == " a" or vandaan == " A":
                print("nicen die waren mijn vragen voor vandaag \nBedankt (:")
            elif vandaan == "B" or vandaan == "b" or vandaan == " b" or vandaan == " B":
                print("nicen die waren mijn vragen voor vandaag \nBedankt (:")


        elif taal == "B" or taal == "b" or taal == " B" or taal == " b":
            print("ja dat klopt, ik heb ook veel vrienden \nWaar komen mijn vrienden vandaan? \nA Nederlands  \nB Turkije? \n kies je antwoord:")
            vandaan2 = input("_")
            if vandaan2 == "B" or vandaan == "b" or vandaan == " b" or vandaan == " B":
                print("nicen die waren mijn vragen voor vandaag \nBedankt (:")
            else:
                print("nicen die waren mijn vragen voor vandaag \nBedankt (:")


    elif jaren == "B" or jaren == "b" or jaren == " b" or jaren == " B":
        print("Mijn vader hij is al 6 jaren in Nederland. \n spreekt hij goed Nederlands? \nA nee \nB ja")
        spreekt = input("-")
        if spreekt == "A" or spreekt == "a" or spreekt == " A" or spreekt == " a":
            print("nicen die waren mijn vragen voor vandaag \nBedankt (:")
        elif spreekt == "B" or spreekt == "b" or spreekt == " B" or spreekt == " b":
            print("nicen die waren mijn vragen voor vandaag \nBedankt (:")

elif gevlucht == "B" or gevlucht == "b" or gevlucht == " b" or gevlucht == " B":
    print("Ik ben met de vliegtuig hier naar Nederland gekomen \n met welke airline ben ik gekomen? \nA KLM \nB Turksh airline \nkies je antwoord:")
    airline = input("-")
    if airline == "B" or airline == "b" or airline == " b" or airline == " B":
        print("ik ben wel met de turks airline hier gekomen")
        print("Was het zomer of winter toen ik hier kwam \nA zomer \nB winter \nkies je antwoord:")
        zomerwinter = input("-")
        if zomerwinter == "B" or zomerwinter == "b" or zomerwinter == " b" or zomerwinter == " B":
            print("Goed zo, die waren mijn vrage nvoor vandaag, \nBedankt (:")
        elif zomerwinter == "A" or zomerwinter == "a" or zomerwinter == " A" or zomerwinter == " a":
            print("Goed zo, die waren mijn vrage nvoor vandaag, \nBedankt (:")
    elif airline == "A" or airline == "a" or airline == " a" or airline == " A":
        print("nicen die waren mijn vragen voor vandaag \nBedankt (:")
