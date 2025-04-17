# hive_utils.py
from pyhive import hive

def get_connection(host: str, timeout=10):
    """获取Hive连接（带超时控制）"""
    return hive.connect(host, timeout=timeout)

def execute_query(conn, sql: str) -> list:
    """执行查询并返回结果"""
    with conn.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()