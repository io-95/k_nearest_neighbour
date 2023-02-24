import csv
import math

line_test = 0
line_data = 0

def main():
	data = []
	readfile(data)
	normalization(data)
	
	#devide data in test and data
	test = []
	test.extend(data[-line_test:])
	data = data[:len(data) - line_test]

	positiv = []
	negativ = []
	devide_data(positiv, negativ, data)

	for i in range(len(positiv)):
		print(positiv[i])
	for i in range(len(negativ)):
		print(negativ[i])
	
def readfile(array):
	global line_test
	global line_data

	#read data from file
	with open('app1.data', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			array.append([float(num) for num in row])

	line_data = len(array)

	#read test data from file
	with open('app1.test', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			array.append([float(num) for num in row])

	line_test = len(array) - line_data

def normalization(array):
	for i in range(len(array[0])):
		min = math.inf
		max = -1
		for j in range(len(array)):
			if array[j][i] > max:
				max = array[j][i]
			if array[j][i] < min:
				min = array[j][i]
		
		for j in range(len(array)):
			array[j][i] = (array[j][i] - min) / (max - min) 

def devide_data(pos, neg, array):
	for i in range(len(array)):
		if array[i][15] == 1:
			pos.append(array[i])
		else:
			neg.append(array[i])

if __name__ == '__main__':
	main()
