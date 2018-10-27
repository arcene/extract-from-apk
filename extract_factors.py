#!/usr/bin/env python

import sys
import os
from apk_parse import apk
from collections import OrderedDict
from permissions import full_permissions, suspicious_permissions
from get_permission_info import get_permission_info
from get_api_info import get_api_info

# paths
#apk_path = './data/train_data/0-normal'
#dex_path = './data/train_data/dex_0-normal'
#out_path = './data/train_data/out_normal'

apk_path = './data/train_data/1-malware'
dex_path = './data/train_data/dex_1-malware'
out_path = './data/train_data/out_malware'

# constants
DELIMITER = ','

out_with_full_permissions = os.path.join(out_path, 'with_full_perm.csv')
out_with_suspicious_permissions = os.path.join(out_path, 'with_suspicious_perm.csv')

ff = open(out_with_full_permissions, 'w')
sf = open(out_with_suspicious_permissions, 'w')

idx = 0

for filename in os.listdir(apk_path):
    apk_abs_path = os.path.join(apk_path, filename)
    dex_abs_path = os.path.join(dex_path, filename+'.dex')

    if not os.path.exists(dex_abs_path):
        continue

    (full_perm_list, suspicious_perm_list) = get_permission_info(apk_abs_path)
    if (full_perm_list is None or suspicious_perm_list is None):
        continue

    api_list = get_api_info(dex_abs_path)

    full = str(idx) + DELIMITER + filename + DELIMITER + str(full_perm_list) + \
        DELIMITER + str(api_list) + '\n'
    suspicious = str(idx) + DELIMITER + filename + DELIMITER + str(suspicious_perm_list) + \
        DELIMITER + str(api_list) + '\n'

    ff.write(full)
    sf.write(suspicious)

    idx = idx + 1

ff.close()
sf.close()
