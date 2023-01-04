# This is to generate random numbers
import random

# this function created 2D array
def create_2d_list(numberOfRows, numberOfColumns):
  # creating an empty 2D list
  list_2d = [[0] * numberOfColumns for i in range(numberOfRows)]

  # filling the list with random integers
  for i in range(numberOfRows):
    for j in range(numberOfColumns):
      list_2d[i][j] = random.randint(0, 100)

  return list_2d
  
# this function sorts the array based on particular column index
def sort_2d_list(list_2d, column_index):
  # sort the list based on the specified column index
  sorted_list = sorted(list_2d, key = lambda x: x[column_index])
  
  return sorted_list
  
# this function prints 2d array in proper manner
def print_2d_array(array):
    
    for i in range(len(array[0])):
        for j in range(len(array[i])):
            print(array[i][j], end = " ")
        print()