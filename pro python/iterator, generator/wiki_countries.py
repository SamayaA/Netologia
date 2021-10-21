import json

class Wiki_countries :
    def __init__ (self):
        self.base = "https://en.wikipedia.org/wiki/" 

    def replace_spaces(self, country: str):
        return country.replace(" ", "_")

    def __iter__(self):
        f = open("countries.json", "r")
        countries_info = json.load(f)
        self.country_link = [i["name"]["common"] + ' - ' + self.base + \
            self.replace_spaces(i["name"]["common"]) for i in countries_info]
        f.close()
        return self

    def __next__(self):
        if not self.country_link:
            raise StopIteration
        link = self.country_link.pop()
        return link

