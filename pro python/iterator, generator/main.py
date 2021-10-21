import os
import hashlib

from wiki_countries import Wiki_countries
# task 1
def hex_generator(path:str):
    with open(path, "r", encoding="utf-8") as file_l:
        line = file_l.readline()
        while line:
            md5_hasher = hashlib.md5()
            md5_hasher.update(line.encode(encoding="utf-8"))
            yield md5_hasher.hexdigest()
            line = file_l.readline()

if __name__ == '__main__':
    path = os.getcwd() + '\\file.txt'
    for string in hex_generator(path):
        print(string)


# task 1

if __name__ == '__main__':
    country_link_f = open("country_wiki.txt", "w+", encoding="utf-8")
    for i in Wiki_countries() :
        country_link_f.write(i)
        country_link_f.write('\n')
    country_link_f.close()