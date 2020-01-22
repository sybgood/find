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
    return False


def nameSearch(target: str) -> list[str]:
    fileList = []
    for root, dirs, files in os.walk(os.getcwd()):
        x = [os.path.join(root, name)
             for name in dirs+files if fnmatch.fnmatchcase(name, target)]
        fileList += x
    return fileList


def inameSearch(target: str) -> list[str]:
    fileList = []
    for root, dirs, files in os.walk(os.getcwd()):
        x = [os.path.join(root, name)
             for name in dirs+files if fnmatch.fnmatch(name, target)]
        fileList += x
    return fileList


def sizeSearch(size: int) -> list[str]:  # size repersent 512b*size space.
    


def options(target_list: List[str]) -> bool:
    if len(target_list) == 2:
        target: str = target_list[0]
        k = 1
    if len(target_list) == 4:
        target: str = target_list[2]
        k = 3
    if target == "-name":
        filelist: list[str] = nameSearch(target_list[k])
    if target == "-size":

    if target == "iname":
        filelist: list[str] = inameSearch(target_list[k])
    if target == "-executable":

    if target == "-gid":
    
        return True
    else:
        return False


def main():
    while 1:
        var: str = input(">")
        if len(var) > 4 and var[:4] == "find":
            input_list: list[str] = var[4::].split()
            if len(input_list) == 1:
                if input_list[0] == "-executable":
                    
                if not find_file(input_list[0]):
                    print("find: '%s': No such file or directory" % input_list[0])
            if len(input_list) == 2:
                suc: bool = options(input_list)
                if not suc:
                    for file in input_list:
                        find_file(file)


if __name__ == "__main__":
    main()
