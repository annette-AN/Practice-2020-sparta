from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')

# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 클라이언트가 줄 데이터를 담을 변수 (이름/ 수량/ 주소/ 전화번호)
    data_name = request.form['name']
    data_count = request.form['count']
    data_address = request.form['address']
    data_tel = request.form['tel']

    user_data = {
        'name': data_name,
        'count': data_count,
        'address': data_address,
        'tel': data_tel,
    }
    db.users.insert_one(user_data)
    return jsonify({'result': 'success'})

# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.users.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)