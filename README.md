# Gaia WebGL

My attempt at displaying the Gaia sources in WebGL

## Running

* Download the Gaia TGAS sources to `gaia_data`
* Install the python requirements
* Run the python script `convert_to_cartesian.py`
* Install the npm packages with `yarn`: `yarn install`
* Use `webpack` to compile the `src/main.js` to `static/bundle.js`: `./node_modules/.bin/webpack src/main.js static/bundle.js`
* Run the python `server.py`
* Visit `localhost:5000`

## Python requirements

* numpy
* fitsio
* flask
