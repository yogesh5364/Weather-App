from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('weather.html')
@app.route('/weather<city>')
def weather(city):
    key="Mmr8VF9HZErNLHxjugyJJBEGIxi9R8kD"
    #city = input("Enter the city name --> ")
    loc_url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={key}&q={city}"
    data = requests.get(loc_url)
    if data.status_code == 200:
        data = data.json()
        loc_key = data[0]['Key']
        final_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{loc_key}?apikey={key}&details=true&metric=true"
        d = requests.get(final_url)
        if d.status_code == 200:
            d = d.json()
            return d
        else:
            print("No Records Found!!")
    else:
        print("No Records Found!!")

@app.route('/search',methods=['POST','GET'])
def search():
    if request.method == 'POST':
        city = request.form['city']
        return redirect(url_for('weather',city=city))
    else:
        request.args.get('city')
        return redirect(url_for('weather',city=city))
if __name__ == '__main__':
    app.run(host='localhost',debug=True,port=80)
