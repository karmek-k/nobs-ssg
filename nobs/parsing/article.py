from datetime import date

from markdown import markdown as parse_markdown


class Article:
    """The class representing a single article"""

    def __init__(self, markdown, title='Article'):
        """Creates an Article object"""
        self.content = parse_markdown(markdown)
        self.title = title

        # placeholder
        self.date = date.today()
    
    def __str__(self):
        """Returns this article's content"""
        return self.content
