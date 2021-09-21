#  File: BabyNames.py 

#  Description: Query of popular baby names 

#  Student Name: Pranjal Jain

#  Student UT EID: pj5775

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 9/11/2019

#  Date Last Modified: 9/13/2019


#creates dictionary of all names and their popularity
def baby_names(f):
    file = open(f)
    names = file.readlines()

    name_pop = {}
    
    for i in range(len(names)):
        line = names[i].split()
        for j in range(len(line)):
            name_pop[line[0]] = line[1:]
                     
    for dicts in name_pop:
        name_pop[dicts] = [int(i) for i in name_pop[dicts]]            

    return name_pop         

#checks if the name exists in the dictionary 
def name_exists(name, name_dict):
    
    if name in name_dict:
        return True
    else:
        return False

#returns the decade when the name was the most popular
def highest_rank(name, name_dict):
    copy_dict = name_dict

    #coverts 0 to 1001
    for i in range(len(copy_dict[name])):
        if copy_dict[name][i] == 0:
            copy_dict[name][i] = 1001
                
    highest = min(copy_dict[name])

    decade_index = 12
    
    for i in range(len(copy_dict[name])):
        if copy_dict[name][i] == highest:
            decade_index = i

    if decade_index == 0:
        return (1900)
    if decade_index == 1:
        return (1910)
    if decade_index == 2:
        return (1920)
    if decade_index == 3:
        return (1930)
    if decade_index == 4:
        return (1940)
    if decade_index == 5:
        return (1950)
    if decade_index == 6:
        return (1960)
    if decade_index == 7:
        return (1970)
    if decade_index == 8:
        return (1980)
    if decade_index == 9:
        return (1990)
    if decade_index == 10:
        return (2000)
            
#returns all the ranks of a given name
def name_ranks(name, name_dict):

    if name in name_dict:
        return name_dict[name]

#returns the names that were ranked each decade
def ranked_every_year(name_dict):

    ranked_names = []

    for i in name_dict:
        if 0 not in name_dict[i]:
            ranked_names.append(name_dict)

    ranked_names.sort()

    return ranked_names

#returns the popularity based on the decade
def decade_rank(name, dec, name_dict):

    if dec == 1900:
        return name_dict[name][0]
    if dec == 1910:
        return name_dict[name][1]
    if dec == 1920:
        return name_dict[name][2]
    if dec == 1930:
        return name_dict[name][3]
    if dec == 1940:
        return name_dict[name][4]
    if dec == 1950:
        return name_dict[name][5]
    if dec == 1960:
        return name_dict[name][6]
    if dec == 1970:
        return name_dict[name][7]
    if dec == 1980:
        return name_dict[name][8]
    if dec == 1990:
        return name_dict[name][9]
    if dec == 2000:
        return name_dict[name][10]

#deletes names that were not ranked in the given decade
#returns the names that were ranked in the given decade
def is_ranked(name, dec, name_dict):
    copy = name_dict

    delete = []
    for key in list(copy):
        if decade_rank(name,dec,copy) == 0:
            delete.append(key)

    for i in delete:
        del copy[i]
    
    return copy

#returns list of names that were ranked every decade
def always_ranked(name_dict):
    name_list = []
    for name in name_dict:
        if 0 not in name_dict[name]:
            name_list.append(name)

    return name_list

#checks if the name was increasing in popularity
def more_popular(name_dict):
    for name in name_dict:
        for i in range(len(name_dict[name]) - 1):
            if name_dict[name][i] > name_dict[name][i+1]:
                return False
            return True

