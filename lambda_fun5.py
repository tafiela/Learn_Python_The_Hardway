def even_numbers(x):
	is_even = lambda num : num % 2 ==0
	even_lst =[]
	for num in x:
	#	if num % 2 == 0:
		if is_even(num):
			even_lst.append(num)
	return even_lst
		
		
print even_numbers(range(10))
