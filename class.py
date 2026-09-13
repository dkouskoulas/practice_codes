

class array_methods:
    def __init__(self, factor, denominator):
        self.factor = factor
        self.denominator = denominator 


    def amplify(self, arr):
        return [self.factor * x for x in arr]
    
    def shrink(self, arr):
        return [x / self.denominator for x in arr]
    

arr = [1, 5, 2, 3, 6]

obj = array_methods(5, 2)
print("Amplify:", obj.amplify(arr))
print("Shrink:", obj.shrink(arr))