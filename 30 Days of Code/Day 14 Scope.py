class Difference:

    def __init__(self, a):
        self.__elements = a

        # Add your code here
        self.maximumDifference = 0

    def computeDifference(self):
        minimum = self.__elements[0]
        maximum = self.__elements[0]
        for i in range(len(a)):
            if minimum > self.__elements[i]:
                minimum = self.__elements[i]
            if maximum < self.__elements[i]:
                maximum = self.__elements[i]
        difference = maximum - minimum
        self.maximumDifference = difference

# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
