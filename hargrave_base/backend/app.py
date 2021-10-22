

from hargrave_base import app


def run_server():
    app.run(debug=True, port=8000, host='0.0.0.0') 


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0') 
