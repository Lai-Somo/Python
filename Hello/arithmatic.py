fee = input("Enter amount: ")
discount_percent = input("Enter the discount percent: ")
discount_amount = (float(discount_percent) / 100) * float(fee)
payable_amount = float(fee) - discount_amount
print("Discount amount: ", discount_amount)
print("Fee to be paid: ", payable_amount )