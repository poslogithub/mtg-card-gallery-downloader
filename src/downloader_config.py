from config import ConfigFile
from os.path import expanduser

class ConfigKey():
    URL = "url"
    DIR = "dir"
    OVERWRITE = "overwrite"

class ConfigValue():
    pass

class DownloaderConfigFile(ConfigFile):
    def __init__(self, path=None):
        super().__init__(path)
        self.config = {
            ConfigKey.URL: "https://magic.wizards.com/ja/articles/archive/card-image-gallery/streets-of-new-capenna",
            ConfigKey.DIR: expanduser('~'),
            ConfigKey.OVERWRITE: False
        }
