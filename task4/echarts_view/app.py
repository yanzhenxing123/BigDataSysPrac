from flask import Flask,render_template
from mysql import Mysql

app = Flask(__name__)
@app.route('/')
def getdata():
    db = Mysql()
    items1 = db.getItems1()
    items2 = db.getItems2()
    items3 = db.getItems3()
    items4 = db.getItems4()
    return render_template('echarts.html', items1 = items1, items2 = items2, items3 = items3, items4 = items4)

if __name__ == '__main__':
    app.run(debug = True, port=5002) #debug=True发生错误时会返回发生错误的地方
