# tracking sales for an online jeans retailer

stock = 600
jeans_sold = 500
target = 500

target_hit = jeans_sold == target
print("Hit jeans sale target: ")
print(target_hit)

# == tells the code to check if jeans_sold is actually equal to target, and if true, then the store did meet their target

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock: ")
print(in_stock)

# != tells the code to check if the current stock is NOT zero, meaning if this is true, there is some jeans available