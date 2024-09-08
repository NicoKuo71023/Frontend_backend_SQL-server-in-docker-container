import pymysql
import pymysql.cursors
# 連接遠端MySQL資料庫需要安裝cryptography處理憑證問題。pip install cryptography

def sql_query(database, query):
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="P@ssw0rd",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
        database=database
    )

    with connection.cursor() as cursor:
        cursor.execute(query)
        cursor.execute(query)
            # 如果是插入語句，需要提交更改
        if query.strip().upper().startswith("INSERT"):
            connection.commit()
            print("Data inserted successfully.")
            return None
        else:
            # 如果是其他查詢（例如 SELECT），則返回結果
            result = cursor.fetchall()
            return result
    
    

if __name__ == "__main__":
    # result = sql_query("test12345","SHOW DATABASES;")
    # print(result)
    result = sql_query("docker_db", "INSERT INTO passengers (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked) VALUES (726, 0, 3, 'Oreskovic, Mr. Luka', 'male',20,0, 0, '315094', 8.6625, NULL, 'S')")
    print(result)