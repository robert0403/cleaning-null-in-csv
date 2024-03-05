# with open("./ttt", 'a') as f:
#     f.write('\0'*1000)
from requests import request
from time import time
def test():
    file_name = "/mnt/disk/data/tradingview/ASX:BMG/60.csv"
    with open(file_name, 'r') as f:
        temp = f.read()
        f.close()
    lines = temp.split('\n')
    # print(lines)
    flag = False
    new_lines = []
    for line in lines:
        if '\0' in line:
            print("error")
            flag = True
        else:
            new_lines.append(line)
            print(line)
    print('\n'.join(new_lines))
    target_file = "new.csv"
    if flag:
        with open(file_name, 'w') as f:
            f.write('\n'.join(new_lines))
            f.close()
if __name__ == "__main__":
    start_ = time()
    test()
    end_ = time()
    print(end_ - start_)