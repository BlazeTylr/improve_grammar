from lib.improve_grammar import *

def test_improve_grammar_no_upperecase():
    actual = improve_grammar("hello there.")
    expected = "Your sentence doesn't start with an uppercase letter"
    assert actual == expected

def test_improve_grammar_no_correct_punctuation_mark():
    actual = improve_grammar("Hello there@")
    expected = "Your sentence doesn't end with a correct punctuation mark."
    assert actual == expected