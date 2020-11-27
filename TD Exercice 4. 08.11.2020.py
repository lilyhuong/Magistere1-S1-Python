#PART I

#exercice 1
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
i = 0  #créer une value départ pour i
while i < len(week): #quand  indice i < taille de la liste (week), ici taille (week) = 7
    if week[i] == "Friday":  #si value i est "Friday"
        print ("Cool ! It's Friday" ) #on print "Cool......"
    elif i > 4:  #ou si  indice i > 4 (ça peut dire que value i est "Saturday" ou "Sunday")
        print ("Week-end, it's party time!") #afficher
    else: #ou le reste =  le denier cas
        print ( "Go to work")
    i += 1 #i = i + 1

#Exercice 2
alphabet =  ["A", "B", "B", "C", "A", "B", "A", "C"]
i = 0 
Replace = [] # on crée une nouvelle liste vide
while i < len(alphabet): #quand indice i < talle de la liste alphabet (taille = 8)
    if alphabet[i] == "A": #si value i est A
        Replace.append("X") #la nouvelle liste Replace ajoute un nouveau élément X
    elif alphabet[i] == "B": #ou si value i est B
        Replace.append("Y") #la liste Replace ajoute "Y"
    else: #denier cas
        Replace.append("Z")
    i += 1
print ("The new list is: " , Replace) 

#Exercice 3
number = [1, 6, 9, 78, -16]
i = 0 #on crée une value départ pour i = 0
min = number[i] #on fait une hypothèse que minnimum of list number est le premier élément
while i < len(number): #quand indice i < taille de la liste number = 5 
    if number[i] < min: #si value of i < min (value d'hypothese)
        min = number[i] #maintement, le minimum de la liste number est value i
    i += 1
print ("Minimum of this list is: " , min)

#Exercice 4
note = [14, 9, 13, 15, 12]
i = 0
min = note[i] #on fait une hypothèse  1 que minnimum of list number est le premier élément
max = note[i] #on fait l'autre hypothèse (2) que maximum of list number est aussi le premier élément
sum = 0 #on suppose que la somme des notes = 0
while i < len(note):
    if note[i] < min :
        min = note[i]
    elif note[i] > max: #si value of i > max (value d'hypothese 2)
        max = note[i] #maintement, le maximum de la liste number est value i
    sum += note[i] #somme = somme + la value i
    i += 1
print ("The minimum grade is ", min)
print ("The maximum grade is ", max)
average = sum/len(note) #créer une nouvelle variable permet calculer la note moyenne
if average >= 14: #si la note moyenne est >= 14
    print ("The average of grades is ", average, " Mention: Very good ")
elif average >= 10 and average < 12: #ou si 
    print ("The average of grades is ", average, " Mention: Faire ")
elif average < 10:
    print ("The average of grades is ", average, " Mention:  ")
else: #le reste
    print ("The average of grades is ", average, " Mention: Good ")


#Exercice 5
i = 0
even = [] #on crée une liste  vide
odd = [] #on crée une liste  vide
while i < 21:
    if i % 2 == 0 and i <= 10: #si le reste de (i/ 2 ) = 0 (par example 19 / 2 = 9 (+ 1), le rest de (i/2) ici égale à 1), et i < = 10
        even.append(i) #on ajoute i à liste even
    elif i % 2 == 1 and i > 10: # ou si le reste de (i/ 2 ) = 1
        odd.append(i)
    i += 1
print(even)
print(odd)

#Exercice 6
Syracuse = []
number = int(input("Give me a positive integer! "))
Syracuse = [number] #le premier élément de la liste Syracuse est number
i = 0 
while Syracuse[i] != 1: #quand la value i est différent à 1 (autrement dit, la fonction while va s'arrete quand la value i = 1)
    if Syracuse[i] % 2 == 0:
        Syracuse.append(int(Syracuse[i]/2))
    if Syracuse[i] % 2 == 1:
        Syracuse.append (int(Syracuse[i] * 3 + 1))
    i += 1
print(Syracuse)


#PART II

#Exercice 1
import math #on exporte la biblothèque "math"
for x in range(10, 21):
    print(math.sqrt(x)) #on utilise la function sqrt(x) = square root of x dans la bibliothèque math

#Exercice 2
import math
print(math.cos(math.pi/2)) 
#math.cos() = Renvoie le cosinus d'un nombre
#math.pi = Renvoie PI (3.1415 ...)

#Exercice 3
import time
for i in range (1, 11):
    print(i)
    time.sleep(1)
    i += 1
#time.sleep(x) = vous pouvez utiliser pour suspendre l'exécution du thread appelant pendant le nombre de secondes x que vous spécifiez.

#Exercice 4
import random
n = 20
print(''.join(["{}".format(random.randint(1,4)) for number in range(0,20)]))
#random.randint(1, 4)  = Renvoie un nombre aléatoire entre 1 et 4, ici (1, 2, 3, 4)

#Exercice 5
import datetime
x = datetime.datetime(2002, 6, 21)
print("The day of the week when you were born:  ", x.strftime("%A"))
#datetime.datetime = créer votre date sur la forme: year, month, day
# %A = Affichez le nom du jour