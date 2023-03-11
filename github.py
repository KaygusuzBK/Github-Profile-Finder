from flask import Flask,redirect,url_for,render_template,request
import requests
base_url = 'https://api.github.com/users/'

app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        githubname = request.form.get("githubname")
        response_user = requests.get(base_url + githubname)
        userinfo = response_user.json()
        response_user = requests.get(base_url + githubname +'/repos')
        repos = response_user.json()
        
        if "message" in userinfo:
            return render_template('index.html', error = "Böyle bir kullanıcı yok")
        else:
            return render_template('index.html', profile = userinfo, repos = repos)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)