# from_brainyquote.py
# this file contains functions to get quotes from barinyquote.com

from bs4 import BeautifulSoup
from requests import get
from random import randint, shuffle

def get_quotes(type, total=1):
    """
    Returns a python list of quotes.
    :param type: one of 'motivational', 'positive', 'friendship', 'life', 'success', 'happiness'
    :param total: total quotes of this type to return. Default is 1
    :return: a list containing number_of_quotes quotes
    """
    url = "http://www.brainyquote.com/quotes/topics/topic_" + type + ".html"
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    for quote in soup.find_all('a', {'title': 'view quote'}):
        quotes.append(quote.contents[0])
    quotes_size = len(quotes)
    if quotes_size < total:
        return quotes
    shuffle(quotes)
    send = []
    for i in range(total):
        send.append(quotes[i])
    return send

def get_quote_of_day():
    """
    Returns a list of "Quote of the Day"
    :return: a list of "Quote of the Day"
    """
    url = "https://www.brainyquote.com/quotes_of_the_day.html"
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    for quote in soup.find_all('a', {'title': 'view quote'}):
        quotes.append(quote.contents[0])
    quotes_size = len(quotes)
    shuffle(quotes)
    return quotes

def get_random_quote():
    choices = ['motivational', 'life', 'positive', 'friendship', 'success', 'happiness']
    result = get_quotes(choices[randint(0, len(choices) - 1)])
    return result


