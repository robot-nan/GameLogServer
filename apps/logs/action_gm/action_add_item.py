# -*- coding:utf-8 -*-
"""
    添加物品
"""
from apps.logs.action_gm import action_base_gm
from apps.game_manager import game_manage_define


def log(manager, server_id, user_id, item_tid, num):
    """
        输出日志
    """
    action = game_manage_define.GM_ACTION_ADD_ITEM

    log_lst = action_base_gm.log_base(manager)

    log_lst.append(str(action))
    log_lst.append(str(server_id))
    log_lst.append(str(user_id))
    log_lst.append(str(item_tid))
    log_lst.append(str(num))

    log_str = '$$'.join(log_lst)
    return log_str


def parse(log_part_lst):
    """
        解析
    """
    result = dict()
    result['action'] = int(log_part_lst[0])
    result['server_id'] = log_part_lst[1]
    result['user_id'] = log_part_lst[2]
    result['item_id'] = log_part_lst[3]
    result['num'] = log_part_lst[4]

    return result