def main():
    names_d = baby_names('names.txt')   

    while True:
        print('Options:')
        print('Enter 1 to search for names.')
        print('Enter 2 to display data for one name.')
        print('Enter 3 to display all names that appear in only one decade.')
        print('Enter 4 to display all names that appear in all decades.')
        print('Enter 5 to display all names that are more popular in every decade.')
        print('Enter 6 to display all names that are less popular in every decade.')
        print('Enter 7 to quit.\n')
        
        #ensures the user does not input letters
        try:
            user = eval(input('Enter choice: '))
        except NameError:
            user = eval(input('Please enter a number between 1-7: '))                        

        if user == 1:
            name = input('Enter a name: ')
            print()
            
            check = name_exists(name, names_d)
            if check == True:
                rank = highest_rank(name, names_d)
                print('The matches with their highest ranking decade are:')
                print(name, rank)
                print()
            else:
                print(name, 'does not appear in any decade')
                print()
                
        if user == 2:
            for name in names_d:
                index = 0
                for i in range(len(names_d[name])):
                    if names_d[name][i] == 1001:
                        names_d[name][i] = 0
                        
            name = input('Enter a name: ')
            print()
            result = name_ranks(name, names_d)

            #ensures that a name in the dictionary is inputted
            #if not, then prompts for another name
            try:
                print(name + ': ' , end='')
                for i in result:
                    print(i, end=' ')
                print()
            except TypeError:
                print('There is no one named', name)
                name = input('Enter another name: ')
                result = name_ranks(name, names_d)
                print(name + ': ' , end='')
                for i in result:
                    print(i, end=' ')
                print()
            finally:
                result = name_ranks(name, names_d)
                                          
            dec = 1900
            for i in names_d[name]:
                print(str(dec)+ ':', i)
                dec += 10
            print()

        if user == 3:
            for name in names_d:
                index = 0
                for i in range(len(names_d[name])):
                    if names_d[name][i] == 1001:
                        names_d[name][i] = 0

            decade = eval(input('Enter decade: '))
            print('The names are in order of rank: ')

            lst = []          

            #skips the names that are ranked 0 and adds the rest to a list
            for name in names_d:
                if decade_rank(name, decade, names_d) == 0:
                    continue
                else:
                    lst.append([name, decade_rank(name, decade, names_d)])

            #bubble sort the ranks
            done = False
            while(not done):
                num_swaps = 0
                for i in range(0,len(lst)-1):
                    if lst[i][1] > lst[i+1][1]:
                        lst[i],lst[i+1] = lst[i+1],lst[i]
                        num_swaps +=1
                if num_swaps ==0 :
                    done = True

            for i in lst:
                print (i[0]+':', i[1])
            print()

        if user == 4:
            for name in names_d:
                index = 0
                for i in range(len(names_d[name])):
                    if names_d[name][i] == 1001:
                        names_d[name][i] = 0
            
            always_names = always_ranked(names_d)

            print(len(always_names), 'names appear in every decade. The names are:')

            for i in always_names:
                print(i)
            print()

        if user == 5:
            for name in names_d:
                index = 0
                for i in range(len(names_d[name])):
                    if names_d[name][i] == 1001:
                        names_d[name][i] = 0
                        
            pop_names = []

            #checks if the entire list is increasing
            for name in names_d:
                check = all(names_d[name][i] > names_d[name][i+1] \
                            for i in range(len(names_d[name]) -1))
                if check == True:
                    pop_names.append(name)

            print(len(pop_names), 'names are more popular in every decade.')

            for i in pop_names:
                print(i)
            print()

        if user == 6:
            less_pop = []
            copy_d = names_d

            for name in copy_d:
                index = 0
                for i in range(len(copy_d[name])):
                    if copy_d[name][i] == 0:
                        copy_d[name][i] = 1001

            #checks if the entire list is decreasing                  
            for name in copy_d:
                check = all(copy_d[name][i] < copy_d[name][i+1] \
                            for i in range(len(copy_d[name]) - 1))
                if check == True:
                    less_pop.append(name)

            print(len(less_pop), 'names are less popular in every decade.')
            for i in less_pop:
                print(i)
            print()

        if user == 7:
            print('\n')
            print('Goodbye.\n')
            break


main()
        
    
