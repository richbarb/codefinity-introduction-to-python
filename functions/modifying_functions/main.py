def apply_discount(price, discount=0.05):
    d_price = price - price*discount
    return d_price

def apply_tax(price, tax=0.07):
    t_price = price + price*tax
    return t_price

def calculate_total(price, discount=0.05, tax=0.07):
 #   print (f"in C_T: price = {price}, discount = {discount}, tax = {tax}")
    discounted_Price = apply_discount(price,discount)
#    print ("discounted price = ", discounted_Price)
    taxed_disc_price = apply_tax(discounted_Price,tax)
#    print ("taxed discounted price = ", taxed_disc_price)
    return (taxed_disc_price)

total_price = calculate_total(100)
#print ("Test Total price =",total_price)

total_price_default = calculate_total(120)
print (f"Total cost with default discount and tax: ${total_price_default}")
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)
print (f"Total cost with custom discount and tax: ${total_price_custom}")