import requests, json
print(requests.post('http://13.125.222.176/quiz/jordan' ,
data = json.dumps({'nickname' : "대전2반김아현", 'yourAnswer' : "kubernetes"}), headers = {'Content-Type' : 'application/json'}).json())