from abc import ABC, abstractmethod


class Page(ABC):
    """Abstract class for objects having their pages"""

    @abstractmethod
    def __init__(self, content, parent=None):
        self.content = content
        self.parent = parent

    def dump(self, path):
        with open(path) as f:
            f.write(self.content)


class ArticlePage(Page):
    pass