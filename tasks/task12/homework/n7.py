def main():
    #  01    02  03
    # 33120 3120 20 
    s = '01'
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '302', 1)
        s = s.replace('02', '3103', 1)
        s = s.replace('03', '20', 1)
    print(s)


main()