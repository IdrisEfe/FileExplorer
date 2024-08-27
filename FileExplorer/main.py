import tkinter as tk
from tkinter import filedialog

class FileExplorer:

    def __init__(self):

        root = tk.Tk()
        root.title("File Explorer")
        root.config(bg = '#fffdd0')
        root.geometry('800x600')

        label_introduction = tk.Label(root, text = 'File Explorer', bg = 'white', fg = 'blue', anchor='w', font = 'bold 20')
        label_introduction.place(relx = 0, rely = 0, relheight=0.1, relwidth=1)

        entry_for_search = tk.Button(root, text = 'Browse Files', command = self.browseFiles)
        entry_for_search.place(relx = 0.45, rely=0.5, relheight=0.05, relwidth=0.1)

        root.mainloop()

    def browseFiles(self):

        fileName = filedialog.askopenfile(initialdir='/',
                                          title = 'Select a File',
                                          filetypes= (('Text files', '*.txt*'), (
                                                     'all files', '*.*')))

def main():
    fileExplorer = FileExplorer()

if __name__ == '__main__':
    main()