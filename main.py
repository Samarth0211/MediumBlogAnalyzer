# app/main.py
import streamlit as st
from utils.helpers import extract_blog_title, fetch_and_store_paragraphs, remove_stopwords


def main():
    st.title("Medium Blog Title Extractor")

    # Accept input from the user
    blog_link = st.text_input("Enter Medium Blog Link:")

    if blog_link:
        # Extract and display the blog title
        blog_title = extract_blog_title(blog_link)
        st.header(f"**Blog Title:** ")
        st.header(blog_title)

        # Fetch and store paragraphs
        output_folder = 'files'
        cleaned_output_file = fetch_and_store_paragraphs(blog_link, output_folder)
        st.success(f"Paragraphs have been stored in {cleaned_output_file}")

        # Remove stopwords
        stopwords_removed_file = remove_stopwords(cleaned_output_file, cleaned_output_file.replace('_cleaned_', '_stopwords_removed_'))
        st.success(f"Stopwords have been removed. Result stored in {stopwords_removed_file}")


if __name__ == "__main__":
    main()
