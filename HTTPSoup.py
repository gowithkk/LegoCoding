from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html><head><title>test123</title>
</head>
<body>

<h1>My First Heading</h1>
<p class="title">My first paragraph.</p>
<p class="text">My second paragraph.</p>
<p class="paragraph">My third paragraph.</p>
</body>
</html>
"""

# Parse HTML code
soup = BeautifulSoup(html_doc, 'html.parser')

# # Parse HTML file
# with open('html_01.html', 'r') as f:
#     html = f.read()
# soup = BeautifulSoup(html, 'html.parser')

print(soup)

# prettify html (better structure)
print(soup.prettify())

# get title
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# get a specific value
print(soup.p['class'])
print(soup.p.get('class'))

# get all the value
print(soup.find_all('p')) # returns a list
print(soup.find('class="title"'))


for link in soup.find_all('p'):
    print(link.get('href'))


# get all texts
print(soup.get_text())

# return all the methods of soup
print(dir(soup))