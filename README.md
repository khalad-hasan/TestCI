# Budget-Planning
![passing](https://app.travis-ci.com/Saisree-123/DATA533-LAB4.svg?branch=master) <br>
**PyPI link** : https://pypi.org/project/budgetplanner/

# Subpackage1: User #
* **Module1:service**
  	* **list()** 
  		- List the service available
  	* **show()** 
  		- Show the detail of the service you choose
  	* **choice()** 
  		- Provide information about what membership you need in order to get that service

* **Module2:password**
  	* **show**
  		- Show the password and userid stored
  	* **update**
  		- Update the account information
  	* **deelete**
  		- Delete account information

* **Module3:personal_info**
  	* **show**
  		- Show collected information
  	* **update**
  		- Update information
  	* **delete**
  		- Delete information
  
# Subpackage2: Budget

* **Module1:Free Membership**
 	* **show_budget_chart()**
 		- Shows chart of current savings vs goal
	* **add_amount()**
		- Add money to the savings
	* **withdraw_amount()**
		- Withdraw money from the savings

* **Module2:Basic Membership**
	* **user_expenditure_data()**: 
		- Get user’s data on expenditure area and the expenditure for a month
	* **expenditure_chart()**
		- Displays graph of user expenditure made under each category
	* **analysis_and_budget_suggestion()**
		- Displays three options for budget savings on top most concern area
	* **reward_calculator()**
		- Calculates the reward for each of the three options

* **Module3:Premium Membership(Basic Membership)**
	* **ideal_expenditure_chart(user_salary)**
		- Displays graph of ideal vs user expenditure made under each category
	* **analysis_and_budget_suggestion() (overridden)**
		- Displays three options for budget savings on op most concern areas
	* **reward_calculator()  (overridden)**
		- Calculates the reward for each of the three options

   
