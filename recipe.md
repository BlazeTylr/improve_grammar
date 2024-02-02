## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def improve_grammar(sentence_string):
    """It will check if the sentence starts with a capital letter and ends with a correct punctuation mark.
    """
    pass
```

## 3. Create Examples as Tests

```python

"""
Given a sentence it will return explanation why the semtence is not correct or a message correct sentence.
"""
improve_grammar('Hello this is a sentence!') => 'Correct sentence'
improve_grammar('Hello this is a sentence!') => "Your sentence doesn't start with a capital letter."
```

## 4. Implement the Behaviour

```python
# EXAMPLE

from lib.improve_grammare import *

"""
Given a sentence without uppercase letter in position 1 it will return: your sentence doesn't start with an uppercase letter.
"""
def test_improve_grammar_no_upperecase():
    actual = improve_grammar("hello there.")
    expected = "Your sentence doesn't start with an uppercase letter"

"""
Given a sentence without correct punctuation mark in the end will return: Your sentence doesn't end with a correct punctuation mark.
"""
def test_improve_grammar_no_upperecase():
    actual = improve_grammar("Hello there@")
    expected = "Your sentence doesn't end with a correct punctuation mark."
```
