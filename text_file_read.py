import glob


def search_and_readtxt():
    search_txt = glob.glob('*.txt')
    for txt_file in search_txt:
        with open(txt_file) as file:
            file_content = file.read()
            print(file_content)


if __name__ == '__main__':
    search_and_readtxt()
