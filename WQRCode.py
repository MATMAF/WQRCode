import qrcode
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['qr_data']
    front_color = request.form['front_color']
    back_color = request.form['back_color']
    qr = qrcode.QRCode(version=2, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=front_color, back_color=back_color)
    img.save('static/qr_code.png')
    return render_template('qr_generated.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
