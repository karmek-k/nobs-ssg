"""Utilities for site creation"""
import abc


class AbstractSiteFactory(abc.ABC):
    """
    An abstract site factory.
    Site factories should inherit from this class.
    """

    @abc.abstractmethod
    def load_files(self, loader):
        """Load neccesary files - md sources, toml config etc."""
        pass

    @abc.abstractmethod
    def render(self, **kwargs):
        """Render the site's templates with provided data."""
        pass

    @abc.abstractmethod
    def build(self):
        """Create a browsable site structure that is ready for outputting."""
        pass
