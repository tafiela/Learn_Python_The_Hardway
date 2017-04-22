class cars:
	
	def __init__(self,color,model,year,make, P_price):
		self.color = color
		self.model = model
		self.year = year
		self.make = make
		self.purchased_price=P_price

	def selling_price(self):
		return self.purchased_price + (self.purchased_price * .20)


car1 = cars("Black", "3-Series", 1999, "convertable",10000)

print car1.year
print car1.selling_price()



