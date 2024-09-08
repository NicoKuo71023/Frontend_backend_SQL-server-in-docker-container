from flask import Flask, request, jsonify
from mysql_connector import sql_query 
from flask_cors import CORS
import csv  

app = Flask(__name__)
CORS(app)

# 定義一個路由來接收前端的請求
@app.route('/get-data', methods=['POST'])
def get_data():
    # 檢查請求中是否包含 JSON 數據
    if request.is_json:
        # 從請求中獲取 JSON 數據
        data = request.get_json()
        
        # 對接收到的數據進行處理（這裡只是範例，只有印出，你可以根據需要處理數據）
        print("Received data:", data)
        db_list = sql_query("docker_db", "select * from passengers")
        
        # 準備要返回的 JSON 數據(可在此撰寫回傳mysql資料庫資料的程式碼)
        response_data = {
            "status": "success",
            "message": "Data received successfully!",
            "data" : data,
            "db": db_list  # 這裡直接回傳接收到的數據，以及從mysql讀到的db列表
        }
        
        # 返回 JSON 響應
        return jsonify(response_data), 200
    else:
        # 如果請求中沒有 JSON 數據，返回錯誤信息
        return jsonify({"status": "error", "message": "Request must be JSON"}), 400

def checkDatabase(): # 如果database:docker_db 不存在就建立
    result = sql_query("mysql","""CREATE DATABASE IF NOT EXISTS docker_db 
                        CHARACTER SET utf8mb4
                        COLLATE utf8mb4_unicode_ci;""")  

def checkTable(): # 如果 table:passengers 不存在就建立 並插入資料
    result = sql_query("docker_db","""CREATE TABLE IF NOT EXISTS passengers(
                        PassengerId INT primary key auto_increment, 
                        Survived INT, 
                        Pclass INT, 
                        Name VARCHAR(100), 
                        Sex VARCHAR(6), 
                        Age INT, 
                        Sibsp INT, 
                        Parch INT, 
                        Ticket VARCHAR(30),
                        Fare DOUBLE,  
                        Cabin VARCHAR(30),
                        Embarked VARCHAR(5)
                        );""")

def insertData(): # 確認 table 中有沒有資料 如果沒有就 insert data 
    result = sql_query("docker_db","SELECT COUNT(*) FROM passengers") # 拿到一個 list 元素為dict [{'COUNT(*)': 0}]
    
    if result[0]['COUNT(*)'] == 0:  # 確認 table 中有沒有資料
        data = readData()
        i = 0
        for row in data:
            
            data_Cleansing(row)
            sql = f"""
                    INSERT IGNORE INTO passengers (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)
                    VALUES ({row[0]}, {row[1]}, {row[2]}, '{row[3]}', '{row[4]}', {row[5] if row[5] else 'NULL'}, 
                            {row[6]}, {row[7]}, '{row[8]}', {row[9]}, {f"'{row[10]}'" if row[10] else 'NULL'}, '{row[11]}');
                """
            # print(sql)
            result = sql_query("docker_db", sql)
            # print(result)
            

def readData():  #讀取資料
    csv_rows=[]
    with open("titanic_csv/train.csv", mode="r", newline='') as data:
        csv_reader = csv.reader(data) # 建立指標物件
        next(csv_reader) # 跳過欄位名稱
        for row in csv_reader:  # 將資料儲存成list
            csv_rows.append(row)
    return csv_rows
    
def data_Cleansing(data):    # 處理單筆資料空值
    data[3] = data[3].replace("'", "''") if data[3] else None
    data[8] = data[8].replace("'", "''") if data[8] else None
    data[10] = data[10].replace("'", "''") if data[10] else None
    data[11] = data[11].replace("'", "''") if data[11] else None  
    return data

if __name__ == '__main__':
    checkDatabase() # falsk 執行前先確認 sql 中資料是否存在
    checkTable()
    insertData()
    # 指定host 0.0.0.0使他可以接收任何ip的遠端api請求
    app.run(host='0.0.0.0', port=5000, debug=True)
  
