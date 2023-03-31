"""
@Author: yanzx
@Date: 2022/6/15 10:46
@Description: 
"""
import pandas as pd

li = ['player_advance', 'player_salary', 'player_season', 'team_history_data', 'team_all',
      'team_playoff', 'team_season']


def get_colunm(column):
    string = f""""cf1"."{column}" varchar,"""
    return string


def main():
    for table_name in li:
        path = './data/' + table_name + ".csv"
        df = pd.read_csv(path)
        columns = list(df.columns)
        sql_li = [f"""create table "{table_name}" (
    id varchar primary key,"""]
        for i in range(1, len(columns)):
            column = columns[i]
            res = get_colunm(column)
            # 把最后一个,去掉
            if i == len(columns) - 1:
                res = get_colunm(column)
                res = res[:-1]
            sql_li.append(res)
        sql_li.append(")column_encoded_bytes = 0;")
        sql = "\n".join(sql_li)
        print(f"=============已完成{table_name}================")
        print(sql)


if __name__ == '__main__':
    main()
