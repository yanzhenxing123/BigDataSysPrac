"""
@Author: yanzx
@Date: 2022/6/16 8:41
@Description: 
"""
import phoenixdb
import phoenixdb.cursor

# database_url = 'http://localhost:8765/'
# database_url = 'http://192.168.26.129:8765/'
database_url = 'http://192.168.26.128:8765/'
conn = phoenixdb.connect(database_url, autocommit=True)
cursor = conn.cursor()
cursor.execute("""
SELECT * FROM "player_salary" limit 10
""")

print(cursor.fetchall())
