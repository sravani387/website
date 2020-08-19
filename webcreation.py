try:
    from flask import Flask,render_template
    from errorhandlers import errors
    app = Flask(__name__)
    @app.route("/")
    @app.route("/index.html")
    def home():
       return render_template("index.html")
    @app.route("/services.html")
    def services():
       return render_template("services.html")
    @app.route("/contact.html")
    def contact():
       return render_template("contact.html")
    @app.route("/about.html")
    def about():
        return render_template("about.html")
    errors(app)
        
    if __name__=='__main__':
           app.run(debug=True)
except IOError as error:
       print(error)
except FileNotFoundError as error:
       print(error)
except ImportError as error:
       print(error)



