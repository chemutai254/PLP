# Function to calculate the discounted price
def calculate_discount(price, discount_percent):
    discount_percent = discount_percent / 100
    # If discount is less than 20%, return the original price
    if discount_percent < (20/100):
        return price 
    else:
        return price - (price * discount_percent)

# Prompt user 
price = float(input("Enter the price: "))
dicount_percent = float(input("Enter the discount percentage:"))

# Calculate the output
print("The final price is:", calculate_discount(price, dicount_percent))