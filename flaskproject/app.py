import os.path
from flask import Flask, Response, g, render_template, jsonify
from queries import availability, weekly

app = Flask(__name__)
app.config.from_object(__name__)
app.debug=True



@app.route('/')
def root():  
    return render_template('DublinBikes.html')
    

    


@app.route("/test/<int:stand_no>", methods=['GET'])
def avail(stand_no):      
    #print("stand no is: %d" % stand_no)
    return availability(stand_no)

@app.route("/weekly/<int:stand_no>", methods=['GET'])
def week(stand_no):
    return weekly(stand_no)
        
        
if __name__ == '__main__':  
    app.run(port=5000)

# @app.route("/<int:num>", methods=['GET'])
# def current(num):
#     return history(num)
