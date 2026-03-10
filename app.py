from flask import Flask, render_template, request, redirect
from database import init_db, add_message, get_messages
import threading
from send_scheduler import start_scheduler

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        phone = request.form["phone"]
        date = request.form["date"]
        time = request.form.get("time", "09:00")
        message = request.form["message"]
        add_message(phone, date, message, time)
    messages = get_messages()
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    # Roda o scheduler em thread separada
    threading.Thread(target=start_scheduler, daemon=True).start()
    app.run(debug=True)