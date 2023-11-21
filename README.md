"# IIHT-Selenium-Money-Control-Python" 

# Important Info


# Running test
	Open the command prompt.
	Navigate to the directory where your Python script is located.
	Run the following command:
	pytest -s .\AutomationTest.py
	 
    
    To execute a single test using the command prompt, you can follow these steps:

	Open the command prompt.
	Navigate to the directory where your Python script is located.
	Run the following command:
	pytest -v .\AutomationTest.py::test_mouse_over_personal_finance
	This command will execute the test_mouse_over_personal_finance test.

    Finding all possible test
        Collect Test - pytest --collect-only
    
    Running all test 
        pytest
    
    Running all test with verbose and print statement
        pytest -vs

    Running specific module
        pytest -vs testfilename.py

    Running specific method/test inside module
        pytest -vs testfilename.py::testname

    Running specific method/test under class inside module
        pytest -vs testfilenamewithclass.py::classname::testname

    Running set of tests which has specific keyword in method name
        pytest -vs -k keywordname

    Running set of tests with custom marking (@pytest.mark.regression)
        pytest -vs -m regression


# Naming Conventions
    File name should start or end with test
    Test methos name or function names should start with test_
    If tests are defined as methods on a class, class name should start with Test


# Fixtures in pytest
    Execute set up activities before each method/class/module
    Execute tear down activity after each method/class/module (using yield)
    Get data for test case
    Data paremeterization
    Fixtures could be centralized via conftest.py