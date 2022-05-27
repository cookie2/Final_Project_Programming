0.Check if you have installed python3. If not, installed it.

1.Make sure you have installed all packages this program required. 
	if not, follow this:
		windows:
			double-click package_auto_install.bat
			or
			open your cmd and input command:
				pip install --upgrade --user selenium
				pip install --upgrade --user beautifulSoup4
				pip install --upgrade --user webdriver_manager
			or:
				py -m pip install selenium
				py -m pip install beautifulSoup4
				py -m pip install webdriver_manager
		
		Linux:
			open your terminal and input command:
				pip install --upgrade selenium
				pip install --upgrade beautifulSoup4
				pip install --upgrade webdriver_manager
			or:
				python3 -m pip install --upgrade selenium
				python3 -m pip install --upgrade beautifulSoup4
				python3 -m pip install --upgrade webdriver_manager
		Mac OS:
			press command + space bar and type in terminal.
			click the app icon to open a new terminal window.
			input command:
				pip install --upgrade selenium
				pip install --upgrade beautifulSoup4
				pip install --upgrade webdriver_manager
			or:
				python3 -m pip install --upgrade selenium
				python3 -m pip install --upgrade beautifulSoup4
				python3 -m pip install --upgrade webdriver_manager
		
		if you use jupyter, create a block and paste:
			!pip install --upgrade selenium
			!pip install --upgrade beautifulSoup4
			!pip install --upgrade webdriver_manager
		warning: i am not suggest you use colab, cause it will has many problems. 

		else if you use anaconda, find out your terminal and input those command:
			pip install --upgrade selenium
			pip install --upgrade beautifulSoup4
			pip install --upgrade webdriver_manager

2.Before you run website_scraper.py, you should know:
	-Open this .py file by your IDE, such like Python IDLE, Visual Studio Code, Jupyter or something else.
	-Read all the comments in this .py file.
	-This example is for chrome user, if you are not, search on browser, how to change selenium setting for different browser.
	-Cause my poor English, if you cannot understand what those comments meaning, you can contact me or research by yourself.

3.You should realize it just an simple code, web scraping is more complex than you thought. If you are instersing in. Ask Professor or give up.
	Just kidding, here is the direction:
		1.If you not familiar with website structure, you should learn it.(Keyword: html, css and javascript)
		2.You should know what is html element.
		3.You must know the difference between Static Webpage and Dynamic Webpage.
		4.How to do html syntactic analysis.(In this case, we use python package beautifulSoup4)
		5.How to do data cleaning.
	There are basic requirements for web scraping. If you want to know more, I recommend you just give up.
	Joke again, follow this:
		1.Know how to read messege from website in console panel.
		2.Observe network panel when website is loading so that you can realize where does data came from.
		3.Find ways to catch the information you want.

4.Give up.

5.If you still not give up, follow this:
	1.Research how the website backend works.
	2.Research what is Communications Protocol.
	3.Enhance your programming ability.
	4.Know what is multithreading and how to use it.
	5.Give up.

6.I will upload the text mining code in next release, maybe.

7.Do not run simple_text_mining.py! I haven't finished it.