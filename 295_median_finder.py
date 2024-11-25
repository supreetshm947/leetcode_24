class MedianFinder(object):

    def __init__(self):
        self.nums = set()
        self.count = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.add(num)
        self.count += 1

    def findMedian(self):
        """
        :rtype: float
        """
        ls = list(self.nums)
        mid = self.count // 2
        if self.count % 2 == 0:
            return (ls[mid - 1] + ls[mid]) / 2
        else:
            return ls[mid]

m = MedianFinder()
m.addNum(1)
m.addNum(2)
print(m.findMedian())
m.addNum(3)
print(m.findMedian())