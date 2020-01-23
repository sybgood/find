#!/usr/bin/env python3

import re
import os
import typing
import fnmatch


# Use for just single file input without any options.
def find_file(target: str) -> bool:
    if target == ".":
        # If user want use find . , then we just print all files from current directory.
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
    

def decideSearchType(target_list: list[str]):
    option: str = target_list[0]
    if option == "-name":
        filelist: list[str] = nameSearch(target_list[1])
    if option == "-size":
        
    if option == "iname":
        filelist: list[str] = inameSearch(target_list[1])
    if option == "-executable":

    if option == "-gid":

    else: 
        return False
def options(target_list: List[str]) -> bool:
    # A legal gramma should be Find opiton target or Find target1 target2
    if len(target_list) == 2:
        return decideSearchType(target_list)
    # Find target_directory option target
    if len(target_list) == 3:
        try:
            os.chdir(target_list[0])
            target_list
            decideSearchType(target_list[1:])
        except FileNotFoundError:
            return False
        return True
    else:
        return False


def main():
    while 1:
        var: str = input(">")
        if len(var) > 4 and var[:4] == "find":
            input_list: list[str] = var[4:].split()
            if len(input_list) == 1:
                if input_list[0] == "-executable":
                    
                if not find_file(input_list[0]):
                    print("find: '%s': No such file or directory" % input_list[0])
            else:
                suc: bool = options(input_list)
                if not suc:
                    for file in input_list:
                        find_file(file)


if __name__ == "__main__":
    main()
