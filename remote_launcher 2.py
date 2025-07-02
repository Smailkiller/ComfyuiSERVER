import os
import subprocess
from flask import Flask, render_template, request, redirect
 
app = Flask(__name__)
 
# Пути
PYTHON_PATH = r"C:\tmp\ComfyUI_windows_portable\python_embeded\python.exe"
COMFY_PATH = r"C:\tmp\ComfyUI_windows_portable\ComfyUI\main.py"
 
# Активные процессы по портам
processes = {}
 
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", sessions=processes)
 
@app.route("/start", methods=["POST"])
def start_instance():
    port_raw = request.form.get("port")
    if not port_raw:
        return "⛔ Порт не указан", 400
 
    try:
        port = int(port_raw)
    except ValueError:
        return "⛔ Неверный формат порта", 400
 
    if port in processes:
        return f"⚠️ Сессия на порту {port} уже запущена", 400
 
    cmd = f'start "ComfyUI - {port}" cmd /k "{PYTHON_PATH} {COMFY_PATH} --listen --port {port}"'
    subprocess.Popen(cmd, shell=True)
    processes[port] = True
    return redirect("/")
 
@app.route("/stop", methods=["POST"])
def stop_instance():
    port_raw = request.form.get("port")
    if not port_raw:
        return "⛔ Порт не указан", 400
 
    try:
        port = int(port_raw)
    except ValueError:
        return "⛔ Неверный формат порта", 400
 
    title = f"ComfyUI - {port}"
    os.system(f'taskkill /F /FI "WINDOWTITLE eq {title}"')
    processes.pop(port, None)
    return redirect("/")
 
if __name__ == "__main__":
    app.run(debug=True, port=7860, host="0.0.0.0")