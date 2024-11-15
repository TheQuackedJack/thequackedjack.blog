# will contain code that parses the markdown files in "posts" folder to make them actual web pages
# TODO: Change the directories of the markdown files to be better named to not conflict with website directory. 
# or at least think about it


# TODO: Add the pydantic model to the config instead as we should validate from there
# TODO: Should find a good markdown linter
def validate_post(file_path: str):
    """
    validate the post markdown file to ensure it has all the contents and appropriate syntax
    should validate the metadata and the contents of the markdown
    """
    pass


def parse_post_metadata(file_path: str):
    """
    Will parse the md file for relevant metadata from the YAML front matter.
    Expectation is that this will will return to a dict that is a valid post pydantic model
    """
    pass


def parse_post_content(file_path: str):
    """
    Parse the post content in way that converts it to html. Try to think about what else will be needed here.
    This is what will be used to convert the markdown that is injected into the jinja template.
    """
    pass


