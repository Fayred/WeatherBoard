import dash

from package import make_layout
from package import arguments

from my_dash.maindash import app

if __name__ == "__main__":
    app.layout = make_layout()
    app.run_server(debug=True)