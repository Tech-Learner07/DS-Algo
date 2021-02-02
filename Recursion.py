'''
The 99 Bottles Of Beer On The Wall Using
Recursion.
'''


def bOB(num):
    # 1st Law Of Recursion: A recursive algorithm must have a Base case.
    # Here when num becomes less than 1 the functions stops calling -
    # itself and returns
    if num < 1:
        print("""No more bottles of beer on the wall, No more
              bottles of beer.""")
        return

    bal = num
    # 2nd Law Of Recursion: A recursive algorithm must change it's value -
    # and moves toward the Base case.
    # Here decrementing the variable num moves toward the base case of -
    # num becoming less than 1
    num -= 1
    print(f"""{bal} bottles of beer on the wall. {bal} bootles
              of beer. Take one down, pass it around,
              {num} bottles of beer on the wall.""")

    # 3rd Law Of Recursion: A recursive algorithm must call itself, recursively.
    bOB(num)


bOB(99)
