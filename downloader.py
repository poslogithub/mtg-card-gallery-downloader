from os.path import basename, expanduser
from tkinter import BooleanVar, Button, Frame, StringVar, Tk, E, W, filedialog
from tkinter.filedialog import askdirectory
from tkinter.ttk import Checkbutton, Entry, Label
from urllib.request import urlopen
import webbrowser

from html_parser import MyHTMLParser
from downloader_config import DownloaderConfigFile, ConfigKey

class Downloader(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # 定数
        self.CONFIG_PATH = "config.json"

        # 変数
        self.config_file = DownloaderConfigFile(self.CONFIG_PATH)
        self.config = self.config_file.load()
        self.sv_url = StringVar(value=self.config.get(ConfigKey.URL))
        self.sv_ext = StringVar(value=self.config.get(ConfigKey.EXT))
        self.sv_dir = StringVar(value=self.config.get(ConfigKey.DIR))
        self.bv_overwrite = BooleanVar(value=self.config.get(ConfigKey.OVERWRITE))

        # GUI
        self.master.title("M:tG Card Image Downloader")
        self.master.geometry("800x180")
        self.master_frame = Frame(self.master)
        self.master_frame.pack()
        self.url_label = Label(self.master_frame, text="Card Image Gallery URL: ", anchor="w")
        self.url_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.url_entry = Entry(self.master_frame, textvariable=self.sv_url, width=90)
        self.url_entry.grid(row=0, column=1, sticky=W + E, padx=5, pady=5)
        self.url_button = Button(self.master_frame, text="　開く　", command=self.push_url_button)
        self.url_button.grid(row=0, column=2, sticky=W + E, padx=5, pady=5)
        self.ext_label = Label(self.master_frame, text="画像ファイルの拡張子: ", anchor="w")
        self.ext_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.ext_entry = Entry(self.master_frame, textvariable=self.sv_ext, width=8)
        self.ext_entry.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        self.dir_label = Label(self.master_frame, text="保存先フォルダ: ", anchor="w")
        self.dir_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.dir_entry = Entry(self.master_frame, textvariable=self.sv_dir, width=44)
        self.dir_entry.grid(row=2, column=1, sticky=W + E, padx=5, pady=5)
        self.dir_button = Button(self.master_frame, text="　参照　", command=self.push_dir_button)
        self.dir_button.grid(row=2, column=2, sticky=W + E, padx=5, pady=5)
        self.overwrite_checkbutton = Checkbutton(self.master_frame, text="既存ファイルを上書きする", variable=self.bv_overwrite)
        self.overwrite_checkbutton.grid(row=3, column=1, sticky=W, padx=5, pady=5)
        self.download_button = Button(self.master_frame, text="　実行　", command=self.push_download_button)
        self.download_button.grid(row=4, column=2, sticky=W + E, padx=5, pady=5)

    def push_url_button(self):
        webbrowser.open(self.sv_url.get())

    def push_dir_button(self):
        if self.sv_dir.get():
            initialdir = self.sv_dir.get()
        elif self.config.get(ConfigKey.DIR):
            initialdir = self.config.get(ConfigKey.DIR)
        elif expanduser('~'):
            initialdir = expanduser('~')
        else:
            initialdir = None
        path = askdirectory(initialdir=initialdir)
        if path:
            self.sv_dir.set(path)

    def save_config(self):
        self.config[ConfigKey.URL] = self.sv_url.get()
        self.config[ConfigKey.EXT] = self.sv_ext.get()
        self.config[ConfigKey.DIR] = self.sv_dir.get()
        self.config[ConfigKey.OVERWRITE] = self.bv_overwrite.get()
        self.config_file.save(self.config)

    def push_download_button(self):
        self.save_config()

        html = None
        try:
            with urlopen(self.sv_url.get()) as res:
                html = str(res.read())
        except:
            html = None

        parser = MyHTMLParser(
            dir=self.config[ConfigKey.DIR], 
            ext=self.config[ConfigKey.EXT],
            overwrite=self.config[ConfigKey.OVERWRITE])
        parser.feed(html)

        print("全てのカード画像ファイルのダウンロードが完了。")

    def run(self):
        self.master.mainloop()
        self.save_config()


if __name__ == "__main__":
    #param = sys.argv
    root = Tk()
    downloader = Downloader(master=root)
    downloader.run()
