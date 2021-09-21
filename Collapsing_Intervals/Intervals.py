#  File: Intervals.py
#  Description: Collapsing intervals that intersect
#  Student Name: Pranjal Jain   
#  Student UT EID: pj5775
#  Course Name: CS 313E
#  Unique Number: 50210
#  Date Created: 9/7/19
#  Date Last Modified: 9/9/19

#checks all cases of when to merge intervals
def check_merge(tup1, tup2):
    #defines min and max for each interval
    tup1_min = tup1[0]
    tup1_max = tup1[1]
    tup2_min = tup2[0]
    tup2_max = tup2[1]

    #cases in which to merge
    if(tup1_min  <= tup2_min and tup2_max <= tup1_max):
        return (True, tup1) 

    if(tup1_min <= tup2_min and tup1_max <= tup2_max and tup2_min <= tup1_max):
        return (True, (tup1_min, tup2_max))

    if(tup2_min <= tup1_min and tup2_max <= tup1_max):
        return (True, (tup2_min, tup1_max))

    if(tup2_min <= tup1_min and tup2_max >= tup1_max):
        return (True, tup2)

    return (False, tup1, tup2)


#checks to see if the intervals can still be merged
def can_still_merge(tup_list):
    tup_list.sort()

    #call check_merge to see if any more pairs can be merged
    res = False
    for i in range(0, (len(tup_list) - 1), 2):
        check = check_merge(tup_list[i], tup_list[i+1])
        if(check[0]):
            res = True
    return res    


#takes the input and returns the merged intervals
def merge_intervals(file):
    f = open(file, 'r')
    lines = f.read()

    #takes the file and makes each interval into a tuple pair
    num = lines.split()
    integers = [int(i) for i in num]
    interval = [(integers[i],integers[i+1]) for i in range(0,len(integers),2)]
    
    interval.sort()

    #contines running check_merge until can_still_merge becomes false
    #adds the merged intervals and non-intersecting intervals into new list 
    result = []
    while can_still_merge(interval):
        for i in range(0, len(interval) - 1, 2):
            check = check_merge(interval[i], interval[i+1])
            if(check[0] == True and not check[1] in result):
                result.append(check[1])
            elif(check[0] == False):
                result.append(check[1])
                result.append(check[2])
        if(len(interval) % 2 == 1):
            result.append(interval[len(interval) - 1])
        interval = result
        result = []

  
    return interval


#implemented bubble sort to sort according to size of interval
def sort_interval(inter):
    
    done = False
    while(not done):
        num_swaps = 0
        for i in range(0,len(inter)-1):
            size = inter[i][1] - inter[i][0]
            size2 = inter[i+1][1] - inter[i+1][0]
            if size > size2:
                inter[i],inter[i+1] = inter[i+1],inter[i]
                num_swaps +=1
        if num_swaps ==0 :
            done = True
 
    return inter
        

def main():
    collapse_intervals = merge_intervals('intervals.txt')
    final_intervals = sort_interval(collapse_intervals)
    for i in final_intervals:
        print(i)


main()
