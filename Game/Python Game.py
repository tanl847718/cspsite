input=raw_input
def intro():
  print ("Welcome to the trivia game!")
  print ("Which category would you like to play?")
  print ("Press a for art, m for music theory, and l for language")
  levelselect= input()
  if levelselect==("a"):
    arttrivia()
  elif levelselect==("m"):
    musictheorytrivia()
  else:
    languagetrivia()

def levelselect():
  print ("Which category would you like to play next?")
  print ("Press a for art, m for music, and l for language")
  levelselect= input()
  if levelselect==("a"):
    arttrivia()
  elif levelselect==("m"):
    musictheorytrivia()
  else:
    languagetrivia()



def arttrivia():
  print ("Welcome to the art category of the game!")
  aq1=("Who painted 'Girl with a Pearl Earring?")
  aq2=("Who painted American Gothic?")
  aq3=("Who painted The Great Wave off Kanagawa?")
  aq4=("Who painted The Persistance of Time?")
  aq5=("Who painted The Son of Man?")

  options1= ("a. Vermeer\nb. Dali\nc. Van Gogh\nd. Seurat")
  options2= ("a. Vermeer\nb. Wood\nc. Klimt\nd. Hopper")
  options3= ("a. Klimt\nb. Kuniyoshi\nc. Seurat\nd. Hokusai")
  options4= ("a. Dali\nb. Hopper\nc. Wood\nd. Van Gogh")
  options5= ("a. Whistler\nb. Wood\nc. Magritte\nd. Klimt")
  score=0
  
  print (aq1)
  print (options1)
  response=input("Press the letter of the answer you think is correct\n")
  if response=="a":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/1")
  else:
    print("The correct answer is a")
    score=score+0
    print ("Your score is", score,"/1")
  
  
  print (aq2)
  print (options2)
  response=input("Press the letter of the answer you think is correct\n")
  if response=="b":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/2")
  else:
    print("The correct answer is b")
    score=score+0
    print ("Your score is", score,"/2")

  print (aq3)
  print (options3)
  response=input("Press the letter of the answer you think is correct\n")
  if response=="d":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/3")
  else:
    print("The correct answer is d")
    score=score+0
    print ("Your score is", score,"/3")

  print (aq4)
  print (options4)
  response=input("Press the letter of the answer you think is correct\n")
  if response=="a":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/4")
  else:
    print("The correct answer is a")
    score=score+0
    print ("Your score is", score,"/4")

  print (aq5)
  print (options5)
  response=input("Press the letter of the answer you think is correct\n")
  if response=="c":
    print ("Correct!")
    score=score+1
    if (score==5):
      print ("Good job on a perfect 5/5!")
    else: 
      print("Your score is", score,"/5")
  else:
    print("The correct answer is c")
    score=score+0
    print ("Your final score is", score,"/5")  
  levelselect()


def musictheorytrivia():
  print ("Welcome to the music category of the game!")
  mq1=("Who composed Ode to Joy?")
  mq2=("How many notes are in a scale?")
  mq3=("Which time period was Chopin from?")
  mq4=("Which of these composers was from the contemporary period?")
  mq5=("Which of these triads is a B Major triad?")

  options1= ("a. Mozart\nb. Liszt\nc. Beethoven\nd. Clementi")
  options2= ("a. 8\nb. 7\nc. 10\nd. 12")
  options3= ("a. Impressionism\nb. Romantic\nc. Classical\nd. Baroque")
  options4= ("a. Scarlatti\nb. Handel\nc. Gershwin\nd. Clementi")
  options5= ("a. B, D, F#\nb. B, D#, F#\nc. B, D, F\nd. B#, D#, C#")
  score=0
  
  print (mq1)
  print (options1)
  response=input("Press the letter of the answer you think is correct\n")
  if response=="c":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/1")
  else:
    print("The correct answer is c")
    score=score+0
    print ("Your score is", score,"/1")
  
  
  print (mq2)
  print (options2)
  response=input("Press the letter of the answer you think is correct\n")
  if response=="a":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/2")
  else:
    print("The correct answer is a")
    score=score+0
    print ("Your score is", score,"/2")

  print (mq3)
  print (options3)
  response=input("Press the letter of the answer you think is correct\n")
  if response=="b":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/3")
  else:
    print("The correct answer is b")
    score=score+0
    print ("Your score is", score,"/3")

  print (mq4)
  print (options4)
  response=input("Press the letter of the answer you think is correct\n")
  if response=="c":
    print ("Correct!")
    score=score+1
    print ("Your score is", score,"/4")
  else:
    print("The correct answer is c")
    score=score+0
    print ("Your score is", score,"/4")

  print (mq5)
  print (options5)
  response=input("Press the letter of the answer you think is correct\n")
  if response=="b":
    print ("Correct!")
    score=score+1
    if (score==5):
      print ("Good job on a perfect 5/5!")
    else: 
      print("Your score is", score,"/5")
  else:
    print("The correct answer is b")
    score=score+0
    print ("Your final score is", score,"/5")  
  levelselect()



def languagetrivia():
  score=0
  print("Welcome to the language category of the game!")
  response=input("How do you say airport in Spanish?")
  if(response=='aeropuerto' or response=='Aeropuerto'):
    print ("Correct!")
    score= score+1
    print("Your score is", score,"/1")
  else:
    print("The correct answer is 'aeropuerto'\nYour score is",score,"/1")

  response=input("How do you say hello in Italian?")
  if(response=='ciao' or response=='Ciao'):
    print ("Correct!")
    score= score+1
    print("Your score is", score,"/2")
  else:
    print("The correct answer is 'ciao'\nYour score is",score,"/2") 
  
  response=input("How do you say bread in French?")
  if(response=='pain' or response=='Pain'):
    print ("Correct!")
    score= score+1
    print("Your score is", score,"/3")
  else:
    print("The correct answer is 'pain'\nYour score is",score,"/3") 
     
  response=input("How do you say apple in Spanish?")
  if(response=='manzana' or response=='Manzana'):
    print ("Correct!")
    score= score+1
    print("Your score is", score,"/4")
  else:
    print("The correct answer is 'manzana'\nYour score is",score,"/4")

  response=input("How do you say good morning in German?")
  if(response=='guten morgen' or response=='Guten morgen' or response=='Guten Morgen'):
    print ("Correct!")
    score= score+1
    if(score==5):
      print("Good job on a perfect 5/5!")
    else:
      print("Your score is", score,"/5")
  else:
    print("The correct answer is 'guten morgen'\nYour score is",score,"/5")
  levelselect()

  

   

  
  

  levelselect()






intro()

