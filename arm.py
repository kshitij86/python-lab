def checkArmstrong(x):
	y, su = x, 0 
	while(y > 0):
		d = y%10
		su += d**3
		y //= 10 
	print(f"Sum is : {su}")
	return su == x
print(checkArmstrong(153))