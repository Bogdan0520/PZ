import tkinter as tk
from tkinter import ttk


def submit():
    print("Data submitted")


def cancel():
    print("Data entry cancelled")


root = tk.Tk()
root.title("Форма регистрации пользователя")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


ttk.Label(mainframe, text="Ваше имя:").grid(row=1, column=1, sticky=tk.W)
name_entry = ttk.Entry(mainframe, width=30)
name_entry.grid(row=1, column=2, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Пароль:").grid(row=2, column=1, sticky=tk.W)
password_entry = ttk.Entry(mainframe, width=30, show="*")
password_entry.grid(row=2, column=2, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Возраст:").grid(row=3, column=1, sticky=tk.W)
age_entry = ttk.Entry(mainframe, width=30)
age_entry.grid(row=3, column=2, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Пол:").grid(row=4, column=1, sticky=tk.W)
gender = tk.StringVar()
ttk.Radiobutton(mainframe, text="Мужской", variable=gender,
                value="Мужской").grid(row=4, column=2, sticky=tk.W)
ttk.Radiobutton(mainframe, text="Женский", variable=gender,
                value="Женский").grid(row=4, column=3, sticky=tk.W)

ttk.Label(mainframe, text="Ваши увлечения:").grid(row=5, column=1, sticky=tk.W)
music_var = tk.BooleanVar()
video_var = tk.BooleanVar()
drawing_var = tk.BooleanVar()
ttk.Checkbutton(mainframe, text="Музыка", variable=music_var).grid(
    row=5, column=2, sticky=tk.W)
ttk.Checkbutton(mainframe, text="Видео", variable=video_var).grid(
    row=5, column=3, sticky=tk.W)
ttk.Checkbutton(mainframe, text="Рисование", variable=drawing_var).grid(
    row=5, column=4, sticky=tk.W)

ttk.Label(mainframe, text="Ваша страна:").grid(row=6, column=1, sticky=tk.W)
country_combobox = ttk.Combobox(
    mainframe, values=["Россия", "США", "Канада", "Другие"], state='readonly')
country_combobox.grid(row=6, column=2, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Ваш город:").grid(row=7, column=1, sticky=tk.W)
city_entry = ttk.Entry(mainframe, width=30)
city_entry.grid(row=7, column=2, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Кратко о себе:").grid(row=8, column=1, sticky=tk.W)
about_text = tk.Text(mainframe, width=40, height=4)
about_text.grid(row=8, column=2, columnspan=2, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Решите пример, запишите результат в поле ниже:").grid(
    row=9, column=1, sticky=tk.W)
example_entry = ttk.Entry(mainframe, width=30)
example_entry.grid(row=9, column=2, sticky=(tk.W, tk.E))

ttk.Button(mainframe, text="Отменить ввод", command=cancel).grid(
    row=10, column=1, sticky=tk.W)
ttk.Button(mainframe, text="Данные подтверждаю",
           command=submit).grid(row=10, column=2, sticky=tk.W)

root.mainloop()
