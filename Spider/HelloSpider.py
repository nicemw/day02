import urllib
from urllib import request

def get_data():
    response = urllib.request.urlopen('http://localhost:8000/myapp/hello/')
    print(response.read().decode('utf-8'))
if __name__ == '__main__':
    get_data()