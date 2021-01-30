def main():
    n = int(input('number of array elements:'))
    array = sorted(list(map(int, input("Enter array elements:").split())))
    req_sum = int(input('required sum:'))

    start_pointer, end_pointer = 0, n-1
    while start_pointer < end_pointer:
        elem_start = array[start_pointer]
        elem_end = array[end_pointer]
        tot = elem_start + elem_end
        if tot < req_sum:
            start_pointer += 1
        elif tot > req_sum:
            end_pointer -= 1
        else:
            return start_pointer, end_pointer

if __name__ == '__main__':
    t = int(input('test-cases:'))
    while t:
        res = main()
        if res:
            print(f'arr[{res[0]}][{res[1]}] == required_sum')
        else:
            print("No such combination possible")
        t -= 1