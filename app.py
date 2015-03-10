from flask import Flask, render_template, send_file, request, url_for
from model import res, add_pir, add_img, img, listImg, ready,new_pir,pirosiki_orig
from flask.ext.scss import Scss

app = Flask(__name__)
app.debug = True
Scss(app, static_dir='static/css', asset_dir='assets')

#создание приложения
@app.route("/favicon")
def fav():
  return send_file('img/favicon.ico', mimetype='image/ico')

@app.route("/")
def index():
  return render_template("index.html", pirozki = res(), word=None, pir_or=pirosiki_orig())

@app.route("/result/<word>")
def result(word):
  allpirozoki= res()
  pir = listImg()
  cur_pir = img(word,allpirozoki)
  pirozokimg ="img/"+pir[cur_pir].strip()+".png"
  return render_template("pirosiki's.html", pirozok=word, pirozki=res(),pirozokimg=pirozokimg)

@app.route("/all")
def all():
  return render_template("all.html",pirozki=res(),pir = listImg())

@app.route("/add")
def more():
  word = request.values['pirosiki']
  add_pir(word)
  add_img(word)
  return index()

@app.route("/done/<number>")
def delete(number):
  a=int(number)
  ready(a)
  return index()

#роутинг

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
#запуск приложения

