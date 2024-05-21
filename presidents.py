from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)

presidents_list = convert_to_dict("presidents.csv")

pairs_list = []
for p in presidents_list:
    pairs_list.append((p['Presidency'], p['President']))

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Presidents Index")

@app.route('/president/<num>')
def detail(num):
    try:
        pres_dict = presidents_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Presidency: {num}</h1>"
    ord = make_ordinal(int(num))
    return render_template('president.html', pres=pres_dict, ord=ord, the_title=pres_dict['President'])

if __name__ == '__main__':
    app.run(debug=True)