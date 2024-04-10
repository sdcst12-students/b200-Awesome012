#!python3

class integer:
    def __init__(self,a):
        self.numbers1 = a

    def getIntegers(self):
        # myList : expected list or tuple
        # iterate through myList and add all the integers to the new list
        integers = []
        for x in self.numbers1:
            test = x
            test = float(test)
            if test % 1 == 0:
                test = int(test)
                integers.append(test)
        return integers

class cool2:
    def __init__(self,a,b):
        self.numbers1 = a
        self.numbers2 = b

    def getFactor(self):
        # myList : expected list or tuple
        # number : integer
        # iterate through the list and add the number to the list if
        # it is a factor of the number
        factors = []
        for x in self.numbers1:
            if x == 0:
                continue
            test = x
            test = int(test)
            self.numbers2 = int(self.numbers2)
            cool = self.numbers2 % test
            if self.numbers2 % test == 0:
                factors.append(test)
        return factors

class negative:
    def __init__(self,a):
        self.numbers1 = a

    def getNegatives(self):
        # myList : expected list or tuple
        # iterate through myList and add all the negative numbers to the new list
        negatives = []
        for x in self.numbers1:
            test = x
            test = float(test)
            if test < 0:
                negatives.append(test)
        return negatives

class intersections:
    def __init__(self,a,b):
        self.numbers1 = a
        self.numbers2 = b

    def getIntersection(self):
        # list 1: expected list or tuple
        # list 2: expected list or tuple
        # return a sorted list of numbers that is in both lists
        # the intersection of the 2 number sets
        common = []
        for x in self.numbers1:
            if x in self.numbers2:
                common.append(x)
        common.sort
        return common

class union:
    def __init__(self,a,b):
        self.numbers1 = a
        self.numbers2 = b

    def getUnion(self):
        # list 1: expected list or tuple
        # list 2: expected list or tuple
        # return a sorted list of numbers that is in either of the lists
        # duplicate values will be ignored
        union = []
        for x in self.numbers1:
            union.append(x)
        for x in self.numbers2:
            if x in union:
                continue
            else:
                union.append(x)
        union.sort()
        return union   

class merge:
    def __init__(self,a,b):
        self.numbers1 = a
        self.numbers2 = b

    def getMerge(self):
        # list 1: expected list or tuple
        # list 2: expected list or tuple
        # add the elements of list2 into list1
        # if the list2 element is in list1, add it at the position where it occurs in list1
        # if the list2 element is not in list1, add it to the end
        for x in self.numbers2:
            if x in self.numbers1:
                check = self.numbers1.index(x)
                check = int(check)
                self.numbers1.insert(check, x)
            else:
                self.numbers1.append(x)
        return self.numbers1

def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    numberlist1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    numberlist2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    try1 = integer([3,4,1.2,1.3,5])
    try2 = cool2(range(10),12)
    try3 = negative([-3,-1,0,1,4])
    try4 = intersections(easy1,easy2)
    try5 = union(easy1,easy2)
    try6 = merge(easy1,easy2)
    try:
        assert try1.getIntegers() == [3,4,5]
        assert try2.getFactor() == [1,2,3,4,6]
        assert try3.getNegatives() == [-3,-1]
        assert try4.getIntersection() == [2,4,6]
        assert try5.getUnion() == [-6, -4, -2, 0.1, 2, 4, 5, 6, 8, 10, 15]
        assert try6.getMerge() == [5,10,15,2,2,4,4,6,6,8,-2,-4,-6,0.1]
        print("All assertions passed")
    except:
        print("At least 1 assertion failed")

if __name__ == "__main__":
    main()
