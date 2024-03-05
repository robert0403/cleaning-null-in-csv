import os
from time import time
import logging
def clean(file_name,logger):
    
    with open(file_name, 'r') as f:
        temp = f.read()
        f.close()
    lines = temp.split('\n')
    
    flag = False
    new_lines = []
    for line in lines:
        if '\0' in line:
            flag = True
        else:
            new_lines.append(line)
    if flag:
        logger.warning(f"Cleaning {file_name}")
        with open(file_name, 'w') as f:
            f.write('\n'.join(new_lines))
            f.close()
        logger.warning(f"success Cleaned {file_name}")

def main():
    logger = logging.getLogger("clean")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler("logs/clean.log")
    loggger_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")   
    file_handler.setFormatter(loggger_formatter)
    logger.addHandler(file_handler)
    warning_file = "logs/warnings.log"
    warning_handler = logging.FileHandler(warning_file)
    warning_handler.setLevel(logging.WARNING)
    warning_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    warning_handler.setFormatter(warning_formatter)
    logger.addHandler(warning_handler)
    
    root_directory = "/mnt/disk/data/tradingview"
    i = 1
    
    for dirpath, dirnames, filenames in os.walk(root_directory):
        start_ = time()
        logger.info(f"{i} Directory: {dirpath}")
        for filename in filenames:
            target_file = os.path.join(root_directory,dirpath, filename)
            clean(target_file,logger)
        i+=1    
        end_ = time()
        logger.info(f"Time taken: {end_ - start_}")

if __name__ == "__main__":
    start_ = time()
    main()
    end_ = time()
    print(end_ - start_)