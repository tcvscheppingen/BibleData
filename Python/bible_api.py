import requests
import json


def dam_id(key, language_code):
    # Retrieves a list of Bible translations available for a given language based on a given language code.
    response = requests.get('https://dbt.io/library/volume?key=' +
                            key + '&language_code=' + language_code + '&v=2').json()

    # Creates a list to store dictionaries containing the names and DAM_IDs of retrieved Bible translations
    translations = []

    # Ranges over the response and stores the name of the version (volume_name) and its corresponding DAM_ID in a list of dictionaries.
    for version in response:
        translations.append(
            {'Version name': version['volume_name'], 'DAM_ID': version['dam_id']})

    # Returns a list of dictionaries
    return translations


def version_listing(key, language_code):
    # Retrieves a list of all Bible translations for a given language based on a language code.
    # The list contains general information for each translation in JSON format.
    response = requests.get('https://dbt.io/library/volume?key=' +
                            key + '&language_code=' + language_code + '&v=2').json()

    # Returns a JSON object.
    return response


def language_listing(key, language_name):
    # Retrieves a JSON-formatted list of languagues based on a give language name in English.
    response = requests.get(
        'https://dbt.io/library/language?key=' + key + '&name=' + language_name + '&v=2').json()

    # Returns a JSON object.
    return response


def book_listing(key, dam_id):
    # Retrieves a JSON-formatted list of Bible books based on a given language code.
    response = requests.get(
        'https://dbt.io/library/book?key=' + key + '&dam_id=' + dam_id + '&v=2').json()

    # Returns a JSON object.
    return response


def get_book(key, dam_id, book_id):
    # Retrieves a JSON formated Bible book.
    response = requests.get('https://dbt.io/text/verse?key=' + key + '&dam_id=' +
                            dam_id + '&book_id=' + book_id + '&v=2').json()

    # Returns a JSON object.
    return response


def get_chapter(key, dam_id, book_id, chapter_id):
    # Retrieves a JSON formatted selection of a chapter from a Bible book.
    response = requests.get('https://dbt.io/text/verse?key=' + key + '&dam_id=' +
                            dam_id + '&book_id=' + book_id + '&chapter_id=' + chapter_id + '&v=2').json()

    # Returns a JSON object.
    return response


def get_verse(key, dam_id, book_id, chapter_id, verse_start, verse_end):
    # Retrieves a JSON formatted selection of Bible verses.
    response = requests.get(
        'https://dbt.io/text/verse?key=' + key + '&dam_id=' + dam_id + '&book_id=' + book_id + '&chapter_id=' + chapter_id + '&verse_start=' + verse_start + '&verse_end=' + verse_end + '&v=2').json()

    # Returns a JSON object.
    return response


def search_group(key, dam_id, query):
    # Searches the Bible based on a given query.
    # Returns total results, results per book and the first result in every book.
    # '+' can be used for AND, '|' can be used for OR in queries.
    response = requests.get('https://dbt.io/text/searchgroup?key=' +
                            key + '&dam_id=' + dam_id + '&query=' + query + '&v=2').json()

    # Returns a JSON object.
    return response


def search(key, dam_id, query):
    # Searches the Bible based on a given query.
    # Returns total results and each individual verse containing a result.
    # '+' can be used for AND, '|' can be used for OR in queries.
    response = response = requests.get('https://dbt.io/text/search?key=' +
                                       key + '&dam_id=' + dam_id + '&query=' + query + '&v=2').json()

    # Returns a JSON object.
    return response
