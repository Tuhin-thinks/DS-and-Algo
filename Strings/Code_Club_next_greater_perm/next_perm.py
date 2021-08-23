import math
def next_large_number ( number) :
    number_arr = []
    number_length = 0
    # converting the number into an array with integer elements

    # Note: this will be a reverse array of the desired number so you have to
    # reverse the array after the calculation is done
    while number != 0:
        number_arr . append (number % 10)
        number = math. trunc (number/10)
        number_length += 1

    number_arr = number_arr[: : -1] # reversing the array
    
    # from the back, checking if the last most number is greater than the one
    # before it. If it is, swap, else ignore.
    for i in range(number_length - 1, -1, -1):
    # second loop to check every element
        for j in range(i - 1, -1, -1) :
            if number_arr[i] > number_arr[j]:
                number_arr[i], number_arr[j] = number_arr[j], number_arr[i]
                # changing the contents of the array into an integer
                # if you do the string method, it'll prolly take some time

                # calculation is preferred for better memory management
                number_arr = number_arr[ :j + 1] + sorted(number_arr[j+1:])
                counter_variable = 1
                result = 0
                for k in range (number_length) :

                    result += number_arr[k] * (10 ** (number_length - counter_variable) )
                    counter_variable += 1
                return result
    
    return "No next permutation possible"

if __name__ == "__main__":
    given_num = int (input ("Please enter a number: ") )
    print (next_large_number (given_num) )
