import streamlit as st
from utils.helpers import extract_username_and_title

def main():
    st.title("Medium Blog Viewer")

    # Accept Medium blog link from the user
    blog_link = st.text_input("Enter Medium Blog Link (e.g., @username/blog_title):")

    # Extract username and blog title from the input link
    username, blog_title = extract_username_and_title(blog_link)

    # Display the extracted information
    if username and blog_title:
        st.write(f"Username: {username}")
        st.write(f"Blog Title: {blog_title}")
    else:
        st.warning("Invalid Medium blog link. Please enter a valid link.")

if __name__ == "__main__":
    main()
