def calculate_revenue(prices, quantities_sold):
    revenues = prices.copy()
    for idx in range(len(revenues)):
        # print (revenues[idx], quantities_sold[idx])
        revenues[idx] *= float(quantities_sold[idx])
        # print (" -> ",revenues[idx])
    return revenues

def formatted_output(revenues):
    for idx in range(len(revenue_per_product)):
        print(f"{revenue_per_product[idx][0]} has total revenue of ${revenue_per_product[idx][1]}")
    return


# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
revenue = calculate_revenue(prices, quantities_sold)
#print (revenue)
revenue_per_product = list(zip(products,revenue))
#print (revenue_per_product)
# Example of expected output line (do not remove):
# print(f"{revenue[0]} has total revenue of ${revenue[1]}")
revenue_per_product = sorted(revenue_per_product)
formatted_output(revenue_per_product)