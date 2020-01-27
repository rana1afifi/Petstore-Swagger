"""The tests to run in this project.
To run the tests type,
$ nosetests --verbose
"""
import challenge2 as ch

from nose.tools import assert_true
def test_auction():
    "Test auction function"
    input= {'John':100 , 'Sara':280 , 'Martin':300 ,'Sandy':280 }
    output = ch.auction(input)
    assert(output=={'Martin':280,'Sandy':280,'Sara':100,'John':300})




