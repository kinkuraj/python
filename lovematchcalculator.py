#Both first names have the same numbers of letters.			+20 pts
#Both first names start with a vowel.						+10 pts
#Both first names start with a consonant.					+5 pts
#Both first names have the same number of vowels.			+12 pts
#Both first names have the same number of consonants.		+12 pts
#Both first names contain at least a “l”, “o”, “v” or “e”.	+7 pts

#score * 0.66

#Love Match Calculator 
print("*****************************")  
print("*   Love Match Calculator   *")  
print("*****************************")  
  
#Retrieve User Inputs  
name1=input("Type a firstname:")  
name2=input("Type another firstname:")  
name1=name1.lower()  
name2=name2.lower()  
  
#Initialise key variables  
score=0  
vowels=["a","e","i","o","u","y"]  
consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]  
vowelsInName1=0  
vowelsInName2=0  
consInName1=0  
consInName2=0 
vowelsexistname1 = False
vowelsexistname2 = False
#Check if both names have the same number of characters  
if len(name1)==len(name2):  
  score = score + 20  
  
#Check if both names start with a vowel  
if (name1[0] in vowels) and (name2[0] in vowels):  
    score = score + 10  
  
#Check if both names start with a vowel  
if (name1[0] in consonants) and (name2[0] in consonants):  
    score = score + 5

for x in vowels:
  if x in name1:
    vowelsInName1 +=1
    vowelsexistname1 = True
  
  if x in name2:
    vowelsInName2 +=1
    vowelsexistname2 = True

for x in consonants:
  if x in name1:
    consInName1 +=1
  
  if x in name2:
    consInName2 +=1
    
if consInName1 == consInName2:
  score = score + 12


if vowelsInName1 == vowelsInName2:
  score = score + 12

#Complete code here to implement all criteria
if vowelsexistname1 == vowelsexistname2:
  score +=7
     

#Display final love match score  
print("Your love match score is: " + str(score*0.66))
