import os, sys
# lấy ra đường dẫn đến thư mục modules ở trong projetc hiện hành
lib_path = os.path.abspath(os.path.join('corona'))
# thêm thư mục cần load vào trong hệ thống

sys.path.append(lib_path)
from flask import Flask, render_template, request
import predict
import nhandien
from corona import run

app = Flask(__name__)
# covid = main()
name = nhandien.main()
@app.route("/")
def home():
    return render_template("index.html",data=name)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if(userText == "corona"):
        return run.world()
    elif(userText == "corona vn"):
        return run.Vietnam()
    else:
        return predict.response(userText, userID='1', show_details=False)


if __name__ == "__main__":
    app.run(host='localhost',port=1234)
