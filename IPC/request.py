import requests

url = "http://172.17.99.254/api/"


class RequestsPost:
    def __init__(self, emailIn, passwordIn):
        self.email = emailIn
        self.password = passwordIn

    def postMessageDate(self, robotId, userName, content, created):
        payload = {'email': self.email, 'password': self.password, 'robotId': robotId, 'userName': userName, 'content': content, 'created': created}
        r = requests.post(url + 'messages/', data=payload)
        print(r.text)

    def postMessageDate(self, speedRight, speedLeft, headPosition, duration, direction):
        payload = {'email': self.email, 'password': self.password, 'speedRight': speedRight, 'speedLeft': speedLeft,
                   'headPosition': headPosition, 'duration': duration, 'direction':direction}
        r = requests.post(url + 'movements/', data=payload)
        print(r.text)

    def postMessage(self, robotId, userName, content):
        payload = {'email': self.email, 'password': self.password, 'robotId': robotId, 'userName': userName, 'content': content}
        r = requests.post(url + 'messages/', data=payload)
        print(r.text)

    def testConnection(self):
        r = requests.get(url)
        print(r.status_code)
        print(r.text)

if __name__ == '__main__':
    request = RequestsPost("test@bla.com", "password123")
    request.postMessage(1, "adrien", "happyMessage")