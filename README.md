
## General instructions

The version of python to be used for this assignment is the default version that ships with Ubuntu at time of writing (3.8). 

Typing hints must be used and mypy will be used to test them. It is advisable to write tests for the features you develop. I will write tests for your code in any case, but you might find it helpful to write your own to make sure your code is working as expected. 

Docstrings should be present on classes and functions. The main program should ultimately be in python but if you want to use C or C++ to write parts of this code and call it from python using python's subprocess module or using tools like pybind11, you can but 50% of the code you have written must be python. 

Fork this git repository and submit the link of the git repo where you have shown your solutions to the evaluations below. 

Each solution must include its own requirements.txt file in case you use any external libraries. The only external libraries you should have to use is Flask (or FastAPI) for Evaluation 1, mypy for checking type annotations and Pytest is a good option for a testing suite if you like to use it (you don't have to). 

## Evaluation 1

You are working for a credit union in a rural part of Canada. The Financial Advisors there need to call a list of of customers who have mortgages renewing in the Spring. The Credit Union doesn't have a customer relationship management tool (traditionally they have been using Excel Spreadsheets). One of your colleagues is really enthusiastic about webpack and React but they need a persistent backend. The Credit Union doesn't want to use cloud technology and won't buy you a server so you are going to host the backend out of a desktop in your office that is always on. Make a backend with Flask (or FastAPI if you prefer) and SQLite. You don't have to use an ORM if you don't want to. Gitignore the sqlite database file but include a python script that creates a database with tables. 

Each Financial Advisor has a set of customers assigned to them. 

Your backend will need to be able to:

- For some Financial Advisor, GET a list of all customers who have not yet been called about their mortgage renewal
- For some Financial Advisor and customer, POST and GET notes from phonecalls about their mortgage renewal
- For some Financial Advisor and customer, POST details of an appointment to renew their mortgage including the date and office location.  
- For some Financial Advisor and day, GET a list of appointments including customer details for each appointment and office location 
- Finally for some customer, POST that the mortgage has been renewed

Your colleague wants to do analytics too. So you will need to implement one more call: 

- GET a list of financial advisors and summary statistics for each one including how many customers they have, how many customers they have called, how many customers they have made appointments with and finally how many customers have renewed their mortgages. 

To be clear, you do not have to produce a frontend. The API app should produce api endpoints on localhost and I will test them using the python requests module. 

## Evaluation 2

Your neice is learning about Ecology in school. She is a bright girl and you always look for every opportunity you can to try to pique her interest in computer science and python. Make her a similuation of a forest that has grass, rabbits and foxes. The rabbits eat the grass and the foxes eat the rabbits. The forest occurs in an 40x40 matrix where each bare square may generate grass with a 20% chance for every 5 ticks of the game clock. Rabbits and foxes move randomly in the forest. If a hungry Rabbit finds grass, it eats it, leaving a barren square and it is well-fed (ie. not hungry) for 10 ticks of the clock afterwards. If two rabbits or two foxes occupy the same square they will breed and produce a new instance of their kind. If a hungry Fox finds a Rabbit, it eats it, and it is well-fed for 12 ticks of the clock after. A Rabbit that his hungry for 10 ticks of the game clock dies and a Fox that is hungry for 12 ticks of the game clock will also perish. 

This is a console game. For each tick of the game clock, print a matrix in console with symbols to represent rabbits, grass and foxes. Also print a count of how much grass, how many rabbits and how many foxes there are. Each tick should last 3 seconds (so we can appreciate each scene) and there should be 60 ticks.



