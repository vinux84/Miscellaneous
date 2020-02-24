import os


def get_storage(file_path_o, file_path_t):
    storage = os.statvfs(file_path_o)
    storage_total = (storage.f_blocks * storage.f_frsize)
    storage_used = (storage.f_blocks - storage.f_bfree) * storage.f_frsize
    sys = os.statvfs(file_path_t)
    sys_total = (sys.f_blocks * sys.f_frsize)
    sys_used = (sys.f_blocks - sys.f_bfree) * sys.f_frsize
    full_total = storage_total + sys_total
    full_used = storage_used + sys_used
    print(f"{full_total} / {full_used}")





get_storage("/media", "/")

# This class needs 2 attributes.

class HardDrive:

    def __init__(self, total, used):
        self.total = total
        self.used = used






