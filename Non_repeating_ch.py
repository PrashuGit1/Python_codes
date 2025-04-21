def f_n_r_str(str):
    for i in str:
        n=0
        n=str.count(i)
        if(n<=1):
            return i
            break

if __name__ == "__main__":
    print(f_n_r_str("ppaddfhh"))