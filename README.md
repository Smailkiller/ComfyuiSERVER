# 📦 ComfyUI Remote Launcher

Набор файлов для управления **несколькими сессиями ComfyUI** через веб-интерфейс. Поддерживает запуск, остановку и быстрый переход по портам — каждая сессия запускается в отдельном окне `CMD`.

---

## 📁 Структура проекта

```
ComfyUI_windows_portable/
├── python_embeded/
│   ├── remote_launcher.py       ← основной Flask-сервер
│   ├── templates/
│   │   └── index.html           ← HTML-интерфейс управления
│   ├── python.exe               ← встроенный Python (не менять!)
├── ComfyUI/
│   └── main.py                  ← точка входа ComfyUI
├── launcher.bat                 ← опциональный .bat-файл для старта
```

---

## 🚀 Как установить и использовать

1. **Скачайте репозиторий или сохраните 3 файла:**
   - `remote_launcher.py`
   - `index.html` → положить в `python_embeded/templates/`
   - `START_SERVER.bat` (опционально)

2. **Проверьте структуру путей:**
   Убедитесь, что вы используете **оригинальную структуру ComfyUI Portable**, без переименований:
   - `python.exe` должен быть по пути:  
     `C:\tmp\ComfyUI_windows_portable\python_embeded\python.exe`
   - Comfy запускается из:  
     `C:\tmp\ComfyUI_windows_portable\ComfyUI\main.py`

Или замените пути в начале файла `remote_launcher.py`

3. **Запуск:**

   👉 Через `bat`:
   ```bat
   START_SERVER.bat
   ```

   Или вручную:
   ```bash
   cd C:\tmp\ComfyUI_windows_portable\python_embeded
   python.exe remote_launcher.py
   ```

4. **Откройте браузер:**
   Перейдите по адресу:  
   [http://127.0.0.1:7860](http://127.0.0.1:7860)

---

## 🖥 Как работает

- На главной странице вы указываете порт (например `8188`) и нажимаете **«Запустить»**
- Открывается новое окно `CMD`, запускается новая сессия ComfyUI на этом порту
- В списке активных сессий появляется ссылка для перехода:  
  👉 [http://127.0.0.1:8188](http://127.0.0.1:8188) (или IP компьютера где открыта сборка)
- Кнопка «Остановить» завершает `CMD`-окно с указанным портом

---

## ⚠️ Важно

- **Python, Flask и всё необходимое уже встроено** в сборку `ComfyUI_windows_portable`.
- **Принудительное завершение открытых сборок на портах пока не работает, но есть в интерфейсе**
