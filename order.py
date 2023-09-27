# Program: order.py
# Programmer: Nneamaka Nwaigbo
# Date: October 9, 2020
# Description: Lab 5
# ###########################################

menu = ["hamburger", "fries", "soda"]
customer_order = ["hamburger", "fries", "soda", "pizza"]
price = [3,2,1.25]
total_price = 0.0
print("Order Detail:\n")

for order in customer_order:
	if order in menu:
		print(f"Adding {order.title()}.")
		order_index = menu.index(order)
		print(f"Price: ${price[order_index]:.2f}\n")
		total_price = total_price + price[order_index]
	else:
		print(f"Sorry, we don't have {order}.\n")

print("Your order is ready!")
print(f"Total Price: ${total_price:.2f}")