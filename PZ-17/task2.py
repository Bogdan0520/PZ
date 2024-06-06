# encode and decode programm using tkinter

import tkinter as tk
from tkinter import ttk


def encode_func(event):
    encode_text_field.delete('1.0', tk.END)
    text = original_text_field.get("1.0", tk.END).strip('\n')
    encode_text = text[1::2] + text[::2][::-1]
    encode_text_field.insert("1.0", encode_text)
    original_text_field.edit_modified(False)
    
def decode_func(event):
    after_decode_field.delete('1.0', tk.END)
    text = before_decode_field.get("1.0", tk.END).strip('\n')
    
    length = len(text)
    mid = (length) // 2 
    even_chars = text[:mid].strip()
    odd_chars = text[mid:][::-1]
    decrypted_str = []
    for i in range(mid):
        try:
            decrypted_str.append(odd_chars[i])
            decrypted_str.append(even_chars[i])
        except:
            print('some error')
    if len(text) % 2 !=0:
        decrypted_str.append(odd_chars[-1])
    decode_text = ''.join(decrypted_str)
    after_decode_field.insert("1.0", decode_text)
    before_decode_field.edit_modified(False)
    
    
def copy_to_clipboard():
    text = encode_text_field.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text)
    
    
def paste_from_clipboard():
    clipboard_text = root.clipboard_get()
    # Вставляем текст в текстовое поле
    before_decode_field.insert(tk.END, clipboard_text)



root = tk.Tk()
root.title("Шифратор - дешифратор")
root.geometry("1000x500")
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(mainframe, text='Введите строку, которую желаете зашифровать').grid(row=1, column=0)
ttk.Label(mainframe, text='Результат шифрования').grid(row=1, column=2, padx=10)

original_text_field = tk.Text(mainframe, width=40, height=5)
original_text_field.grid(row=2, column=0)
original_text_field.bind("<<Modified>>", encode_func)


encode_text_field = tk.Text(mainframe, width=40, height=5)
encode_text_field.grid(row=2, column=2, padx=30)


ttk.Label(mainframe, text='Введите строку, которую желаете дешифровать').grid(
    row=3, column=0)
ttk.Label(mainframe, text='Результат дешифрования').grid(
    row=3, column=2, padx=10)

before_decode_field = tk.Text(mainframe, width=40, height=5)
before_decode_field.grid(row=4, column=0)
before_decode_field.bind("<<Modified>>", decode_func)


after_decode_field = tk.Text(mainframe, width=40, height=5)
after_decode_field.grid(row=4, column=2, padx=30)

copy_button = tk.Button(mainframe, width=10, height=5,
                        text='Copy text', command=copy_to_clipboard)
copy_button.grid(row=2, column=3, padx=10)


paste_button = tk.Button(mainframe, width=10, height=5,
                         text='Paste text', command=paste_from_clipboard)
paste_button.grid(row=5, column=0)


root.mainloop()
