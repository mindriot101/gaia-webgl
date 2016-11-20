from flask import Flask, render_template, jsonify
import fitsio
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data/<int:index>')
def fetch_data(index):
    fname = './TgasSource_000-000-{:03d}_cartesian.fits'.format(index)
    with fitsio.FITS(fname) as infile:
        x = infile[1]['x'].read()
        y = infile[1]['y'].read()
        z = infile[1]['z'].read()

    ind = np.isfinite(x) & np.isfinite(y) & np.isfinite(z)
    return jsonify({
        'x': x[ind].tolist(),
        'y': y[ind].tolist(),
        'z': z[ind].tolist()})

if __name__ == '__main__':
    app.run(debug=True)
