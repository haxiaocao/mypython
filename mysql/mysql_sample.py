import pymysql

config={
"host":"localhost",
"port":5678,
"user":"guokai2",
"password":"111111",
"db":"oktest",
"charset":"utf8"
}
db=pymysql.connect(**config)
cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone()
sql="select * from oktest.student"
cursor.execute(sql)
results=cursor.fetchall()
for row in results:
    id=row[0]
    name=row[1]
    print("id:{},name:{}",id,name)
