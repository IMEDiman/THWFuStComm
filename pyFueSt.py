from flask import Flask, render_template, request, redirect, url_for


from src.funker import Funker
from src.ldf import LdF

class pyFueSt:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()
        self.agents = {"funker":[], "ldf": []}

    def setup_routes(self):
        self.app.route("/")(self.home)
        self.app.route("/login", methods=['POST'])(self.login)
        self.app.add_url_rule('/<role>', view_func=self.main)

    def home(self):
        return render_template('index.html')

    def login(self):
        user_sign = request.form['user_sign']
        user_pw = request.form['user_pw']
        user_role = request.form['user_role']
        if user_role == "Funker":
            self.agents["funker"].append(Funker(user_sign))
        elif user_role == "LdF":
            self.agents["ldf"].append(LdF(user_sign))

        print(f"Received from client: {user_sign}, {user_pw}, {user_role}")
        return redirect(url_for('main', role=user_role))
        #return render_template('index.html', message=f"Login: {user_sign} als {user_role}")
    
    def main(self, role):
        print(self.agents)
        if role == "Funker":
            return render_template('funker.html')
    
    def run(self):
        self.app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    pyFueSt_app = pyFueSt()
    pyFueSt_app.run()
    
