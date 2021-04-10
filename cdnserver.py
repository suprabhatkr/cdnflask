from flask import Flask,request,jsonify,send_from_directory
from flask_restful import Resource,Api 
import json
import ast
import os
import os.path

app = Flask(__name__, static_url_path='') 
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)
api = Api(app) 
Data= [] 
class People(Resource):
    def get(self):
        for x in Data:
            if x['Data'] == name:
                return x 
        return {"Data":"nothing there"}
    def post(self):
        debugger = open('debug.txt','w')
        request_data = request.get_data()
        dict_str = request_data.decode("UTF-8")
        data = ast.literal_eval(dict_str) 
        #data = jsonify(request_data)
        if ".css" in data['url']:
            curr_path = "css" 
        else:
            curr_path = 'js'
        url=data['url'].replace('\'',"")
        url=url.replace('\\',"")
        url=url.replace('http://127.0.0.1/',"")
        debugger.write(url)
        for folder in url.split('/')[:-1]:
            curr_path+="/"+folder
            debugger.write(curr_path)
            if not os.path.isdir(curr_path):
                os.mkdir(curr_path) 
        f = open(curr_path+"/"+data['url'].split('/')[-1],'w') 
        f.write(data['content'])
        f.close() 
        debugger.close()
        return url 

    def delete(self):
        for ind,x in enumerate(Data):
            if x['Data'] == name:
                Tem = Data.pop(ind) 
                return {'Note':'Deleted'} 

api.add_resource(People,"/")

if __name__ == "__main__":
    app.run(debug=True) 