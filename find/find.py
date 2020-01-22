#!/usr/bin/env python3

import re
import os
import typing
import fnmatch


# Use for just single file input without any options.
def find_file(target: str) -> bool:
    if target == ".":
        # If user want use find . , then we just print all files from current direcotry.
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))
        return True
    else:
        for files in os.listdir():
            if files == target:
                print(target)
                return True
    return false


def options(target: str) -> bool:
    if (
        target == "-name"
        or target == "-size"
        or target == "iname"
        or target == "-executable"
        or target == "-gid"
    ):
        return True
    else:
        return False


def main():
    while 1:
        var: str = input(">")
        if len(var) > 4 and var[:4] == "find":
            input_list: list[str] = var[4::].split()
            if len(input_list) == 1:
                if not find_file(input_list[0]):
                    print("find: '%s': No such file or directory" % input_list[0])
            if len(input_list) == 2:
                if not options:
                    for file in input_list:
                        find_file(file)
                else:
                    


if __name__ == "__main__":
    main()
