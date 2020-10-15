import random 
beginner=['home','smile','angry','stop','good'] 
intermediate=['computer','invertor','hangman','pathetic','slippery'] 
advance=['awkward','networking','success','syndrome','pneumonia'] 
print('Welcome! to the world of Hangman') 
name=input('Your Good Name? ') 
print(f'Hey {name} lets Start')

a=[''' 
---------- 
| 0 
| 
| 
| 
---- 
''', 
''' 
---------- 
| 0 
| | 
| | 
| 
---- 
'''] 
c=[''' 
---------- 
| 0 
| |\ 
| | 
| 
---- 
'''] 
d=[''' 
----------- 
| 0 
| /|\ 
| | 
| 
---- 
'''] 
e=['''
 
------------ 
| 0 
| /|\ 
| | 
| / 
---- 
'''] 
 
f=[''' 
------------ 
| 0 
| /|\ 
| | 
| / \ 
---- 
'''] 
hanglist=[a[0],a[1],c[0],d[0],e[0],f[0]] #list of step by step hanging 
def hang_algo(level) : 
	print('Level 1') 
	print('You have total 6 trials') 
	
	word=random.choice(level) #will choose randomly any word from given list 
	turns=6 #initialise turns to 6 
	guesses=' ' #sring concaneted of char choosen by player 
	print("Guess a character ") 

	while turns > 0 : 
		failure=0 #to print '_' 
		for char in word : 
			if char in guesses : #if char is in guesses then print that char 
				print(char,end=' ') 
			else : 
				print('_',end=' ') #else print _ on that place 
				failure += 1 
		if failure==0 : #if all char persent in gueeses then print winner 
			print('\nWinner Winner Chicken Dinner!') 
			print('The Word is : ',word) 
			break 
		print('')
		while True : #this loop is for player to choose only one char at atime 
			guess=input("Guess a character ") #take i/p from player 
			if len(guess)==1 : 
				guesses+=guess 
				break 
			else : 
				print('Please enter one char at a time') 
		if guess not in word : 
			print('Wrong char') 
			print(hanglist[-(turns)]) 
			turns-=1 
			print('Your remaining turns are ',turns) 
				
		if turns==0 : 
			print('\nBetter Luck Next time\n') 
				
ans=input('Ready? (y/n) ') 
while ans=='y' : 
	cho=int(input('Select Difficulty level \n1.Begginer \n2.Intermediate \n3.Advance\n')) 
	if cho==1 : 
		hang_algo(beginner) 
	elif cho==2 : 
		hang_algo(intermediate) 
	elif cho==3 : 
		hang_algo(advance) 
	ans=input('Do You Want to continue(y/n) ')

#output
/*


C:\Users\TECHNICAL KD\Downloads>python test.py
Welcome! to the world of Hangman
Your Good Name? kiran
Hey kiran lets Start
Ready? (y/n) y
Select Difficulty level
1.Begginer
2.Intermediate
3.Advance
1
Level 1
You have total 6 trials
Guess a character
_ _ _ _ _
Guess a character s
Wrong char

----------
| 0
|
|
|
----

Your remaining turns are  5
_ _ _ _ _
Guess a character a
a _ _ _ _
Guess a character n
a n _ _ _
Guess a character g
a n g _ _
Guess a character e
Wrong char

----------
| 0
| |
| |
|
----

Your remaining turns are  4
a n g _ _
Guess a character r
a n g r _
Guess a character y
a n g r y
Winner Winner Chicken Dinner!
The Word is :  angry
Do You Want to continue(y/n) y
Select Difficulty level
1.Begginer
2.Intermediate
3.Advance
2
Level 1
You have total 6 trials
Guess a character
_ _ _ _ _ _ _ _
Guess a character s
Wrong char

----------
| 0
|
|
|
----

Your remaining turns are  5
_ _ _ _ _ _ _ _
Guess a character u
Wrong char

----------
| 0
| |
| |
|
----

Your remaining turns are  4
_ _ _ _ _ _ _ _
Guess a character h
_ _ _ h _ _ _ _
Guess a character a
_ a _ h _ _ _ _
Guess a character n
Wrong char

----------
| 0
| |\
| |
|
----

Your remaining turns are  3
_ a _ h _ _ _ _
Guess a character p
p a _ h _ _ _ _
Guess a character e
p a _ h e _ _ _
Guess a character t
p a t h e t _ _
Guess a character i
p a t h e t i _
Guess a character c
p a t h e t i c
Winner Winner Chicken Dinner!
The Word is :  pathetic
Do You Want to continue(y/n) y
Select Difficulty level
1.Begginer
2.Intermediate
3.Advance
3
Level 1
You have total 6 trials
Guess a character
_ _ _ _ _ _ _
Guess a character s
s _ _ _ _ s s
Guess a character u
s u _ _ _ s s
Guess a character e
s u _ _ e s s
Guess a character s
s u _ _ e s s
Guess a character s
s u _ _ e s s
Guess a character c
s u c c e s s
Winner Winner Chicken Dinner!
The Word is :  success
Do You Want to continue(y/n)
*/