def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("nhập ds các số, cách nhau bằng dấu phẩy:" )
numbers = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("list sau khi đảo ngược là:", list_dao_nguoc)