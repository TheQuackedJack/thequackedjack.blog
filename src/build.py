from jinja2 import Environment, FileSystemLoader
import logging

# TODO: Check if BUILD_PATH is needed later
from config import (BUILD_PATH,
                    TEMPLATES_PATH, 
                    POST_BUILD_PATH, 
                    POST_TEMPLATE_NAME) 

# Set up the Jinja2 environment to load templates from the templates directory
env = Environment(loader=FileSystemLoader(str(TEMPLATES_PATH)))

# Load the template file
template = env.get_template(POST_TEMPLATE_NAME)

# TODO: Add in Pydantic model for validating the post input data.

# TODO: Add unit tests later for this
# TODO: change the page_name to be a part of the post context
def build_post(post_context: dict, page_name: str):
    """
    Builds a post HTML file from the given context and saves it to the build directory.

    Args:
        post_context (dict): Context data for rendering the template.
        page_name (str): Name of the output HTML file.

    Raises:
        ValueError: If the page name is not valid.
    """
    if not page_name:
        logging.error("The page name is not valid.")
        raise ValueError("The page name is not valid.")
    
    if not page_name.endswith(".html"):
        logging.warning("A .html extension was forgotten; appending '.html' to the page name.")
        page_name += ".html"
        
    # TODO: add in a bit of code for ensuring the slug of the file name will follow good practices for SEO
    # probably want to use a regex
    # can use awesome-slugify for this task


    # Log the rendering process
    logging.info("Rendering HTML for page: %s", page_name)

    # Render the template with the context data
    rendered_html = template.render(post_context)

    file_path = POST_BUILD_PATH / page_name

    # Ensure the output directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)
        logging.info("Saved rendered HTML to %s", file_path)


def retrieve_md_posts():
    """
    Retrieves a list of markdown files that are ready for deployment (yaml bool key of "deploy_post")
    """
    pass

def build_post_index():
    """
    This will be a json index of the posts that will build the index.html.
    Might also help the main site as well.
    This will be called 'index.json'
    This will be build by parsing the yaml of each md_post with "parse_post_metadata" applied on retrieve_md_posts.
    """
    pass

def build_post_feed():
    """
    This will be a 'feed.xml' to share the articles of the site.
    """
    pass

def build_site_index():
    """
    Make a function that builds the index.html based around index.json.
    """
    pass

def build_site_posts():
    """
    Will build the site by calling 'parse_post_content'
    """

def build_site():
    """
    Will bring all the pieces together.
    """

# TODO: think about whether it is useful to zip the site up or not or have a way to transfer it
# TODO: think about how the version will be attached to the build

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

    # Define the context for rendering the template
    context = {
        "seo_description": "An in-depth exploration of Python’s libraries for data analysis.",
        "keywords": "Python, Data Analysis, Pandas, NumPy",
        "author": "Jerry Bard",
        "title": "Exploring Python Libraries for Data Analysis",
        "og_title": "Exploring Python Libraries for Data Analysis",
        "og_description": "An in-depth exploration of Python’s libraries for data analysis.",
        "og_image": "https://example.com/path/to/og_image.jpg",
        "og_url": "https://thequackedjack.dev/blog/python-data-analysis",
        "post_content": "<p>This is the content of the blog post.</p>"
    }

    page_name = "test-post.html"
    build_post(context, page_name)

if __name__ == "__main__":
    main()
