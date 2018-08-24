def tic_tac_toe(mat):
	for row in mat:
		if row.count(row[0]) == 3:
			print(row[0])
			return row[0]
	lst = []
	for j in range(3):
		for k in range(3):
			l = [i for i in mat[j][k]]
			lst.append(l)
	for itera in range(len(lst)-6):
		if lst[itera] == lst[itera+3] and lst[itera+3] == lst[itera+6]:
			if ''.join(lst[itera]) in ('x','o'):
				print(''.join(lst[itera]))
			else:
				print('invalid input')
				'''else:
					print('invalid game')'''
	'''elif lst[itera+2] == lst[itera+4] and lst[itera+4] == lst[itera+6]:
		print(lst[itera])'''
	'''elif lst[itera] == lst[itera+4]:
		print(lst[itera])'''

def read_matrix():
	 matrix = []
	 for i in range(3):
	 	l = [i for i in input().split(" ")]
	 	matrix.append(l)
	 return matrix

def main():
	mat = read_matrix()
	tic_tac_toe(mat)

if __name__ == "__main__":
	main()
