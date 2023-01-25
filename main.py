from flask import Flask
from flask import render_template,request,redirect,url_for,flash
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route("/searchcode",methods=['POST'])
def searchcode():
    # user input code
    code = request.form['code']
    
    # read database
    text_str = read_json('genshin_code.json')
    
    # check  repeat code with input code and database
    ans = check_repeat_code(code,text_str)

    # output answer
    if ans == "序號已存在":
        flash('序號已存在')
    elif ans == "序號可使用":
        flash('序號可使用')
    else:
        flash('有BUG, 請等待修復')
    return redirect(url_for('index'))



def read_json(filename):
    text_str = {}
    try:
        with open(filename, "r", encoding='utf8') as f:
            text_str = json.loads(f.read())
    except:
        print("Can't find json file.\n")
    return text_str



def check_repeat_code(code,text_str):
    # code = new code
    # _code = the code in json file
    if text_str != {}:
        for item in text_str.keys():
            for _code in text_str[item]['code']:
                if code == _code:      
                    return "序號已存在"
        return "序號可使用"
    else:
        flash("找不到比對資料，無法比對序號，請回報問題")




if __name__ == '__main__':
    app.debug = True
    app.secret_key = "your key"
    app.run()