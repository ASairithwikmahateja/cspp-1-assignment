# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.


def evalQuadratic(a_i, b_i, c_i, x_i):
    y_i = a_i*x_i*x_i+b_i*x_i+c_i
    return y_i
def main():
	data = input()
	data = data.split(' ')
	data = list(map(float, data))
	# print(data)
	for x_i in range(len(data)):
		temp = str(data[x_i]).split('.')
		if(temp[1] == '0'):
			data[x_i] = int(float(str(data[x_i])))
		else:
			data[x_i] = data[x_i]
	print(evalQuadratic(data[0],data[1],data[2],data[3]))

if __name__ == "__main__":
	main()

