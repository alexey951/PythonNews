from flask import Flask
import pyodbc


app = Flask(__name__)

#подключение бд
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-JH3KBFP;DATABASE=dbnews;')
cursor = conn.cursor()

#get запрос
@app.route('/news', methods=['GET'])
def get():
    result = []
    query = "select * from news"
    cursor.execute(query)
    for row in cursor.fetchall():
        news_dict = {}
        news_dict["id"] = row[0]
        news_dict["name"] = row[1]
        news_dict["title"] = row[2]
        news_dict["publishedAt"] = row[3]
        news_dict["description"] = row[4]
        news_dict["url"] = row[5]
        news_dict["urlToImage"] = row[6]
        result.append(news_dict)
    return result


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

