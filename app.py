from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    title = "Halaman Utama"
    message = "Selamat datang di aplikasi web Flask!"
    features = [
        {
            "icon": "⚡",
            "title": "Cepat & Ringan",
            "desc": "Menggunakan Flask framework yang minimalis dan mudah dikembangkan."
        },
        {
            "icon": "🧩",
            "title": "Template Inheritance",
            "desc": "Struktur modular menggunakan Jinja2 dengan base.html dan index.html."
        },
        {
            "icon": "📱",
            "title": "Desain Responsif",
            "desc": "Tampilan modern, bersih, dan nyaman dilihat di berbagai perangkat."
        }
    ]
    return render_template("index.html", title=title, message=message, features=features)

if __name__ == "__main__":
    app.run(debug=True)

