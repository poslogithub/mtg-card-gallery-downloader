from html.parser import HTMLParser
from urllib.request import urlopen
from os.path import expanduser, join, exists

class MyHTMLParser(HTMLParser):
    def __init__(self, dir=None, ext=None, overwrite=False):
        super().__init__()
        self.dir = dir if dir else expanduser('~')
        self.ext = ext if ext else 'jpg'
        self.overwrite = overwrite

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            alt = None
            src = None
            for attr in attrs:
                if attr[0] == 'alt':
                    alt = attr[1].strip()
                if attr[0] == 'src':
                    src = attr[1].strip()
            if alt and src:
                with urlopen(src) as res:
                    filename = alt+"."+self.ext
                    path = join(self.dir, filename)
                    if not exists(path) or self.overwrite:
                        print(filename+"をダウンロード中... ", end='')
                        try:
                            with open(path, 'wb') as f:
                                f.write(res.read())
                            print("完了。")
                        except:
                            print("失敗。")
