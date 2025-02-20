class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prod = []

    def add(self, num: int) -> None:
        self.nums.append(num)
        self.prod = list(map(lambda x:x*num, self.prod))+[num]

    def getProduct(self, k: int) -> int:
        return self.prod[-k]

obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
param_2 = obj.getProduct(2)
print(param_2)
param_2 = obj.getProduct(3)
print(param_2)
param_2 = obj.getProduct(4)
print(param_2)
obj.add(8)
param_2 = obj.getProduct(2)
print(param_2)