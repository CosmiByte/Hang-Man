import requests
import random

hangman_stages = [
    
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    
    """,  # ^ base index
    
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    
    """, 
    
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    
    """, 
    
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    
    """, 
    
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    
    """, 
    
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    
    """, 
    
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    
    """
]

stage_index = 0

def display_stage():
    
    print(hangman_stages[stage_index])
    
    if stage_index == len(hangman_stages) - 1:
        
        return loser()
    
    else:
        
        return True
    
    
def next_stage():
    
    global stage_index
    
    stage_index += 1
    
    if display_stage():
        
        return True
    
    else:
        
        return False
    
    
def generate_word():
    
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    
    if response.status_code == 200:
        
        word = response.json()[0]
        
        return word
    
    else:
        
        print("Failed to generate a random word.")
        
        return None
    
    
    
def get_letter_guess(word : str):
    
    ans = input("Enter a letter to guess : ")
    
    if len(ans) == 1: 
        
        return ans
    
    else:
        
        print("Brave attempt to try and guess the word.")
        
        result = is_word_guess_correct(ans, word)
        
        if result == False:

            return False
        
        else:
            
            return
        
        
def is_word_guess_correct(word : str, gen_word : str):
    
    if word == gen_word:
        
        winner()
        
        return False
    

def is_guess_char_in_word(letter : chr, unfilled_pallet : list, word_char_list : list):
        
    if letter in word_char_list:
        
        print("Correct guess.")
        
        being_filled = replace_space_with_char(letter, unfilled_pallet, word_char_list)
        
        print(being_filled)
        
        try:
            
            being_filled.index('_')
            
        except:
            
            winner()
        
        else:    
            
            return True

    else:
        
        print("Incorrect guess.")
        
        result = next_stage()
        
        if result:
            
            return True
        
        else:
             
            return False # ISSUE
        
    
def replace_space_with_char(char, list_of_unfilled, word_list):
    
    for i, letter in enumerate(word_list):
        
        if letter == char:
            
            list_of_unfilled[i] = char
            
    return list_of_unfilled


def winner():
    
    print("Congratulations for guessing the correct word, here is your award.. 🏆")
    return False


def loser():
    
    print("Unfortunately you have failed, and the man has now been hanged.. 💀")
    return False

    
def main():
    
    progresser = True
    
    word = generate_word()
    
    print(word)
    
    word_letters = list(word)
        
    unfilled_pallet = ['_' for _ in range(len(word_letters))]
        
    while progresser == True:
        
        character = get_letter_guess(word)
        
        if character == False:
            
            progresser = False
            
        else:
            
            result = is_guess_char_in_word(character, unfilled_pallet, word_letters)
            
            if result is False:
                
                progresser = False
            
            

    
if __name__ == "__main__":
    
    main()
