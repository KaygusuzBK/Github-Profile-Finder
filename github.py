from flask import Flask,redirect,url_for,render_template,request
import requests
base_url = 'https://api.github.com/users/'

app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        githubname = request.form.get("githubname")
        response = requests.get(base_url + githubname)
        userinfo = response.json()
        return render_template('index.html', profile = userinfo)
    
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)