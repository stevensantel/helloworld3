from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Steven Santel! I am adding my first code change.'


@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/favorite-course')
def favorite_course():
    print('Course subject entered: ' + request.args.get('subject_name'))
    print('Course number entered: ' + request.args.get('course_number'))

    return render_template('favorite-course.html')


@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run()
