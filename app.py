from flask import Flask, render_template_string

app = Flask(__name__)

theory_sections = [
    {
        "title": "Фонетика",
        "content": "Фонетика ғылымының қалыптасу тарихы, тілдік дыбыстардың түрлері, дауысты және дауыссыз дыбыстар, буын, екпін, сингармонизм заңдылықтары және ғалымдардың көзқарастары."
    },
    {
        "title": "Дауысты дыбыстар",
        "content": "Қазақ тіліндегі дауысты дыбыстардың саны мен сапасы, артикуляциялық ерекшеліктері, жіктелуі (жуан/жіңішке, ашық/қысаң, еріндік/езулік)."
    },
    {
        "title": "Дауыссыз дыбыстар",
        "content": "Консонантизмнің жіктелуі: үнді, ұяң, қатаң дыбыстар, шұғыл, ызың, діріл дыбыстар, айтылу орны бойынша топтастыру."
    },
    {
        "title": "Буын",
        "content": "Буынның түрлері: ашық, тұйық, бітеу. Буынның құрылымы мен қызметі. Жасалу жолдары."
    },
    {
        "title": "Екпін",
        "content": "Сөз, фразалық және логикалық екпін түрлері. Сингармонизммен байланысы, түрлі ғалымдар теориялары."
    }
]

practice_examples = [
    {
        "word": "Сиқырлы",
        "analysis": "Сый-қыр-лы. 7 әріп, 8 дыбыс. Тіл үндестігі: бірыңғай жуан. Екпін соңғы буынға түседі."
    },
    {
        "word": "Монтию",
        "analysis": "Мон-ты-йұу. 6 әріп, 8 дыбыс. Ерін үндестігі: бар. Тіл үндестігі: бірыңғай жуан."
    },
    {
        "word": "Қиямет",
        "analysis": "Қы-йа-мет. Аралас тіл үндестігі. Екпін: соңғы буын."
    },
    {
        "word": "Көркем",
        "analysis": "Көр-кем. Бірыңғай жіңішке."
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Қазақ тіл білімінің салалары</title>
    <style>
        body { font-family: sans-serif; padding: 20px; }
        .tab { margin: 10px 0; }
        .section, .example { margin-bottom: 20px; padding: 15px; border: 1px solid #ccc; border-radius: 10px; }
        h2 { margin-bottom: 5px; }
    </style>
</head>
<body>
    <h1>Қазақ тіл білімінің салалары</h1>
    <div class="tab">
        <h2>Теория</h2>
        {% for section in theory %}
        <div class="section">
            <h3>{{ section.title }}</h3>
            <p>{{ section.content }}</p>
        </div>
        {% endfor %}
    </div>
    <div class="tab">
        <h2>Практика</h2>
        {% for example in practice %}
        <div class="example">
            <h3>{{ example.word }}</h3>
            <p>{{ example.analysis }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, theory=theory_sections, practice=practice_examples)

if __name__ == "__main__":
    app.run(debug=True)
