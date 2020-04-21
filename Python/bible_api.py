import requests
import json


def dam_id(language_code, version_code, collection, drama_type, media_type):
    # Generates a DAM ID to be used in requesting the Bible API.
    # The parameters for this function can be found by searching on https://www.digitalbibleplatform.com/bibles/
    dam_id = language_code + version_code + collection + drama_type + media_type

    return dam_id


def language_listing(key, language_name):
    # Retrieves a JSON-formatted list of languagues based on a give language name in English.
    response = requests.get(
        'https://dbt.io/library/language?key=' + key + '&name=' + language_name + '&v=2').json()

    return response


def book_listing(key, dam_id):
    # Retrieves a JSON-formatted list of Bible books based on a given language code.
    response = requests.get(
        'https://dbt.io/library/book?key=' + key + '&dam_id=' + dam_id + '&v=2').json()

    return response


def get_book(key, dam_id, book_id):
    # Retrieves a JSON formated Bible book.
    response = requests.get('https://dbt.io/text/verse?key=' + key + '&dam_id=' +
                            dam_id + '&book_id=' + book_id + '&v=2').json()

    return response


def get_chapter(key, dam_id, book_id, chapter_id):
    # Retrieves a JSON formatted selection of a chapter from a Bible book.
    response = requests.get('https://dbt.io/text/verse?key=' + key + '&dam_id=' +
                            dam_id + '&book_id=' + book_id + '&chapter_id=' + chapter_id + '&v=2').json()

    return response


def get_verse(key, dam_id, book_id, chapter_id, verse_start, verse_end):
    # Retrieves a JSON formatted selection of Bible verses.
    response = requests.get(
        'https://dbt.io/text/verse?key=' + key + '&dam_id=' + dam_id + '&book_id=' + book_id + '&chapter_id=' + chapter_id + '&verse_start=' + verse_start + '&verse_end=' + verse_end + '&v=2').json()

    return response


def search_group(key, dam_id, query):
    # Searches the Bible based on a given query.
    # Returns total results, results per book and the first result in every book.
    response = requests.get('https://dbt.io/text/searchgroup?key=' +
                            key + '&dam_id=' + dam_id + '&query=' + query + '&v=2').json()

    return response
