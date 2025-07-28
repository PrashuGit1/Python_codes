def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:]) 
    print(w)
    for i in range(1, number+1):
        dec = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:]
        binary = bin(i)[2:]

        print(
            dec.rjust(w),
            octal.rjust(w),
            hexa.rjust(w),
            binary.rjust(w)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)