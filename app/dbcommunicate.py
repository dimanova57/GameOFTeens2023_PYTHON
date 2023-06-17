from database import User, session


def add_point_for(tariff_name, user_id, points):
    user = session.query(User).where(User.id == user_id).first()
    if tariff_name == 'free':
        user.free_life += points
    elif tariff_name == 'smart':
        user.smart_life += points
    elif tariff_name == 'simple':
        user.simple_life += points
    elif tariff_name == 'platinum':
        user.platinum_life += points
    elif tariff_name == 'school':
        user.school_life += points
    elif tariff_name == 'gadjet':
        user.gadjet_life += points
    elif tariff_name == 'family':
        user.family_life += points
    session.commit()


def add_user(user_id, user_name):
    user = User(user_name, user_id)
    session.add(user)
    session.commit()


def delete_all_points_by(user_id):
    user = session.query(User).where(User.id == user_id).first()
    user.free_life = 0
    user.smart_life = 0
    user.simple_life = 0
    user.platinum_life = 0
    user.school_life = 0
    user.gadjet_life = 0
    user.family_life = 0
    session.commit()


def check_user_in_bd_by(user_id):
    user = session.query(User).where(User.id == user_id).first()
    if user:
        return True
    return False


def sorting_dict(tariff_dict: dict):
    top_dict = dict()
    max_value = 0
    cof = 0
    max_value_name = str()
    for i in range(3):
        for k, v in tariff_dict.items():
            if v > max_value:
                max_value = v
                max_value_name = k
        top_dict[max_value_name] = max_value
        cof += max_value
        tariff_dict[max_value_name] = -10
        max_value = -10
    cof = 100/cof
    print(top_dict)
    for k, v in top_dict.items():
        print(f'{k} => {v*cof}')
    return top_dict, cof


def show_all_res(user_id):
    user = session.query(User).where(User.id == user_id).first()
    list_of_res = {'/free': user.free_life, '/smart': user.smart_life, '/simple': user.simple_life,
                   '/platinum': user.platinum_life, '/school': user.school_life,
                   '/gadjet': user.gadjet_life, '/family': user.family_life}
    print(list_of_res)
    pretty_str = f''
    top_dict = sorting_dict(list_of_res)
    for k, value in top_dict[0].items():
        pretty_str += f'\n{k} => {round(value*top_dict[1])}%'
    return pretty_str


