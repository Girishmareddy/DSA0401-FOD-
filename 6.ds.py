item_prices = [2.5, 3.0, 1.75, 5.25]
quantities = [3, 2, 4, 1]
discount_rate = 10  
tax_rate = 7    
total_cost_before_discount = sum(price * quantity for price, quantity in zip(item_prices, quantities))
discount_amount = (discount_rate / 100) * total_cost_before_discount
total_cost_after_discount = total_cost_before_discount - discount_amount
tax_amount = (tax_rate / 100) * total_cost_after_discount
final_total_cost = total_cost_after_discount + tax_amount
print("Total Cost Before Discounts: $", total_cost_before_discount)
print("Discount Amount: $", discount_amount)
print("Total Cost After Discounts: $", total_cost_after_discount)
print("Tax Amount: $", tax_amount)
print("Final Total Cost: $", final_total_cost)
 
