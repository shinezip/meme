from flask import Flask, render_template, request
import random

app = Flask(__name__)

excuses = {
    "добрий": [
        {"text": "Я намагався, але захворів на легку депресію.", "meme": "https://i.imgflip.com/4/1bij.jpg"},
        {"text": "Випадково видалив проєкт, але не хотів вас турбувати.", "meme": "https://i.imgflip.com/4/1bgw.jpg"},
        {"text": "Хотів зробити краще.", "meme": "https://i.imgflip.com/4/1ihzfe.jpg"}
    ],
    "злий": [
        {"text": "апав супрiма в напах.", "meme": "https://imgs.search.brave.com/OzsqdSlMgR7S7KjYF6tcoM2lpfx91gusjcjzIMLs9io/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9wbGF0/Zm9ybS50aGV2ZXJn/ZS5jb20vd3AtY29u/dGVudC91cGxvYWRz/L3NpdGVzLzIvY2hv/cnVzL3VwbG9hZHMv/Y2hvcnVzX2Fzc2V0/L2ZpbGUvMzYxNjg2/Ni9jdXRlLXN1Y2Nl/c3Mta2lkLTE5MjB4/MTA4MC4wLmpwZz9x/dWFsaXR5PTkwJnN0/cmlwPWFsbCZjcm9w/PTcuODEyNSwwLDg0/LjM3NSwxMDAmdz0y/NDAw"},
        {"text": "чат гпт сказав що я гальмо.", "meme": "https://imgs.search.brave.com/7eQCstkGWSEazIdMJqHOEt1R4ewm4N3Iqg5bE0NjP1o/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmlt/Z2ZsaXAuY29tLzQv/M3k2cW1mLmpwZw"},
        {"text": "Я здав, але у вicнi.", "meme": "https://imgs.search.brave.com/w3WbDpR8cCi88M_f7tEv0YKHzQGGYEjrahN0ZM7f7rA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzQ4L2Nj/LzY2LzQ4Y2M2NjQ3/MjgyMTVkZWNmMzgw/MTUwZjg2ZGM4OWZl/LmpwZw"}
    ],
    "пофек": [
        {"text": "Мені було всеодно.", "meme": "https://imgs.search.brave.com/CwcefeYJ6F6sjnJJATcLee-SMYyla_86wbQ0bWoqzJA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvOTkx/NDAzMDYyL3Bob3Rv/L2dydW1weS1jYXQu/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PTkwUW51UTh3alFH/cmFUUlFtRlNZalkt/dldCcndnTm9hVEFG/bDhoeTRBUWM9"},
        {"text": "Навіть deepseek не зрозумів що робити.", "meme": "https://imgs.search.brave.com/q9cPjtDGMjZUAGx9Vs3m41uBcQmMNeqJkrmB_zj-0h4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLnNz/dGF0aWMubmV0L3BC/NDNrLmpwZw"},
        {"text": "Якщо чесно, я думав, що ця лаба вже сдана.", "meme": "https://imgs.search.brave.com/NCMDMsSWUpS0VwkY5CoxJjU7ks8g0RxjkGCXh9_Llyc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jb250/ZW50LmltYWdlcmVz/aXplci5jb20vaW1h/Z2VzL21lbWVzL1dh/aXRpbmctc2tlbGV0/b24tbWVtZS04Lmpw/Zw"}
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    meme_url = None
    if request.method == "POST":
        teacher_type = request.form.get("teacher")
        selected = random.choice(excuses.get(teacher_type, []))
        result = selected["text"]
        meme_url = selected["meme"]
    return render_template("index.html", result=result, meme_url=meme_url)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10000)

