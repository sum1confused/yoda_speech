speech = str(input())
 
speech = (speech[0:].split())


speech.append (speech[0])
speech.append (speech[1])
speech.remove (speech[0])
speech.remove (speech[0])




speech =  (" ".join(speech))

print(speech)