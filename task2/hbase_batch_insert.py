"""
@Author: yanzx
@Date: 2022/6/15 8:32
@Description:
"""

# coding: utf-8
import happybase
import pandas as pd
li = [
    # 'player_advance',
    #   'player_salary',
    #   'player_season',
    #   'team_history_data',
    #   'team_all',
    #   'team_playoff',
      'team_season']
count = 0
for table_name in li:
    path = './data/' + table_name + ".csv"
    df = pd.read_csv(path)
    columns = list(df.columns)
    hcolumns = []
    for i in columns:
        hcolumns.append('cf1:' + i)
    length = len(hcolumns)
    conn = happybase.Connection(
        # host='hbase-master',
        # host='192.168.26.129',
        host='192.168.26.128',
        port=9090,
        timeout=None,
        autoconnect=True,
        table_prefix=None,
        table_prefix_separator=b'_ ',
        compat='0.98',
        transport='buffered',
        protocol='binary'
    )
    # table = happybase.Table('team_season', conn)
    table = happybase.Table(table_name, conn)
    batch = table.batch(batch_size=100)
    f = open(path, 'r', encoding='utf-8')
    n = 0
    lines = f.readlines()
    for line in lines[1:]:
        line = line.strip('.\n')
        line = line.split(',')
        for i in range(length):
            batch.put(str(n), {hcolumns[i]: line[i]})
        n = n + 1
    f.close()
    conn.close()
    count += 1
    print(f"已完成{count}个, {table_name}")
