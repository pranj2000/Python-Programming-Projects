#  File: EvenMagicSquare.py

#  Description: Permutation of 4 by 4 Magic Squares

#  Student Name: Pranjal Jain   

#  Student UT EID: pj5775

#  Partner Name: Vivian Chang

#  Partner UT EID: vc8969

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 10/15/19

#  Date Last Modified: 10/16/19


def permute (a, lo, hi):
    stop = True
        
    if (lo == hi):
        sr1 = sum(a[0:4])
        
        if sr1 == 34:
            sr2 = sum(a[4:8])

            if sr2 == 34:
                sr3 = sum(a[8:12])
           
                if sr3 == 34:
                    sr4 = sum(a[12:16])
                
                    if sr4 == 34:
                        sc1 = a[0]+a[4]+a[8]+a[12]
                        sc2 = a[1]+a[5]+a[9]+a[13]
                        sc3 = a[2]+a[6]+a[10]+a[14]
                        sc4 = a[3]+a[7]+a[11]+a[15]
            
                        if sc1 == 34 and sc2 == 34 and sc3 == 34 and sc4 == 34:
                            sd1 = a[12]+a[9]+a[6]+a[3]
                            sd2 = a[0]+a[5]+a[10]+a[15]
                            
                            if sd1 == 34 and sd2 == 34:
                                print (a)

                            else:
                                for i in range (lo, hi):
                                    a[i], a[lo] = a[lo], a[i]
                                    permute (a, lo + 1, hi)
                                    a[i], a[lo] = a[lo], a[i]
                        else:
                            for i in range (lo, hi):
                                a[i], a[lo] = a[lo], a[i]
                                permute (a, lo + 1, hi)
                                a[i], a[lo] = a[lo], a[i]
                    else:
                        for i in range (lo, hi):
                            a[i], a[lo] = a[lo], a[i]
                            permute (a, lo + 1, hi)
                            a[i], a[lo] = a[lo], a[i]           
                else:
                    for i in range (lo, hi):
                        a[i], a[lo] = a[lo], a[i]
                        permute (a, lo + 1, hi)
                        a[i], a[lo] = a[lo], a[i]
            else:
                for i in range (lo, hi):
                    a[i], a[lo] = a[lo], a[i]
                    permute (a, lo + 1, hi)
                    a[i], a[lo] = a[lo], a[i]
        else:
            for i in range (lo, hi):
                a[i], a[lo] = a[lo], a[i]
                permute (a, lo + 1, hi)
                a[i], a[lo] = a[lo], a[i]
    else:
        for i in range (lo, hi):
            a[i], a[lo] = a[lo], a[i]
            permute (a, lo + 1, hi)
            a[i], a[lo] = a[lo], a[i]


def main():
    a = [1, 2, 15, 16, 12, 14, 3, 5, 13, 7, 10, 4, 8, 11, 6, 9] 

    permute(a, 0, 16)

main()
