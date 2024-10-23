from hw1_strings import *
import pytest

def test_constantsAndVariables():
    assert constantsAndVariables() == 23

def test_NumTimesQuoteIn23():
    assert numTimesQuoteIn23() == 15

def test_StartAndEndIndeciesOfSubstring():
    assert startAndEndIndicesOfSubString() == (262, 308)

def test_IntegerSeqToString():
    assert integerSeqToString() == "J Robert Oppenheimer"