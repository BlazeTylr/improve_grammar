from lib.improve_grammar import *

def test_improve_grammar_no_upperecase():
    actual = improve_grammar("hello there.")
    expected = "Your sentence doesn't start with an uppercase letter"

def test_improve_grammar_no_upperecase():
    actual = improve_grammar("Hello there@")
    expected = "Your sentence doesn't end with a correct punctuation mark."