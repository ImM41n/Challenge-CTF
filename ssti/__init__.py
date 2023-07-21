from flask import Flask, render_template_string, request


app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    user = request.args.get('user') or None

    template = '''
    <html><head><title>Universe</title><style>body {margin: 90px; background-image: url('{{url_for('static', filename='bg.jpg')}}');}</style></head><body>
    '''

    footer = '''
    <br><p style="margin-top: 30px;">
    Follow me: <a href="https://universe.leagueoflegends.com/vn_VN/champion/aatrox/" target="_blank" style="color: #C21010">Aatrox</a>&nbsp;&nbsp;
    <a href="https://universe.leagueoflegends.com/vn_VN/champion/ahri/"  target="_blank" style="color: #C21010">Ahri</a>
    '''

    if user == None:
        template = template + '''
        <h1>Tôi gọi bạn là gì?</h1>
        <form>
        <input name="user" style="border: 2px solid #C21010; padding: 10px; border-radius: 10px; margin-bottom: 25px;" value=""><br>
        <input type="submit" value="Nhập" style="border: 0px; padding: 5px 20px ; color: #C21010;">
        </form>
        '''.format(user) + footer
    else:
        template = template + '''
        <h1>Hi {}</h1>
        Get ready the enemies will arrive in 5 seconds<br>
        Chào mừng bạn đã đến với kỷ nguyên vô tận !!.
        '''.format(user) + footer
    
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8089)
