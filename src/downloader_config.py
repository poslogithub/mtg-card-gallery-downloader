from config import ConfigFile
from os.path import expanduser

class ConfigKey():
    URL = "url"
    EXT = "ext"
    DIR = "dir"
    OVERWRITE = "overwrite"

class ConfigValue():
    pass

class DownloaderConfigFile(ConfigFile):
    def __init__(self, path=None):
        super().__init__(path)
        self.config = {
            ConfigKey.URL: "https://magic.wizards.com/ja/articles/archive/card-image-gallery/kamigawa-neon-dynasty",
            ConfigKey.EXT: "jpg",
            ConfigKey.DIR: expanduser('~'),
            ConfigKey.OVERWRITE: False
        }
