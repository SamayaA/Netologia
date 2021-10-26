import json

class Wiki_countries :
    def __init__ (self, file_path ):
        self.base = "https://en.wikipedia.org/wiki/" 
        self.file_path = file_path

    def replace_spaces(self, country: str):
        return country.replace(" ", "_")

    def __iter__(self):
        f = open(self.file_path, "r")
        countries_info = json.load(f)
        self.country_link = [i["name"]["common"] for i in countries_info]
        f.close()
        return self

    def __next__(self):
        if not self.country_link:
            raise StopIteration
        country = self.country_link.pop()
        link = country + ' - ' + self.base + \
            self.replace_spaces(country)
        return link

