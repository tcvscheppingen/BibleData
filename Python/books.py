import bible_api as ba
import json
import pandas as pd

translations = ba.dam_id('7b1efc5d23b2458b2f08e785a2cd1e6a', 'ENG')
for translation in translations:
    print(translation)


books_ot = ba.book_listing('7b1efc5d23b2458b2f08e785a2cd1e6a', 'ENGKJVO1ET')
books_nt = ba.book_listing('7b1efc5d23b2458b2f08e785a2cd1e6a', 'ENGKJVN1ET')

books = books_ot + books_nt

book_list = []
for book in books:
    book_list.append(
        {'Book_Index': book['book_order'], 'Book_Id': book['book_id'], 'Chapter_Count': book['number_of_chapters']})

df = pd.DataFrame(book_list)

df.to_csv('Data/books.csv')
