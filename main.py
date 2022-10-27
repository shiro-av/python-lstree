import os, sys, stat, time

from pathlib import Path

file_count = dir_count = 0


class bcolors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def lstree(path, level=0):
    global file_count, dir_count
    for file in os.listdir(path):
        new_path = path + '/' + file
        if os.path.isdir(new_path):
            dir_count += 1
            offset = ' ' * 4 * (level + 1)
            print_file_info(new_path, offset)
            os.chdir(new_path)

            lstree(new_path, level+1)
            os.chdir('..')
            #level-=1
        else:
            file_count += 1

            offset = ' ' * 4 * (level+1)
            print_file_info(new_path, offset)


def print_file_info(path, offset=''):
    p = Path(path)
    stat_info = os.stat(path)
    # for i in stat_info:
    #    print(i)
    if os.path.isfile(path):
        print(f'{offset}{stat.filemode(stat_info[0])} {p.owner()} {p.group()} {stat_info.st_size}B '
              f'{time.ctime(stat_info.st_mtime)} {bcolors.RED} {p.name} {bcolors.RESET}')
    else:
        print(f'{offset}{stat.filemode(stat_info[0])} {p.owner()} {p.group()} {stat_info.st_size}B '
              f'{time.ctime(stat_info.st_mtime)} {bcolors.GREEN} {p.name} {bcolors.RESET}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        path = os.path.abspath(os.getcwd())
    else:
        path = sys.argv[1]
    print_file_info(path)
    print('-----------------------------------------------------------')
    lstree(path)
    print(f'dirs: {dir_count} | files: {file_count}')
