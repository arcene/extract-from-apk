import os
from collections import OrderedDict
from apis import suspicious_api_dict
from parse_dex import *

def get_api_info(abs_file_path):
    all_list = []

    temp_dict = OrderedDict()
    for i in suspicious_api_dict:
        name = i
        temp_list = [0 for i in range(len(suspicious_api_dict[i]))]
        temp_dict[name] = temp_list

    try:
        fp = open(abs_file_path, 'rb')
    except IOError as e:
        all_list = [-1 for i in range(78)]
    except:
        print abs_file_path

    mm = fp.read()
    fp.close()
    hdr = header(mm)

    string_ids = string_id_list(mm, hdr)
    type_ids = type_id_list(mm, hdr)
    method_ids = method_id_list(mm, hdr)

    list_api = []
    for i in range(len(method_ids)):
        (class_idx, proto_idx, name_idx) = method_ids[i]
        class_str = string_ids[type_ids[class_idx]]
        name_str = string_ids[name_idx]
        list_api.append([class_str[1:], name_str])
        #print '[%s.%s()]' % (class_str[1:], name_str)
        for i in suspicious_api_dict:
            if class_str[1:].lower().find(i) != -1:
                if 'NONE' in suspicious_api_dict[i]:
                    temp_dict[i][suspicious_api_dict[i].index('NONE')] = 1
                if name_str.lower() in suspicious_api_dict[i]:
                    temp_dict[i][suspicious_api_dict[i].index(name_str.lower())] = 1

    for i in temp_dict:
        all_list = all_list + temp_dict[i]

    return all_list

