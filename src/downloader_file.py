from os.path import expanduser
from tkinter import BooleanVar, Button, Frame, StringVar, Tk, E, W, filedialog
from tkinter.filedialog import askdirectory
from tkinter.ttk import Checkbutton, Entry, Label

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
        self.sv_file = StringVar(value=self.config.get(ConfigKey.FILE))
        self.sv_file_dir = self.config.get(ConfigKey.FILE_DIR)
        self.sv_dir = StringVar(value=self.config.get(ConfigKey.DIR))
        self.bv_overwrite = BooleanVar(value=self.config.get(ConfigKey.OVERWRITE))

        # GUI
        self.master.title("M:tG Card Image Downloader")
        self.master.geometry("800x140")
        self.master_frame = Frame(self.master)
        self.master_frame.pack()
        self.file_label = Label(self.master_frame, text="Card Image Gallery File: ", anchor="w")
        self.file_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.file_entry = Entry(self.master_frame, textvariable=self.sv_file, width=90)
        self.file_entry.grid(row=0, column=1, sticky=W + E, padx=5, pady=5)
        self.file_button = Button(self.master_frame, text="　参照　", command=self.push_file_button)
        self.file_button.grid(row=0, column=2, sticky=W + E, padx=5, pady=5)
        self.dir_label = Label(self.master_frame, text="保存先フォルダ: ", anchor="w")
        self.dir_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.dir_entry = Entry(self.master_frame, textvariable=self.sv_dir, width=44)
        self.dir_entry.grid(row=1, column=1, sticky=W + E, padx=5, pady=5)
        self.dir_button = Button(self.master_frame, text="　参照　", command=self.push_dir_button)
        self.dir_button.grid(row=1, column=2, sticky=W + E, padx=5, pady=5)
        self.overwrite_checkbutton = Checkbutton(self.master_frame, text="既存ファイルを上書きする", variable=self.bv_overwrite)
        self.overwrite_checkbutton.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        self.download_button = Button(self.master_frame, text="　実行　", command=self.push_download_button)
        self.download_button.grid(row=3, column=2, sticky=W + E, padx=5, pady=5)

    def push_file_button(self):
        path = filedialog.askopenfilename(filetypes=[('ウェブページ、完全', '*.htm;*.html')], initialdir=self.sv_file_dir)
        if path:
            self.sv_file.set(path)

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
        self.config[ConfigKey.FILE] = self.sv_file.get()
        self.config[ConfigKey.DIR] = self.sv_dir.get()
        self.config[ConfigKey.OVERWRITE] = self.bv_overwrite.get()
        self.config_file.save(self.config)

    def push_download_button(self):
        self.save_config()

        html = None
        try:
            with open(self.sv_file.get(), "r", encoding="utf-8") as f:
                html = f.read()
        except:
            html = None

        parser = MyHTMLParser(
            dir=self.config[ConfigKey.DIR], 
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
