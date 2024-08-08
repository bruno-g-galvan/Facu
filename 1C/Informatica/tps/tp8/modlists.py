import random

#Genera una lista de N valores aleatorios entre start y end. 
def generate_random_lst(start, end, lenght):
    lst = []
    for _ in range(lenght):
        random_number = random.randint(start, end)
        lst.append(random_number)
    
    return lst

def rep_in_lst(lst):
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
            

def num_in_lst(num, lst):
    for i in range(0, len(lst)):
        if lst[i] == num:
            return True
        
    return False

def num_in_lst_index(num, lst):
    for i in range(0, len(lst)):
        if lst[i] == num:
            return i
        
    return -1

def bin_search_val(num, lst):
    start = 0
    end = len(lst)
    while start < end:
        mid = int((start + end) / 2)
        if lst[mid] == num:
            return True
        elif lst[mid] > num:
            end = mid
        else:
            start = mid + 1
    return False