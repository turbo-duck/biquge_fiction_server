import sqlite3

# 连接到第一个数据库
conn1 = sqlite3.connect('./tubro-duck/biquge_fiction_spider/db/biquge.db')
cursor1 = conn1.cursor()

# 连接到第二个数据库
conn2 = sqlite3.connect('./tubro-duck/biquge_fiction_server/db.sqlite3')
cursor2 = conn2.cursor()

# 获取 A 表的列名
cursor1.execute("PRAGMA table_info(chapter_detail_list)")
columns_info = cursor1.fetchall()
column_names = [info[1] for info in columns_info]

# 分批查询并插入数据
batch_size = 10000
offset = 0

while True:
    cursor1.execute(f"SELECT * FROM chapter_detail_list LIMIT {batch_size} OFFSET {offset}")
    rows = cursor1.fetchall()
    if not rows:
        break
    insert_query = f"INSERT INTO fiction_chapterdetaillist ({', '.join(column_names)}) VALUES ({', '.join(['?' for _ in column_names])})"
    cursor2.executemany(insert_query, rows)
    conn2.commit()
    offset += batch_size
    print(f"{offset} rows transferred")

# 关闭连接
conn1.close()
conn2.close()

print("数据导入完成")
