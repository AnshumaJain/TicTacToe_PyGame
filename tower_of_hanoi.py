"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
The objective of the puzzle is to move the entire stack to another rod,
obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and
placing it on top of another stack i.e. a disk can only be moved if it is
the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.
"""


def hanoi_recursion(n, a, b, c):
    """
    n = total number of discs
    a = source tower
    b = helper tower
    c = destination tower
    """
    if n == 2:
        b.append(a[-1])  # step1
        a.remove(a[-1])
        print(a, b, c)

        c.append(a[-1])  # step2
        a.remove(a[-1])
        print(a, b, c)

        c.append(b[-1])  # step3
        b.remove(b[-1])
        print(a, b, c)

    else:
        hanoi_recursion(n - 1, a, c, b)
        print(a, b, c)

        c.append(a[-1])
        a.remove(a[-1])
        print(a, b, c)

        hanoi_recursion(n - 1, b, a, c)
        print(a, b, c)

    return (a, b, c)


print(hanoi_recursion(5, [5, 4, 3, 2, 1], [], []))
