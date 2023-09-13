from flask_app import app

from flask_app.controllers.burgers import burgers
import flask_app.controllers.restauarnts
if __name__=="__main__":
    app.run(debug=True, host='localhost', port=7100)