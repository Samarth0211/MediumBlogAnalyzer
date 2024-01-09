import os,re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources (run this once)
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')


def extract_blog_title(blog_link):
    # Extract the path from the URL and split it to get the last part
    path = urlparse(blog_link).path
    blog_title = path.split("/")[-1]

    # Remove dashes and the last set of numbers
    cleaned_title = blog_title.replace("-", " ").rsplit("-", 1)[0]

    # Trim the last 12 characters and convert to sentence case
    final_title = cleaned_title[:-12].replace("-", " ").upper()

    return final_title


def fetch_and_store_paragraphs(blog_link, output_folder):
    # Fetch content from the blog link
    response = requests.get(blog_link)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract paragraphs
    paragraphs = [re.sub(r'[^a-zA-Z0-9\s]', '', p.get_text()) for p in soup.find_all('p')]

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Store cleaned paragraphs in a text file
    output_file = os.path.join(output_folder, f"{extract_blog_title(blog_link)}_cleaned_paragraphs.txt")
    with open(output_file, 'w', encoding='utf-8') as file:
        for paragraph in paragraphs:
            file.write(paragraph + '\n')

    return output_file


def remove_stopwords(input_file, output_file):
    stop_words = set(stopwords.words('english'))

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            words = line.split()
            words = [word.lower() for word in words if word.lower() not in stop_words]
            outfile.write(' '.join(words) + '\n')

    return output_file


