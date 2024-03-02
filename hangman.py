import random

board = ['

Hangman

+---+
   
     
     
     
     
=========''', '

+---+
   
o   
     
     
     
=========''', '

+---+
   
o    
    
     
     
=========''', '

+---+
   
o    
    
     
     
=========''', '

 +--+
   
 o    
   
     
         
=========''', '

  +--+
     
 o    
 
     
         
=========''', '

 +--+
     
 o    
 
        
         
=========''', '

 +--+
     
 o    
 
     
          
=========''', '

class Hangman
def__init__(self,word)
         self.word = word
         self.missed_letters = []
         self.guessed_letters = []

def guess(self,letters)
         if letters in self.word and letter not in self.
         guessed_letters
         self.guessed_letters.append(letter)
         eilf letter not in self.word and letter not in self.missed_letters.append(letter)
         else
         return False
         return True

def hangman_over(self)
         return self.hangman_won() or (len(self.missed_letters) == 6)

         def hangman_over(self)
         if'_' not in self.hide_word()
         return True
         return False

         def hide_word(self)
         rtn = 
         for letter not in self.guessed_letters
         rtn += '_'
         else
         rtn += letter
         return rtn

         def print_game_status(self)
         print (board[len(self.missed_letter)])
         print ('Word ' + self.hide_word())
         print (Letters Missed ',)
                for letter in self.missed_letters
                print(letter,)
                print ()
                print ('Letters Guessed ',)
                for letter in self.guessed_letters
                print(letter,)
                print ()

def rand_word()                
    
