import csv
import math
import matplotlib.pyplot as plt


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
	
	false_rates = []
	for i in range(len(data)):
		false_rates.append(k_nearest_neighbour(data, test, i))
		
	show_result(false_rates)
	
def show_result(data):
	print("Optimal k is: ", data.index(min(data)))
	
	plt.scatter(range(len(data)), data)

	plt.xlabel('K')
	plt.ylabel('Falserate')
	plt.title('Falserate')

	plt.show()

	
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

def k_nearest_neighbour(data, test, k):
	correct = 0
	false = 0
	
	for i in range(len(test)):
		dist_list = []
		for j in range(len(data)):
			dist_list.append([
				manhatten_distance(data[j], test[i]),
				data[j][15]
				])

		classification = -1
		count_pos = 0
		count_neg = 0	
		dist_list.sort()

		#count classification of the neighbours
		for l in range(k+1):
			if dist_list[l][1] == 0:
				count_neg += 1
			else:
				count_pos += 1

		if count_pos > count_neg:
			classification = 1
		else:
			classification = 0

		if classification == test[i][15]:
			correct += 1
		else:
			false += 1

	return false

def manhatten_distance(pointA, pointB):
	dist = 0
	for i in range(len(pointA) - 1):
		sum = pointA[i] - pointB[i]
		sum = abs(sum)
		dist += sum
	return dist

if __name__ == '__main__':
	main()
