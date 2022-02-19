# 🐍 WeatherBoard

Dashboard which can get weather informations about city.

### 📦 Dependencies installation

```
$ pip3 install -r requirements.txt
```

### ❓ How to use ?

#### Default Mode :

```
$ python3 app.py
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'my_dash.maindash' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
```

#### Debug Mode :

```
$ python3 app.py
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'my_dash.maindash' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on

[DEBUG] << 03:04:09 >>
URL=https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=40.7127281&lon=-74.0060152&units=metric&dt=1645236248&appid=6021ba231b6d784afa939de3dd0b8d83

       City                Time Weather Main Weather Description  ... Temperature Felt  Pressure  Humidity  Wind Speed
0  New York 2022-02-19 01:00:00        Clear           clear sky  ...            -4.63      1016        37        7.72
1  New York 2022-02-19 02:00:00        Clear           clear sky  ...            -5.48      1018        41        6.69
2  New York 2022-02-19 03:00:00        Clear           clear sky  ...            -6.02      1018        43        6.17
3  New York 2022-02-19 03:04:08        Clear           clear sky  ...            -6.02      1018        43        6.17

[4 rows x 10 columns]
```

### Result :
!["result_01"](https://i.imgur.com/ZCWqPJe.png)
!["result_02"](https://i.imgur.com/P4bsF7l.png)
!["result_03"](https://i.imgur.com/WPAPwQO.png)
