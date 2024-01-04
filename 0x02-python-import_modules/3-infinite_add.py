#!/usr/bin/python3
if _name_ == "_main_":
    from sys import argv
    sum = 0
    for argue in argv[1:]:
        sum += int(argue)

    print("{:d}".format(sum))
