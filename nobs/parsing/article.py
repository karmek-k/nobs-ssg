from datetime import date

from markdown import markdown


class Article:
    """The class representing a single article"""

    def __init__(self, html):
        """Creates an Article object"""
        self.content = markdown(html)

        # placeholder
        self.date = date.today()
    
    def __str__(self):
        """Returns this article's content"""
        return self.content
