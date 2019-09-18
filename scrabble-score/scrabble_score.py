def score(word):
    # hardcoded scores to letters
    scrabble_scores_to_letters = {
            "1":['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
            "2":['D', 'G'],
            "3":['B', 'C', 'M', 'P'],
            "4":['F', 'H', 'V', 'W', 'Y'],
            "5":['K'],
            "8":['J', 'X'],
            "10":['Q', 'Z']}
    
    # Create a dictionary of letters to scores
    scrabble_letters_to_scores = {}
    
    for score_value in scrabble_scores_to_letters.keys():
        letters_of_the_score = scrabble_scores_to_letters[score_value]
        
        for letter in letters_of_the_score:
            letter_score = {letter: int(score_value)}
            scrabble_letters_to_scores.update(letter_score)
    
    # Set word to uppercase
    word = word.upper()
    
    # Calculate the total score from "scrabble_letters_to_score"
    total_scrabble_score = sum([scrabble_letters_to_scores[letter] for letter in word])
    
    return total_scrabble_score
                               
    