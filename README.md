# README [![CI](https://github.com/nogibjj/Vivian_Project6/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Vivian_Project6/actions/workflows/ci.yml)
This repository features the materials for Mini-Project 6. The important files are:
- Makefile
- cicd.yml
- lib.py
- main.py
- test_main.py
- .env(a hidden file)
- log.md (a log file)

## Purpose Of Project
- Connect to a cloud mySQL database
- Design a complex SQL query involving joins, aggregation, and sorting and perform the query with CICD. 

## Preparation 
1. open the project in codespaces
2. container built and virtual environment to be activated through requirements.txt

## Steps
1. set up a cloud MySQL database called "BarBeerDrinker" which includes 2 tables: Bar and Sells. Bar includes all in-network bars and Sells includes all past time, type, and year of the beers sold at each bar. 
2. make a .env file and store my connection information including SERVER_HOSTNAME, SERVER_PORT, USER_NAME, ACCESS_TOKEN, and DATABASE_NAME.
4. connect to the cloud database and run a complex query.
5. obtain the result after querying on the cloud database. 

## Check Format & Errors
1. make format
2. make lint
   
<img width="680" alt="Screen Shot 2023-10-08 at 6 08 20 PM" src="https://github.com/vivianzzzzz/Template/assets/143654445/3a4ff1e7-0e71-451d-955e-a94fd264977f">
   
3. make test
   
<img width="889" alt="Screen Shot 2023-10-08 at 6 08 29 PM" src="https://github.com/vivianzzzzz/Template/assets/143654445/9df54e70-ecd7-403c-ba6c-59816ef17560">

## Query
Query and Results: 

<img width="527" alt="Screen Shot 2023-10-08 at 6 20 56 PM" src="https://github.com/vivianzzzzz/Template/assets/143654445/2d93b277-f24c-49ec-ad32-0f9dcd4f0485">

Explanation:
This query left-joins table "Bars" with a sub-table from "Sells" which I name it "a" 
- the sub-table "a" is created through the sub-query "SELECT s.bar FROM Sells s WHERE s.price > 5" which retrieves the names of bars from the Sells table where the selling price of some item is greater than 5.
- the LEFT JOIN attempts to join the result from the sub-table to the Bars table based on the condition where a.bar matches the name of the bar in the Bars table. The use of a LEFT JOIN ensures that all rows from the Bars table (even those that do not have a matching bar in the subquery) will be included in the result.
- "WHERE a.bar IS NULL": filters out all rows where there is a match between Bars and the subquery. In other words, it retains only those bars from Bars that don't sell any item for a price greater than 5. It effectively gives us bars that only sell items at a price of 5 or less.
- "GROUP BY city": After the join and filter conditions are applied, the resulting set of records is grouped by the city where the bars are located.
- "SELECT city, count(city)" Finally, the query selects the name of each city from these grouped records and counts how many bars in each city fit the criteria (only sell items for a price of 5 or less).

Final Output:
The result of the query will be a list of cities and the number of bars in each city that do not have any item priced above 5.
This result can also be retrieved in the log file. 

<img width="898" alt="Screen Shot 2023-10-08 at 6 07 51 PM" src="https://github.com/vivianzzzzz/Template/assets/143654445/a1f2edac-99da-4673-b89c-194a1698d6b0">

## Visualization

<img width="368" alt="Screen Shot 2023-09-30 at 11 31 51 AM" src="https://github.com/vivianzzzzz/Template/assets/143654445/8b808d80-0203-40e7-86d0-27380c4cfbae">




