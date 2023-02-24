import csv
import math

def main():
	data = []
	readfile(data)
	normalization(data)
	print(data)


def readfile(array):
	with open('app1.data', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			array.append([float(num) for num in row])

	with open('app1.test', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			array.append([float(num) for num in row])

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

if __name__ == '__main__':
	main()
