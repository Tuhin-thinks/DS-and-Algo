import sys
from colorama import Fore


dividend = 100100
divisor = 1101

def compare(a, b)->str:
    res = ""

    for e1, e2 in zip(a, b):
        if e1 == e2:
            res += '0'
        else:
            res += "1"

    return res

def modify_dividend(divisor, dividend):
    return f"{dividend}{(len(str(divisor))-1) * '0'}"


def division(dividend, divisor):
    # modify dividend
    
    len_divisor = len(str(divisor))  # store the length of the divisor
    
    # dividend:str = str(dividend) + "0" * (len_divisor -1)
    divisor:str = str(divisor)

    len_dividend = len(dividend)

    print(f"{Fore.CYAN}\nFinal dividend:{dividend}\ndivisor:{divisor}\n{Fore.RESET}")

    pointer_pos:int = 0
    rem:str = ""
    quotient:str = ""
    first_iteration = True
    compare_a:str = ""

    while pointer_pos < len_dividend:
        if ((len_dividend - pointer_pos) + len(compare_a)) < len(divisor):
            chunk = dividend[pointer_pos:]
            quotient += "0" * (len(chunk)-1)
            rem = compare_a + chunk
            break


        print(f"{Fore.LIGHTMAGENTA_EX}pointer_pos={pointer_pos}{Fore.RESET}", end=" compare_a=")
        if first_iteration:
            elem_now = dividend[:len_divisor]
            pointer_pos = len_divisor - 1
            first_iteration = False
        else:
            elem_now = dividend[pointer_pos]

        compare_a += elem_now
        print(int(compare_a), end=" ")
        if len(compare_a) == len_divisor:
            last_rem = compare(compare_a, divisor)
            compare_a = str(int(last_rem))
            quotient += '1'
            if compare_a == '0':
                compare_a = ""
            rem = last_rem
        else:
            quotient += '0'

        print(f"rem: {int(rem)}")
        pointer_pos += 1
    print(f"{Fore.RED}Final rem:{rem}{Fore.LIGHTWHITE_EX} Quotient:{quotient}{Fore.RESET}")

    len_crc = len_divisor - 1
    final_rem = rem[-len_crc:]

    if mode == 'find':
        print(f"\n{Fore.LIGHTYELLOW_EX}CRC: {final_rem}{Fore.RESET}")
        data_to_transmit = dividend[:-len_crc] + final_rem
        print(f"{Fore.LIGHTYELLOW_EX}Data to be transmitted:{data_to_transmit}{Fore.RESET}")
    else:
        if int(final_rem) == 0:
            print("No Error in transmission.")
            print(f"Original Data: {dividend[:-len_crc]}")
        else:
            print(f"error in data transmission, final remainder: {Fore.LIGHTRED_EX}{final_rem}{Fore.RESET}")

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        mode = "find"
    else:
        mode = "check"
    dividend = input("Enter data:")
    divisor = input("Enter the key:")
    if mode == "check":
        pass
    else:
        dividend = modify_dividend(divisor, dividend)
    division(dividend, divisor)