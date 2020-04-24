import bible_api as ba
import json
import pandas as pd

# Requests a list of books based on a given DAM_ID
books_ot = ba.book_listing('7b1efc5d23b2458b2f08e785a2cd1e6a', 'ENGKJVO1ET')
books_nt = ba.book_listing('7b1efc5d23b2458b2f08e785a2cd1e6a', 'ENGKJVN1ET')

# Merges Old and New Testament JSON Objects.
books = books_ot + books_nt

# Creates a list of dicts containing Book_Index, Book_Order,
book_list = []
for i, book in enumerate(books):
    book_list.append(
        {'Book_Index': i, 'Chapter_Count': book['number_of_chapters']})

df = pd.DataFrame(book_list)

df.to_csv('Data/books.csv')
