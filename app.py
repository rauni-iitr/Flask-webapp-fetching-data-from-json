from flask import Flask, request
import json

global json_dict 

def read_file(): 
    global json_dict 
    json_dict = {} 
    with open("./result.json", 'r') as f:
        for line in f.readlines():
            _dict= json.loads(line)
            json_dict[_dict['Name']] = _dict['Entity']
        
        
        #print(json_dict)

app = Flask(__name__)

@app.route('/')
def index():
    return '''<form method="POST" action = "/result">
        Input you Text  <input type="text" name="Name">
        <input type ="Submit">
        </form>'''

@app.route('/result',methods=['POST'])
def result():
    req_data=request.form["Name"]
    #json_file = {"Oz": "Person", "Jake": "Person"}
    #print(req_data)
    ans=json_dict.get(req_data,"Not Found")
    return '''<h1>
            The Entity is {}.
            </h1>'''.format(ans)

if __name__ == "__main__":
    read_file() 
    app.run(debug=True, port=5000)