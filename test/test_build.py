import pytest
from build import build_post

@pytest.mark.parametrize("page_name", ["", None])
def test_build_post_page_name_exceptions(page_name):
    """
    Tests for exception handling on invalid page_names.
    """
    post_context = {}
    with pytest.raises(ValueError):
        build_post(post_context=post_context, page_name=page_name)


# TODO: Add in the case for invalid pydantic models on the post building

def test_build_post_warning_logs():
    pass


def test_build_post_output():
    pass

