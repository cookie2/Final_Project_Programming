# 0. Check if you have installed python3. If not, install it.

# 1. Make sure you have installed all the packages. 
## Which package you should install, please refer to "requirements.txt".
## If not, follow this:
	windows:
		double-click package_auto_install.bat
		or
		open your cmd and input command:
			pip install --upgrade --user ***package***
		or:
			py -m pip install ***package***
		
	Linux:
		open your terminal and input command:
			pip install --upgrade ***package***
		or:
			python3 -m pip install --upgrade ***package***
	Mac OS:
		press command + space bar and type in terminal.
		click the app icon to open a new terminal window.
		input command:
			pip install --upgrade ***package***
		or:
			python3 -m pip install --upgrade ***package***
		
	If you use Jupyter, create a block and paste:
		!pip install --upgrade ***package***
	warning:
		I am not suggest you use colab, because it will has many problems. 

	Else if you use Anaconda, find out your terminal and input those command:
		pip install --upgrade ***package***
		***when you have done, follow the messeges show on your terminal, restart it.***

# 2. Before you run website_scraper.py or website_scraper_another_ver.py.
## You should do that:
	-Open this .py file by your IDE, such like Python IDLE, Visual Studio Code, Jupyter or something else.
	-Read all the comments in website_scraper.py.
## You should know:
	-This example is for chrome user.
	-If you are not, search how to change selenium setting for different browser by yourself.
	-Cause my poor English, if you cannot understand what those comments meaning, you can contact me or research by yourself.

# 3. You should realize:
## It is just a simple code, web scraping is more complex than you thought. If you are instersing in. Ask Professor or give up.
### Just kidding, here is the direction:
	1.If you not familiar with website structure, you should learn it.(Keyword: Html, Css and Javascript)
	2.You should know what is html element.
	3.You must know the difference between Static Webpage and Dynamic Webpage.
	4.How to do html syntactic analysis.(In this case, we use python package named beautifulSoup4)
	5.How to do data cleaning.
### Those are basic requirements for web scraping. If you want to know more, I recommend you give up.
### Joke again, follow this:
	1.Know how to read messeges from the website in console panel.
	2.Observe network panel when website is loading so that you can realize where the data came from.
	3.Find ways to catch the information you want.

# 4. Give up.

# 5. If you still insist, follow this:
	1.Research how the website backend works.
	2.Research what is Communications Protocol.
	3.Enhance your programming ability.
	4.Know what is multithreading and how to use it.
	5.Give up.

# 6.Another version.
## I just release another version use undetected_chromedriver named website_scraper_another_ver.py.
#### You must notice that this version is only available in the Windows Operation System.
#### If you use others Operation System, ask god for help.
#### Just kidding, follow this:
	1.Delete the section I comment "# get chrome version, just available in Windows"
	2.Check your browser version.
	3.Edit this line: version = eval(resp.split(".")[0]), the variable "version" must same as your browser version.
		For example:
			If your chrome version is 101, then your edition should be:
				version = 101
	4.This version also demonstrate how to use javascript to control website.
	5.This version scrape target is udemy.

# 7. Give up.

# 8. Before you run simple_text_mining.py
## you should know:
### (1) Ensure your dataset is a csv file, because in this example, I use csv file as my dataset. 
### (2) If you get error messeges, shut down your Laptop/PC and go to sleep.
### (3) Just kidding, follow this:
	Which package you should install, please refer to requirements.txt
	windows:
		double-click package_auto_install.bat
		or
		open your cmd and input command:
			pip install --upgrade --user ***package***
		After you finished installing, then input: 
			python -m spacy download en_core_web_sm
	Linux:
		open your terminal and input command:
			pip install --upgrade --user ***package***
			python -m spacy download en_core_web_sm
		or:
			python3 -m pip install --upgrade ***package***
			python3 -m spacy download en_core_web_sm
	Warning:
		I am not sure if the commands for Linux are correct.
		Because I have not test it.
	Mac OS:
		press command + space bar and type in terminal.
		click the app icon to open a new terminal window.
		input command:
			pip install --upgrade ***package***
			python -m spacy download en_core_web_sm
		or:
			python3 -m pip install --upgrade ***package***
			python -m spacy download en_core_web_sm
	Warning: 
		I am not sure if the commands for Mac OS are correct.
		Because I am so poor, cannot afford the Macbook.
	If you use Jupyter, create a block and paste:
		!pip install --upgrade ***package***
		python -m spacy download en_core_web_sm
	warning:
		I am not suggest you use colab, cause it will has many problems.
	warning:
		I am not sure if the commands for Jupyter are correct.
		Because I have not test it.
		If you have any problems, contact me.
	Else if you use Anaconda, find out your terminal and input those command:
		pip install --upgrade ***package***
		python -m spacy download en_core_web_sm
		***when you have done, follow the messeges show on your terminal, restart it.***
	warning:
		I am not sure if the commands for Anaconda are correct.
		Because I have not test it.
		If you have any problems, contact me.
### (4) Read all the comments in this .py file.
### (5) If you cannot understand what those comments meaning or want to learn more detail about this code:
	Ask professor or Dr. Tu.
### (6) If this code have done, check your folder:
	If there is a file named LDA_Visualization.html, it means your code run successfully.
### (7) Open LDA_Visualization.html with your browser, you can see the result.
### (8) If you use notebook like Colab or Jupyter, you can modify your visualization:
###### change those codes:
	visualisation = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word, mds = "mmds")
    pyLDAvis.save_html(visualisation, 'LDA_Visualization.html')
###### to:
	pyLDAvis.enable_notebook()
	visualisation = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
	visualisation

# 9. You still need to realize:
## It also a simple code, Natural Language Processing is more complex than you thought. If you are instersing in. Ask Professor or give up.

# 10. I do not have any quotes, give up.
