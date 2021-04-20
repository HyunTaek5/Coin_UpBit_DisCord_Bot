import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='1234',
                     db='UpBit',
                     charset='utf8')

try:
    with db.cursor() as cursor:
        sql = f"""
            CREATE
        """
        cursor.execute(sql)
        db.commit()
finally:
    db.close()