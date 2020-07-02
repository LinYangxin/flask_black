from flask import escape, send_from_directory, make_response, jsonify, render_template, request
from app.main import app

@app.route('/')
def template_index():
    return render_template('index.html')

#have some bugs
@app.route('/<string:next_page>')
def template_next_page(next_page):
    if not next_page.endswith(".html"):
        next_page = next_page + ".html"
    try:
        return render_template(next_page)
    except Exception as e:
        return jsonify({"code": "404", "message": "{}".format(e)})

# 通过把 URL 的一部分标记为 <variable_name> 就可以在 URL 中添加变量。标记的部分会作为关键字参数传递给函数。
# 通过使用 <converter:variable_name> ，可以选择性的加上一个转换器，为变量指定规则。
# @app.route('/show_user_id/<int:user_id>')
# def show_user_id(user_id):
#     return "user id is %s" % escape(user_id)

# 发送文件，make_response构建响应
# @app.route('/getFile/')
# def get_file():
#     try:
#         response = make_response(send_from_directory('./static', 'testFile.txt', as_attachment=True))
#         return response
#     except Exception as e:
#         return jsonify({"code": "异常", "message": "{}".format(e)})

# 渲染模版，render_template可以渲染模版，传递参数，在html处用{{参数}}读取，传递全部的本地变量给template，使用**locals()
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('testHTML.html', name=name)

# 测试request,用request.args.get获取url参数，URL用?参数1=xxx&参数2=XXXXX
# @app.route('/test_request', methods=['GET'])
# def test_request():
#     username = request.args.get('username')
#     id = request.args.get('id')
#     return jsonify({"code": "200-200", "message": username, "id": id})