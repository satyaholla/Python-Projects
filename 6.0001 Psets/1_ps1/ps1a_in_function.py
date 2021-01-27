def part_a(salary, savings_percent, total_cost):
	#########################################################################
	""" Set down payment to 0.15 (given in problem), amount saved
	to 0 (given), and the interest rate to 5% (or 0.05), which is
	also given, and you start off at 0 months. """
	percent_down_payment = 0.15
	amount_saved = 0
	r = 0.05
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ##
	###############################################################################################
	""" the loop iterates for each month, and after each iteration, the value of amount saved
	increases by the appropriate amount. This continues until amount saved > cost of down payment """
	while amount_saved < total_cost*percent_down_payment: #cost of down payment is the total cost times the down payment percentage
	    months = months + 1 #iterates the number of months (each loop represents the end of a month)
	    amount_saved *= 1 + r/12 #investment return: the amount saved increases by amount_saved*r/12, since r is ANNUAL
	    amount_saved += salary*savings_percent/12 #how much you earn from the salary
	
	#######################################################
	## Print out the number of months it would take here ##
	#######################################################
	print ("Number of months:", months) #output the number of months
	return months