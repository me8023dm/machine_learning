
# 编写用户年龄段划分函数（儿童<18，成人18-60，老人>60）
def user_age_group(age: int, child_max=18, elder_min=60) -> str:
    if age <= child_max:
        return '儿童'
    elif age > child_max and age < elder_min:
        return '青年'
    else:
        return '老年'
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