# from flask import Flask

# app = Flask(__name__)

# @app.route("/",methods = ['GET','POST'])
# def index():
#     return "Starting Machine Learning Project"


# if __name__=="__main__":
#     app.run(debug = True)





from flask import Flask

app = Flask(__name)

@app.route('/',methods = ['GET','POST'])
def index():
    return 'THis is my first project ever'


if __name__=='__main__':
    app.run(debug = True)