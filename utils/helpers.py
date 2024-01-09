def extract_username_and_title(blog_link):
    # Check if the input is a valid Medium blog link
    if "https://medium.com/" not in blog_link:
        return None, None

    # Extract username and blog title
    try:
        _, username, blog_title = blog_link.split("/", 2)
        return username, blog_title
    except ValueError:
        return None, None
