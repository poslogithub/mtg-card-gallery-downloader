from config import ConfigFile
from os import getenv
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
            ConfigKey.URL: "https://magic.wizards.com/ja/news/card-image-gallery/phyrexia-all-will-be-one",
            ConfigKey.FILE: "",
            ConfigKey.FILE_DIR: getenv('HOME')+"\Downloads",
            ConfigKey.DIR: expanduser('~'),
            ConfigKey.OVERWRITE: False
        }
