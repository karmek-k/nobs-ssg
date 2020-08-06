"""File utilities"""
import os
from pathlib import Path


class FileLoader:
    """Class responsible for loading files."""
    def __init__(self, path=os.getcwd()):
        """Sets the path where FileLoader looks for files."""
        # Check if the path argument is a Path object or just a string 
        if isinstance(path, Path):  
            self.path = path
        else:
            self.path = Path(path)
    
    def map_template_files(self,
            path=self.path, config_folder='config', factory_file='factory.py',
            config_file='config.toml', src_extensions={'html', 'css', 'js'}):
        """Returns names of template files and directories in the FileLoader's path."""
        config_path = path / config_folder

        all_files = path.glob('**/*')
        # only files including one of src_extensions
        src = filter(
            lambda fpath: fpath.suffix[1:] in src_extensions,
            all_files
        )

        factory = config_path / factory_file
        config = config_path / config_file

        mapped_files = {
            'factory': factory if factory.exists() else None,
            'config': config if config.exists() else None,
            'src': src
        }
        
        return mapped_files
