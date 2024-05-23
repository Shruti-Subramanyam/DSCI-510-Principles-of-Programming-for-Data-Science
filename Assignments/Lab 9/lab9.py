import requests
import re
from bs4 import BeautifulSoup


def word_frequency_in_text(url: str, word_to_search: str) -> int:
    try:
        response = requests.get(url)
        if response.status_code > 199 and response.status_code < 300:
            text = re.sub(r"[^a-zA-Z'\d\s]", "", response.text)
            word_list = text.split()
            print(word_list)
            return word_list.count(word_to_search)
        else:
            raise Exception("Failed to fetch content from url")
    except Exception as e:
        raise Exception("Error occurred", e)


def analyze_quotes(url: str) -> dict:
    quotes_dict = {}
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = BeautifulSoup(response.content, "html.parser")
        quote_elements = data.find_all(class_="quote")
        for quote_element in quote_elements:
            quote_text_element = quote_element.find(class_="text")
            quote_text = (
                quote_text_element.get_text(strip=True) if quote_text_element else None
            )
            author_name_element = quote_element.find(class_="author")
            author_name = (
                author_name_element.get_text(strip=True)
                if author_name_element
                else None
            )
            if quote_text and author_name:
                if author_name in quotes_dict:
                    quotes_dict[author_name].append(quote_text)
                else:
                    quotes_dict[author_name] = [quote_text]
        return quotes_dict

    except Exception as e:
        raise Exception("Error occurred", e)
