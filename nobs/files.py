"""File utilities"""
import os
import abc
from pathlib import Path


class AbstractFileLoader(abc.ABC):
    """Abstract class responsible for loading files."""
    def __init__(self, path):
        self.path = path if isinstance(path, Path) else Path(path)
    
    @abc.abstractmethod
    def map_files(self):
        pass


class TemplateFileLoader(AbstractFileLoader):
    """Class responsible for loading template files."""
    def map_files(self,
            config_folder='config', factory_file='factory.py',
            config_file='config.toml', extensions={'html', 'css', 'js'}):
        """Returns paths of template files and directories in the FileLoader's path."""
        config_path = self.path / config_folder

        all_files = self.path.glob('**/*')
        # only files including one of extensions
        template_files = filter(
            lambda fpath: fpath.suffix[1:] in extensions,
            all_files
        )

        factory = config_path / factory_file
        config = config_path / config_file

        mapped_files = {
            'factory': factory if factory.exists() else None,
            'config': config if config.exists() else None,
            'template_files': template_files
        }
        
        return mapped_files


class SourceFileLoader(AbstractFileLoader):
    """Class responsible for loading source files."""
    def map_files(self, extensions={'md'}):
        """Returns paths of source files."""
        all_files = self.path.glob('**/*')
        src = filter(
            lambda fpath: fpath.suffix[1:] in extensions,
            all_files
        )

        mapped_files = {
            'src': src
        }

        return mapped_files
