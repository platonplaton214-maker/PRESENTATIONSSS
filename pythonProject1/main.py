import tkinter as tk
from tkinter import filedialog, messagebox


def process_file():
    # 1. Получаем ключ
    key_str = entry_key.get()
    if not key_str:
        messagebox.showerror("Ошибка", "Введите ключ!")
        return

    try:
        # Превращаем строку ключа в число для операции XOR
        # Если ключ длинный, берем сумму кодов символов или просто первый байт
        key = sum(ord(char) for char in key_str) % 256
    except Exception:
        messagebox.showerror("Ошибка", "Некорректный ключ!")
        return

    # 2. Выбираем файл (любое изображение)
    file_path = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=[("Изображения", "*.jpg *.jpeg *.png *.bmp"), ("Все файлы", "*.*")]
    )

    if not file_path:
        return

    try:
        # 3. Читаем файл как набор байтов
        with open(file_path, 'rb') as f:
            data = bytearray(f.read())

        # 4. Шифруем/Дешифруем (XOR)
        for i in range(len(data)):
            data[i] ^= key

        # 5. Сохраняем результат
        save_path = filedialog.asksaveasfilename(
            title="Сохранить результат как...",
            defaultextension=file_path[file_path.rfind('.'):],  # Берем расширение оригинала
            filetypes=[("Все файлы", "*.*")]
        )

        if save_path:
            with open(save_path, 'wb') as f:
                f.write(data)
            messagebox.showinfo("Готово", "Выполнено шифрование/дешифрование!")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось обработать файл: {e}")


# --- Интерфейс (стандартный tkinter) ---
root = tk.Tk()
root.title("XOR Cipher")
root.geometry("300x160")
root.resizable(False, False)

tk.Label(root, text="Введите код (ключ):").pack(pady=10)

entry_key = tk.Entry(root, show="*")
entry_key.pack(pady=5)

# Кнопка "Готово" по вашему запросу
btn_done = tk.Button(root, text="Готово", width=15, command=process_file)
btn_done.pack(pady=20)

root.mainloop()
