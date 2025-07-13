from flask import Flask, render_template, request
from translator import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text_in_languages_dic = None
    row_headers = None
    column_headers= None
    if request.method == 'POST':
        input_text = request.form['user_input']
        text_in_languages_dic = Translator.translate(input_text)
        print(text_in_languages_dic)
        row_headers = list(text_in_languages_dic.keys())
        column_headers = text_in_languages_dic[row_headers[0]]
        print(row_headers)
        print(column_headers)

    return render_template('index.html', result=text_in_languages_dic,  column_headers=column_headers, row_headers= row_headers)

if __name__ == '__main__':
    app.run(debug=True)