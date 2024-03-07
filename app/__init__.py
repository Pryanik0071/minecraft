from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('main_page/index.html')

    # @app.route('/bluetooth-aoa-technology/')
    # def bluetooth_aoa():
    #     return render_template('bluetooth_aoa/index.html')
    #
    # @app.route('/in-progress/')
    # def progress():
    #     return render_template('progress.html')

    return app
