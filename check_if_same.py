#Check if the first and last numbers of a list are the same
def check_if_same(list):
    if list[0] == list[-1]:
        return True
    return False

print(check_if_same([10, 20, 30, 40, 53]))