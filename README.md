## This is a README file that shows the instructions for product_analysis.py
#### step1: install dependencies 
pip3 install requests

#### step2: execute the solution
python3 solution.py

#### step3: execute the test case
python3 test.py

## Analysis Requirement
Query the following API that returns a randomized list of products in JSON format.
https://www.beautylish.com/rest/interview-product/list

1. Display a list of products including only the brand name, product name, and price. 
2. Filter out any products that are hidden or deleted.
3. Sort by lowest to the highest price. If two items have the same price, sort by name. 
4. If the same product is included twice, only display it once.
5. Display a summary that includes: a. The total number of unique products b. The total number of unique brands c. The average price


