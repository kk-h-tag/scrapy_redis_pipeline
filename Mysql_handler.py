import time
import pymysql
import json

class mysql_item_handler(object):
    def __init__(self, **mysql_kwargs):
        self.item_data = []

        self.db_conn = pymysql.connect(**mysql_kwargs)

    def data_length(self):
        return len(self.item_data)

    def clear_data(self):
        self.item_data.clear()

    def add_item_data(self, redis_data):
        for raw_dict in redis_data:
            raw_dict = json.loads(raw_dict.decode())
            #todo 아래 item data field에 redis 에서 pop 한 데이터를 tuple로 변환할 수 있게 raw_dict 사용하여 변경.
            self.item_data.append(tuple(("item data field")))

    def item_insert(self):
        # todo 아래 sql_query를 자신의 테이블에 맞게 변경.
        sql_query = '''INSERT INTO your table (your table schema) 
                            values (%s)'''
        cursor = self.db_conn.cursor()
        start = time.time()
        cursor.executemany(sql_query, self.item_data)
        end = time.time()
        cursor.close()
        self.db_conn.commit()
        self.clear_data()
        print(f"{end - start:.5f} sec")