from html.parser import HTMLParser
from urllib.request import urlopen
from os.path import expanduser, join, exists

class MyHTMLParser(HTMLParser):
    def __init__(self, dir=None, overwrite=False):
        super().__init__()
        self.dir = dir if dir else expanduser('~')
        self.overwrite = overwrite

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            alt = None
            src = None
            ext = None
            for attr in attrs:
                if attr[0] == 'alt':
                    alt = attr[1].strip()
                if attr[0] == 'src':
                    src = attr[1].strip()
                    ext = src.split('.')[-1]
            if alt and src:
                filename = alt+"."+ext
                path = join(self.dir, filename)
                if not exists(path) or self.overwrite:
                    try:
                        with urlopen(src) as res:
                            print(filename+"をダウンロード中... ", end='')
                            with open(path, 'wb') as f:
                                f.write(res.read())
                            print("完了。")
                    except Exception as e:
                        print("失敗。")
                        print(e.args)
