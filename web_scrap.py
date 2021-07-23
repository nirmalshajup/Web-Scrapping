#importing reqired modules

import newspaper

#Assingn url

url = "https://alduinnirmal.github.io/Personal-Website/"

#Extract web data

url_i = newspaper.Article(url="%s" % url, language='en')
url_i.download()
url_i.parse()

#display
print(url_i.text)