import os
import apk_parse
from apk_parse import apk
from permissions import full_permissions, suspicious_permissions

def get_permission_info(abs_file_path):

    full_list = [0]*len(full_permissions)
    suspicious_list = [0]*len(suspicious_permissions)

    try:
        apkf = apk.APK(abs_file_path)
        perm = apkf.get_permissions()
    except:
        return (None, None)

    for p in perm:
        p = p.split('.')[-1]
        if p in full_permissions:
            full_list[full_permissions.index(p)] = 1
        if p in suspicious_permissions:
            suspicious_list[suspicious_permissions.index(p)] = 1

    return (full_list, suspicious_list)
