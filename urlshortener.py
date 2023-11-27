import random
import string

class URLShortener:
    def __init__(self):
        self.database = {}

    def shorten(self, long_url):
        if long_url in self.database:
            return self.database[long_url]
        
        short_url = "short.ly/" + self.generate_random_string()
        
        while short_url in self.database.values():
            short_url = "short.ly/" + self.generate_random_string()
        
        self.database[long_url] = short_url
        return short_url

    def redirect(self, short_url):
        for long_url, short in self.database.items():
            if short == short_url:
                return long_url
        
        return None

    def generate_random_string(self, length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

shortener = URLShortener()

# Testing the shorten method
short_url_1 = shortener.shorten("https://www.google.com/search?q=codewars")
print("Short URL:", short_url_1)

short_url_2 = shortener.shorten("https://www.moringa.com")
print("Short URL:", short_url_2)

# Testing the redirect method
long_url_1 = shortener.redirect(short_url_1)
print("Long URL:", long_url_1)

long_url_2 = shortener.redirect(short_url_2)
print("Long URL:", long_url_2)
