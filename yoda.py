#Takes user input
speech = str(input())
 
 #splits the string into a list
speech = (speech[0:].split())

#puts the first 2 words at the end of the list

if len(speech) < 3:
    print  (" ".join(speech))
else:

    speech.append (speech[0])
    speech.append (speech[1])
    speech.remove (speech[0])
    speech.remove (speech[0])
 # rejoins the list into a string with spaces
    speech =  (" ".join(speech))

    print(speech)






# I did this for fun and practice in a few minutes, I plan on making it a full fledged program that actually makes more sense.