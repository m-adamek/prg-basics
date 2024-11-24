# The store has 10 types of goods in stock.
# The prices of the goods and the number of pieces of goods
# are given below. Write a program that calculates the value of
# all the goods available in the store.

# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

total = 0
index = 0 

for product in product_quantities:
    index = product_quantities.index(product)
    total += product * product_quantities[index]

print("Total:", total)