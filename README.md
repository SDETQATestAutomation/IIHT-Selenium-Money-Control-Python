"# IIHT-Selenium-Money-Control-Python" 

# Important Info
	No need to add chromedrive, latest selenium version takes care of chromedrive.


# Running test
	cd  C:\Users\pranjan\Desktop\IIHT\IIHTWorkspace\Selenium-Money-Control-Python\src\test\python\com\iiht\evaluation\automation\functional
	 pytest -s .\AutomationTest.py
	 
	 To run a single test with order 1, you can use the -k option in pytest along with the test name and the --order-scope option to set the order scope to "test":
	 
	 if __name__ == "__main__":
    pytest.main([__file__, '-k', 'test_mouse_over_personal_finance', '--order-scope', 'test'])
    
    To execute a single test with order 1 using the command prompt, you can follow these steps:

	Open the command prompt.
	Navigate to the directory where your Python script is located.
	Run the following command:
	pytest -k test_mouse_over_personal_finance -m order:1
	This command will execute the test_mouse_over_personal_finance test with the order:1 marker.
	