from flask import Flask
from flask import request
from process import CompareString

app = Flask(__name__)
instance=CompareString()

@app.route("/")
def hello_world():
    return "<p>Hello, World! The server is running in uwsgi mode</p>"

@app.route("/comparestring",methods=['POST','GET'])
def processData():
    if request.method == 'POST':
        print(request.form)
        ans = instance.sentenceSimilarity(request.form["s1"],request.form["s2"])
        print(ans)
    #   user = request.form['nm']
        return "<p>Similarity: "+str(ans)+"</p>"
    else:
      return "<p>Please submit data in post with variable s1 and s2!</p>"

if __name__ == "__main__":
    app.run()