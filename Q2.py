arrayA = list(map(int,input().split(",")))
arrayB = list(map(int,input().split(",")))

def remove_dupl(array):
    return set(array)

def union(array1,array2):
    union_array = array1.union(array2)
    return union_array

def inter(array1, array2):
    inter_array = array1.intersection(array2)
    return inter_array

if __name__ == '__main__':
    print(list(inter(set(arrayA), set(arrayB))))
        