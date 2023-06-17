list  = [5,3,2,8,7,4]

print("List before swapping ",list)

def swap_lst(lt):
    x = len(lt)
    a = lt[0]
    lt[0] = lt[x-1]
    lt[x-1] = a
    
    return lt

print("List after swapping ",swap_lst(list))