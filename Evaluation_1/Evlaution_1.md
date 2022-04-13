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
