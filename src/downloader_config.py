from config import ConfigFile
from os.path import expanduser

class ConfigKey():
    URL = "url"
    FILE = "file"
    FILE_DIR = "file_dir"
    DIR = "dir"
    OVERWRITE = "overwrite"

class ConfigValue():
    pass

class DownloaderConfigFile(ConfigFile):
    def __init__(self, path=None):
        super().__init__(path)
        self.config = {
            ConfigKey.URL: "https://magic.wizards.com/ja/products/the-lost-caverns-of-ixalan/card-image-gallery",
            ConfigKey.FILE: "",
            ConfigKey.FILE_DIR: expanduser('~')+"\Downloads",
            ConfigKey.DIR: expanduser('~'),
            ConfigKey.OVERWRITE: False
        }
