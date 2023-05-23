import os, sys, flask, io, qrcode
from flask import Flask, request, render_template, redirect, url_for
import werkzeug
# from jinja2 import Markup, Environment, FileSystemLoader

# from livereload import Server
from datetime import datetime

from qrcode import *

app = Flask(__name__, static_url_path='/qrimg', static_folder='qrimg')

app.config['SECRET_KEY'] = SECRET_KEY = os.urandom(12)

print("*******************************")
print("*                             *")
print("*           Welcome!          *")
print("*                             *")
print("*******************************")

# Main Page
@app.route('/', methods=['GET', 'POST'])
def index():
        return render_template('index.html', qrcodename="qr_carlaheywood.com.png", current_year=datetime.now().year)

@app.route('/newQRcode', methods=['POST'])
def makeqrcode():
    # https://github.com/lincolnloop/python-qrcode
    
    weblink = request.form['weblink']
    print("Weblink: ",weblink)

    # Encoding data using make() function
    img = qrcode.make(weblink)
    
    # Saving as an image file
    qrcodename = "qr_" + weblink[8:] + ".png"
    print(qrcodename)
    img.save('qrimg/' + qrcodename)

    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
    qr.add_data(weblink)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())
    return render_template('index.html', qrcodename=qrcodename, current_year=datetime.now().year)

app.debug = False
if __name__ == '__main__':
#    app.run(debug=bool(os.environ.get('FLASK_DEBUG', False)))
#    server = Server(app.wsgi_app)
#    server.serve(host='0.0.0.0', port=5000)
   app.run(host='0.0.0.0', port=5000)
