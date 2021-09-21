#  File: Pancake.py

#  Description: Creating an algorithm to sort pancakes by flipping lists

#  Student's Name: Pranjal Jain

#  Student's UT EID: pj5775

#  Partner's Name: Maurya Atluri

#  Partner's UT EID: ma57744

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 2/21/20

#  Date Last Modified: 2/21/20

#  Input: pancakes is a list of positive integers
#  Output: a list of the pancake stack each time you
#          have done a flip with the spatula 
#          this is a list of lists
#          the last item in this list is the sorted stack
def sort_pancakes ( pancakes ):
  every_flip = []
  not_sorted = len(pancakes) - 1
  biggest_index, not_sorted = biggest_pancake(pancakes, not_sorted)
  if biggest_index == -1:
    return -1
  while biggest_index != -1:
    if biggest_index == 0:
      pancakes = flip(pancakes, not_sorted)
      not_sorted -= 1
      every_flip.append(pancakes)
    else:
      pancakes = flip(pancakes, biggest_index)
      every_flip.append(pancakes)
      pancakes = flip(pancakes, not_sorted)
      not_sorted -= 1
      every_flip.append(pancakes)
    if not_sorted == 0:
      break
    biggest_index, not_sorted = biggest_pancake(pancakes, not_sorted)
      
    
  return every_flip    # return a list of flipped pancake stacks

def flip (pancakes, index):
  flipped_pancakes = pancakes[:index + 1]
  flipped_pancakes.reverse()
  flipped_pancakes += pancakes[index + 1:]
  return flipped_pancakes

def biggest_pancake(pancakes, not_sorted):
  if not_sorted == 0:
      return -1, 0
  biggest =  max(pancakes[0:not_sorted + 1])
  while biggest == pancakes[not_sorted]:
    not_sorted -= 1
    if not_sorted == 0:
      return -1, 0
    biggest =  max(pancakes[0:not_sorted + 1])
  biggest_index = pancakes[0:not_sorted + 1].index(biggest)
  return biggest_index, not_sorted
  
  
    
def main():
  # open the file pancakes.txt for reading
  in_file = open ("./pancakes.txt", "r")

  line = in_file.readline()
  line = line.strip()
  line = line.split()
  print (line)
  pancakes = []
  for item in line:
    pancakes.append (int(item))
  in_file.close()
  # print content of list before flipping
  print ("Initial Order of Pancakes = ", pancakes)

  # call the function to sort the pancakes
  every_flip = sort_pancakes ( pancakes )

  # if pancakes already flipped end program
  if every_flip == -1:
    print("Pancakes already in order")
    print("Final Order of Pancakes = ", pancakes)
    quit()
  # print the contents of the pancake stack after
  # every flip
  for i in range (len(every_flip)):
    print (every_flip[i])

  # print content of list after all the flipping
  print ("Final Order of Pancakes = ", every_flip[-1])

if __name__ == "__main__":
  main()
