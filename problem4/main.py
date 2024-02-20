def palindrome(input_string):
    array = [char for char in input_string]
    array_reverse = []
    
    for i in range(len(array) - 1, -1, -1):
       array_reverse.append(array[i])
    my_string = ''.join(array_reverse)
    if my_string == input_string :
       return 'True'
    else : 
        return 'False'


if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False