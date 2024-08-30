arrayA = map(int,input().split(","))
arrayB = map(int,input().split(","))

def remove_dupl(array):
    return set(array)

def union(array1,array2):
    merge_array = array1 + array2
    union_array = merge_array.union()
    return union_array

def intersection(array1, array2):
    merge_array = array1 + array2
    inter_array = merge_array.intersection()
    return inter_array

if __name__ == '__main__':
    print(intersection(arrayA, arrayB))
        