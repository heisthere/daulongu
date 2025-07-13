from flask import Flask, render_template, request

from articleDecomposer import ArticleDecomposer
from translator import Translator

app = Flask(__name__)


@app.route('/', methods=['GET'])
def default():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def decompose_article():
    if request.method == 'POST':
        # get input article
        article = request.form['article']
        #decompose article to sentences
        sentences = ArticleDecomposer.decompose(article)
        print(sentences)
        return render_template('list_sentences.html', sentences=sentences)

@app.route('/sentence', methods=['GET', 'POST'])
def translate_sentence():
    text_in_languages_dic = None
    row_headers = None
    column_headers= None
    if request.method == 'POST':
        sentence = request.form['sentence']
        text_in_languages_dic = Translator.translate(sentence)
        print(text_in_languages_dic)
        row_headers = list(text_in_languages_dic.keys())
        column_headers = text_in_languages_dic[row_headers[0]]
        print(row_headers)
        print(column_headers)
    return render_template('sentence_translated.html', result=text_in_languages_dic, column_headers=column_headers,
                           row_headers=row_headers)


if __name__ == '__main__':
    app.run(debug=True)