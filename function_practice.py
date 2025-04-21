


from hive_utils import get_connection, execute_query
import pandas as pd



# 编写用户年龄段划分函数（儿童<18，成人18-60，老人>60）
def user_age_group(age: int, child_max=18, elder_min=60) -> str:
    if age <= child_max:
        return '儿童'
    elif age > child_max and age < elder_min:
        return '青年'
    else:
        return '老年'

# 在模块中封装用户行为统计函数
def user_action_statistic(actions: list, start_num: int) -> tuple:
    try:
        return actions[start_num], start_num
    except IndexError:
        return None, start_num
    except TypeError:
        return None, None

# a = user_age_group(20)
# b = user_age_group(60)
user_actions = ["click", "view", "purchase"]
user_action_statistic(user_actions,2)


def analyze_user_profile(host: str):
    conn = get_connection(host)

    # 从Hive获取数据
    df = pd.DataFrame(
        execute_query(conn, "SELECT age, gender, action_count FROM users"),
        columns=["age", "gender", "actions"]
    )

    # 数据处理管道
    df['age_group'] = df['age'].apply(user_age_group)
    df['action_level'] = df['actions'].apply(
        lambda x: "high" if x > 10 else "low"
    )

    return df