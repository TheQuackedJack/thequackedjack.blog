from pathlib import Path

# Define the project root as two levels up from the current file
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Define paths relative to the project root
BUILD_PATH = PROJECT_ROOT / "build"
TEMPLATES_PATH = PROJECT_ROOT / "templates"
POST_BUILD_PATH = BUILD_PATH / "posts"

# Template names
POST_TEMPLATE_NAME = "post.html.jinja"