import pytest

# http://pytest-ordering.readthedocs.io/en/develop
#C A B F E D

@pytest.mark.run(order=2)
def test_run_order_methodA(OnetimesetUp,setUp):
    print("Running method A")
@pytest.mark.run(order=3)
def test_run_order_methodB(OnetimesetUp, setUp):
    print("Running method B")
@pytest.mark.run(order=1)
def test_run_order_methodC(OnetimesetUp,setUp):
    print("Running method C")
@pytest.mark.run(order=6)
def test_run_order_methodD(OnetimesetUp,setUp):
    print("Running method D")
@pytest.mark.run(order=5)
def test_run_order_methodE(OnetimesetUp,setUp):
    print("Running method E")
@pytest.mark.run(order=4)
def test_run_order_methodF(OnetimesetUp,setUp):
    print("Running method F")