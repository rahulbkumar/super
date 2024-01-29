
import random
test1 = [random.randint(-10,10) for r in range(10)]
print(test1)

def SumThree1(num_list):
    if len(num_list)<3:
        summed = 'List too small'
        return summed
    sorted_list = sorted(num_list)
    sumed = sorted_list[-3] * sorted_list[-2] * sorted_list[-1]
    return sumed

def SumThree2(num_list):
    if len(num_list)<3:
        summed = 'List too small'
        return summed
    summed = 1
    for i in range(3):
        largest = max(num_list)
        num_list.remove(largest)
        summed = summed * largest
    return summed   

print(SumThree1(test1))
print(SumThree2(test1))
