'''
Rename files from a folder
Get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
'''
import os


def rename_files():
    '''
    rename files in a folder
    :return: nothing
    '''
    ispath = r"D:\prankOrig"
    files = os.listdir(ispath)  # returns list
    saved_path = os.getcwd() # save the current directory (folder)
    os.chdir(ispath)
    for file in files:
        # remove digits from name
        new_file=file.lstrip('0123456789')
        print("Old Name: ", file, "  -  New Name: ", new_file)
        # rename file to new_file
        os.rename(file, new_file)

    os.chdir(saved_path)  # return to the saved (current folder)


def main():
    '''
    Test function
    :return: nothing
    '''
    rename_files()


if __name__ == '__main__':
    main()
    exit(0)
