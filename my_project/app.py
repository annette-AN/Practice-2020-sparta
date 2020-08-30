from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbproject

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
# @app.route('/api/list', methods=['GET'])
# def show_stars():
#     # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
#     # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
#     # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
#     return jsonify({'result': 'success', 'msg': 'list 연결되었습니다!'})

# def next_id():
#
    # nextId = thisId + 1
    # db.nextId.update_one({'next_board' : {$set: {nextId}}})

@app.route('/api/boards', methods=['POST'])
def post_board():
    b_name = request.form['board_name']
    row_ids = db.nextId.find().limit(1)[0]
    b_id = row_ids['next_board']
    data = {'b_Id': b_id, 'name': b_name}

    db.board.insert_one(data)
    db.nextId.update_one({'next_board': b_id}, {'$set': {'next_board': b_id + 1}})
    return jsonify({'result': 'success'})

@app.route('/api/boards', methods=['GET'])
def get_boards():
    boards = list(db.board.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'board': boards})

@app.route('/api/boards', methods=['PUT'])
def put_board():
    # board_name = list(db.board.find({}, {'_id': False}))
    return jsonify({'result': 'success'})


@app.route('/api/categorys', methods=['POST'])
def post_category():
    c_name = request.form['category_name']
    b_id = request.form['board_id']
    row_ids = db.nextId.find().limit(1)[0]
    c_id = row_ids['next_category']
    data = {'b_id': b_id, 'c_Id': c_id, 'name': c_name}

    db.category.insert_one(data)
    db.nextId.update_one({'next_category': c_id}, {'$set': {'next_category': c_id + 1}})
    return jsonify({'result': 'success'})

@app.route('/api/categorys', methods=['GET'])
def get_catogory():
    categorys = list(db.category.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'category': categorys})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)