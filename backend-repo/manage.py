import os
from __init__ import create_app

a = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    a.run(debug = True, host = 'localhost', port = 80)