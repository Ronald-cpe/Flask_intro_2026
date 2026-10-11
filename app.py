from math import isfinite, pi

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/works/linklist')
def linklist():
    return render_template('linkedlist.html')

@app.route('/works/stack')
def stack():
    return render_template('stack.html')

@app.route('/works/infix-postfix')
def infix_postfix():
    return render_template('in/postfix.html')

@app.route('/works/uppercase', methods=['GET', 'POST'])
def uppercase():
    result = None
    input_string = ''
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result, input_string=input_string)

@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    error = None
    radius = ''

    if request.method == 'POST':
        radius = request.form.get('radius', '').strip()

        try:
            radius_value = float(radius)
            if not isfinite(radius_value):
                error = 'Enter a finite number for the radius.'
            elif radius_value < 0:
                error = 'Radius cannot be negative.'
            else:
                area = pi * radius_value ** 2
                if isfinite(area):
                    result = area
                else:
                    error = 'Radius is too large to calculate.'
        except ValueError:
            error = 'Enter a valid number for the radius.'

    return render_template('circle.html', result=result, error=error, radius=radius)

@app.route('/works/area/triangle', methods=['GET', 'POST'])
def triangle():
    result = None
    error = None
    base = ''
    height = ''

    if request.method == 'POST':
        base = request.form.get('base', '').strip()
        height = request.form.get('height', '').strip()

        try:
            base_value = float(base)
            height_value = float(height)
            if not isfinite(base_value) or not isfinite(height_value):
                error = 'Enter finite numbers for the base and height.'
            elif base_value < 0 or height_value < 0:
                error = 'Base and height cannot be negative.'
            else:
                result = base_value * height_value / 2
        except ValueError:
            error = 'Enter a valid number for both the base and height.'

    return render_template(
        'triangle.html',
        result=result,
        error=error,
        base=base,
        height=height,
    )

# @app.route('/areaOfcirle', methods=['GET', 'POST'])
# def areaOfcirle():
#     result = None
#     name=request.get('name','')
#     print(name)
#     if request.method == 'POST':
#         input_string = request.form.get('inputradius', '')
#         result = int(input_string) * int(input_string) * 3.14
#     return render_template('areaCircle.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
