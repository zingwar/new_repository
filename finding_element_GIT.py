'''
def dict_work(element,path,result):
    for key,value in element.items():
        if value == result:
            print("Знайшли елемент")
            return path + [key]
        if type(value) == dict:
            return dict_work(value,path + [key],result)
        if type(element) == list:
            return list_work(element,path,result)
        
def find_element(data,result):
    def work_with_element(element,path):
        print(f"{element} -- {path}")
        if type(element) == dict:
            return dict_work(element,path,result)
    return work_with_element(data,[])


data = {"1":1,"2":{"3":"4","5":{"tmp":155}}}
print(find_element(data,155))
'''








'''
def find_element(data,result):
    print(f"Шукаємо елемент {result} у стурктурі {data}")

    def local_finding(element,path):
        print(f"Шлях де шукаємо {path} що шукаємо {result}")
        for key,value in element.items():
            if value == result:
                return path + [key]
            if type(value) == dict:
                return local_finding(value,path + [key])

    return local_finding(data,[])

data = {"1":"1","2":"2","3":"3","14":{"11":11,"12":12,"155":155}}
result = find_element(data,155)
print(f"Шлях до елементу {result}")
'''
'''
data = [1,2,1,2,1,2,1,155]
for index,value in enumerate(data):
    if value == result:
        return path + [index]
    if type(value) == list:
        return local_finding(value,path + [index])
'''
# data = [3,1,2,3,5,6,78,8]
# відсуртувати від найменьшого до найбільшого
# без використання sort і sorted
'''
import random
import datetime

def bubble_sort(data):
    for start_index in range(len(data)):
        #print(f"Ми порівнюємо {data[start_index]}")
        for second_index in range(len(data)):
            #print(f"Порівнюємо із {data[second_index]}")
            if data[second_index] > data[start_index]:
                data[start_index],data[second_index] = data[second_index],data[start_index]
    # print(data)
    
data = [random.randint(1,10000) for _ in range(10)]
data2 = [random.randint(1,10000) for _ in range(10)]

start = datetime.datetime.now()
bubble_sort(data)
end = datetime.datetime.now()
print(end-start)
'''
'''
def quick_sort(data):
    if len(data) <= 1:
        return data
    left,center,right = [],[],[]
    center_element = data[0]
    for element in data:
        if element < center_element:
            left.append(element)
        if element == center_element:
            center.append(element)
        if element > center_element:
            right.append(element)
            
    return quick_sort(left)  + center  +  quick_sort(right)

start = datetime.datetime.now()
quick_sort(data2)
end = datetime.datetime.now()
print(end-start)
'''
# 1 ЗА ЧАСОМ
# 2 ЗА КІЛКІСТЮ ОПЕРАЦІЙ
# O нотація

# Кільк - прямує до нескінченності
# O(5) = 1
# O(n)

# N * N  ==   ( N ** 2)





