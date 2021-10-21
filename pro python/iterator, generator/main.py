from wiki_countries import Wiki_countries
if __name__ == 'main':
    country_link_f = open("country_wiki.txt", "w+", encoding="utf-8")
    for i in Wiki_countries() :
        country_link_f.write(i)
        country_link_f.write('\n')
    country_link_f.close()