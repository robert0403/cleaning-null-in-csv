import os
from requests import request
from time import time

def main():
    root_directory = "/mnt/disk/data/tradingview"
    i = 1
    
    for dirpath, dirnames, filenames in os.walk(root_directory):
        print(f"{i} Directory: {dirpath}", end = ": ")
        for filename in filenames:
            print(filename, end = ", ")
        print()
        i+=1
    

if __name__ == "__main__":
    start_ = time()
    main()
    end_ = time()
    print(end_ - start_)