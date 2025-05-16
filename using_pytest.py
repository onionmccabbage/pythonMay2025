# we may need to isntall pytest
# py -3 -m pip install pytest

# import any modules we may need
from collections import namedtuple

# write some code to be tested
task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
task.__new__.__defaults__ = (None, None, False, None)

def test_defaults(): # every test we write begins with the word 'test'
    t1 = task('Learn Py', 'Floella', False, 42)
    t2 = task() # this will have the default values
    t3 = task(None, None, False, None)
    # write a test (this might be in another module)
    assert t2 == t3

# run the tests like this: 
# pytest -v using_pytest.py