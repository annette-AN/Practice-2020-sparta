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


@app.route('/post_board', methods=['POST'])
def post_board():
    # 1. 클라이언트가 전달한 post 데이타를 서버변수에 저장한다.
    name_board = request.form['post_board_name']
    name = {'board': name_board}
    db.board.insert_one(name)
    return jsonify({'result': 'success'})

@app.route('/post_category', methods=['POST'])
def post_category():
    # 1. 클라이언트가 전달한 post 데이타를 서버변수에 저장한다.
    name_category = request.form['post_category_name']
    name = {'category': name_category}
    db.category.insert_one(name)
    return jsonify({'result': 'success'})

@app.route('/get_board', methods=['GET'])
def get_board():
    name_board = list(db.board.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'board_names': name_board})

@app.route('/get_category', methods=['GET'])
def get_catogory():
    name_category = list(db.category.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'category_names': name_category})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)