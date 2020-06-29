from abc import ABC, abstractmethod

from jinja2 import Environment, PackageLoader, select_autoescape


class Page(ABC):
    """Abstract class for objects having their pages"""
    template = None
    css_files = []
    data = {}

    def __init__(self, **kwargs):
        """
        Initializes the jinja2 environment
        and sets site data.
        """
        self.env = Environment(
            loader=PackageLoader('nobs', 'templates'),
            autoescape=select_autoescape(['html'])
        )
        for k, v in kwargs.items():
            self.data[k] = v
    
    def __str__(self):
        """Returns template name"""
        return f'<Page instance with template: {self.template}>'
    
    def render(self):
        """Returns rendered page"""
        return self.env.get_template(self.template).render(
            data=self.data
        )


class ArticlePage(Page):
    """Represents a single article in a blog"""
    template = 'articles/article.html'
    css_files = ['articles/article.css']
