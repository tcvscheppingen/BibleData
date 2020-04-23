import requests
from bs4 import BeautifulSoup


def get_commentary(response):
    # Returns a Bible commentary and cross-text references from a GET-response.

    # Parses the response using an HTML-parser
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finds all 'article'-tags with the class 'library'
    # This contains the Bible commentary and it's cross-text references.
    results = soup.find_all('article', class_='library')

    # Creates a list to hold all URL's containing a cross-text reference.
    references = []

    for result in results:
        # Assigns the result, without HTML tags, found with soup.find_all, to a variable.
        text = result.text

        # Finds all anchor-tags in the result and appends it's 'href'-attribute to the 'references'-list.
        for a in result.find_all('a', href=True):
            if 'http' in a['href']:
                references.append(a['href'])

    return text, references


def commentary_parameters(commentary, book, chapter):
    # Returns a Bible commentary and cross-text references, based on a given commentary, book and chapter.
    # A list of commentaries can be found on https://www.biblestudytools.com/commentaries/
    url = ('https://www.biblestudytools.com/commentaries/' + commentary + '/' +
           book + '/' + chapter + '.html')

    # Sends a GET-request to the URL specified above.
    response = requests.get(url)

    # Gets the Bible commentary and cross-text references from the response using the get_commentary() method.
    text, references = get_commentary(response)

    return text, references


def commentary_url(url):
    # Returns a Bible commentary and cross-text references from a given URL.
    response = requests.get(url)

    # Gets the Bible commentary and cross-text references from the response using the get_commentary() method.
    text, references = get_commentary(response)

    return text, references


tekst, linkjes = commentary_parameters(
    'matthew-henry-complete', 'exodus', '20')
print(tekst)
for link in linkjes:
    print(link)
