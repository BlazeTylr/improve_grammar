def improve_grammar(sentence):
    punctuation_marks = ['!', '.', '?']
    
    if sentence[0].isupper() and sentence[:-1] not in 		punctuation_marks:
        return "Your sentence doesn't end with a correct punctuation mark."
    return "Your sentence doesn't start with an uppercase letter"
    
improve_grammar('Hello there@')