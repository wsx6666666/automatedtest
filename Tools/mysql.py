import pymysql.cursors
# 连接数据库


conn = pymysql.Connect(
    host='47.111.109.158',
    port=3306,
    user='root',
    passwd='fjUuex7REd0dvBJS',
    db='content_risk',
    charset='utf8'
)
curs = conn.cursor()
# 事务处理
sql_1 = "SELECT id FROM merchant_application ORDER BY id ASC LIMIT 1"
sql_2 = "SELECT id FROM merchant_system_rbac_role ORDER BY id DESC LIMIT 1"

try:
    curs.execute(sql_1)
    curs.execute(sql_2)
except Exception as e:
    conn.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    conn.commit()  # 事务提交
    print('事务处理成功', curs.rowcount)
ret = curs.fetchall()
# 关闭连接
curs.close()
conn.close()
print(ret[0][0])