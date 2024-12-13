from flask import Flask, request, redirect

app = Flask(__name__)

# Список заблокированных сайтов
blocked_sites = ["twitch.tv", "www.twitch.tv"]

@app.route('/')
def index():
    return "Этот прокси-сервер блокирует доступ к определённым сайтам."

@app.route('/<path:url>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(url):
    # Проверка на наличие заблокированного сайта в URL
    for site in blocked_sites:
        if site in url:
            return "Доступ к этому сайту заблокирован.", 403

    # Если сайт не заблокирован, перенаправляем запрос
    return redirect(f"http://{url}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
