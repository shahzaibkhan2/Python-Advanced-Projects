# Import pyasell module which is a Python's Library
import pyaspell

# Function to correct spellings
def correct_spelling(word):
    checker = pyaspell.Speller()
    suggestions = checker.suggest(word)
    if suggestions:
        return suggestions[0]
    else:
        return word

# Function for spelling check
def spell_check_text(text):
    words = text.split()
    corrected_text = []
    for word in words:
        corrected_text.append(correct_spelling(word))
    return ' '.join(corrected_text)

# Example for usage
sample_text = "I am a Python develepar andd data analistt."
corrected_text = spell_check_text(sample_text)
print(corrected_text)
