class ADTSet:
    def Add_element(self, val, Set):
        Set.add(val)
        print(val, " is added to set :", Set)

    def Delete_element(self, val, Set):
        Set.remove(val)
        print(val, " is Deleted from set ", Set)

    def Is_contain(self, val, Set):
        if val in Set:
            print(val, " is contains in set :", Set)
        else:
            print(val, " is not contains in set :", Set)

    def Size_of_set(self, Set):
        x = len(Set)
        print("Size of Set :", Set, " is :", x)

    def Union(self, SetA, SetB):
        return SetA.union(SetB)

    def Intersection(self, SetA, SetB):
        return SetA.intersection(SetB)

    def Difference(self, SetA, SetB):
        return SetA.difference(SetB)

    def Is_subset(self, SetA, SetB):
        if SetA.issubset(SetB):
            print("Set A is a subset of Set B")
        else:
            print("Set A is not a subset of Set B")

obj = ADTSet()

a = set()
b = set()

print("Enter elements for Set A (separated by commas): ")
elements_a = input().split(',')
for ele in elements_a:
    a.add(int(ele))

print("Enter elements for Set B (separated by commas): ")
elements_b = input().split(',')
for ele in elements_b:
    b.add(int(ele))

print("Given sets are: \n Set A: ", a, "\n Set B: ", b)

while True:
    print("Select operation to perform: ")
    print("\n1.Add \n2.Remove \n3.Contain \n4.Size \n5.Intersection \n6.Union \n7.Difference \n8.Subset")
    ch = int(input("\nEnter your choice: "))

    if ch == 1:
        s = int(input("Enter the set to add the element (1 for Set A, 2 for Set B): "))
        ele = int(input("Enter the element to add: "))
        if s == 1:
            obj.Add_element(ele, a)
        elif s == 2:
            obj.Add_element(ele, b)

    elif ch == 2:
        s2 = int(input("Enter the set to Delete the element (1 for Set A, 2 for Set B): "))
        ele2 = int(input("Enter the element to Delete: "))
        if s2 == 1:
            obj.Delete_element(ele2, a)
        elif s2 == 2:
            obj.Delete_element(ele2, b)

    elif ch == 3:
        s4 = int(input("Enter the set to check the element (1 for Set A, 2 for Set B): "))
        ele4 = int(input("Enter the element to check: "))
        if s4 == 1:
            obj.Is_contain(ele4, a)
        elif s4 == 2:
            obj.Is_contain(ele4, b)

    elif ch == 4:
        s3 = int(input("Enter the set to check size (1 for Set A, 2 for Set B): "))
        if s3 == 1:
            obj.Size_of_set(a)
        elif s3 == 2:
            obj.Size_of_set(b)

    elif ch == 5:
        print("Intersection of the sets A and B is :", obj.Intersection(a, b))

    elif ch == 6:
        print("Union of the sets A and B is :", obj.Union(a, b))

    elif ch == 7:
        print("Difference of the sets A and B is :", obj.Difference(a, b))
        print("Difference of the sets B and A is :", obj.Difference(b, a))

    elif ch == 8:
        s5 = int(input("Enter the set to check the Subset or not (1 for Set A, 2 for Set B): "))
        if s5 == 1:
            obj.Is_subset(a, b)
        elif s5 == 2:
            obj.Is_subset(b, a)
