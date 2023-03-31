"""
@Author: yanzx
@Date: 2022/6/16 9:14
@Description: 
"""
from flask import Flask, url_for, render_template
import phoenixdb
import phoenixdb.cursor

# database_url = 'http://localhost:8765/'
database_url = 'http://192.168.26.128:8765/'
conn = phoenixdb.connect(database_url, autocommit=True)

cursor = conn.cursor()
cursor.execute(
    "select \"team\",sum(to_number(\"win\")) from \"team_season\" group by \"team\"order by sum(to_number(\"win\")) desc limit 5")
data = cursor.fetchall()
print('data1: ', data)
cursor.execute(
    "select \"team\",avg(to_number(\"score\")) from \"team_season\" group by \"team\"order by avg(to_number(\"score\")) desc limit 3")
data2 = cursor.fetchall()
print('data2: ', data2)

# 薪资分析
# sql = """select "name", "salary" from "player_salary" order by "salary" desc limit 5 """
# cursor.execute(sql)
# data3 = cursor.fetchall()
# print('data3: ', data3)


app = Flask(__name__)


@app.route('/')
def user():
    return render_template('myindex.hml', num0=data[0][1], num1=data[1][1], num2=data[2][1], num3=data[3][1],
                           num4=data[4][1], team0=data[0][0], team1=data[1][0], team2=data[2][0], team3=data[3][0], team4=data[4][0],

                           score0=data2[0][1], score1=data2[1][1], score2=data2[2][1],
                           team_score0=data2[0][0], team_score1=data2[1][0], team_score2=data2[2][0],

                           # name0=data2[0][1], name1=data2[1][1], name2=data2[2][1], name3=data2[3][1], name4=data2[2][1],
                           # team_score0=data2[0][0], team_score1=data2[1][0], team_score2=data2[2][0],

                           )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
