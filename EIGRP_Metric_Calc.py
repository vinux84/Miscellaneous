

def eigrp_metric(least_bw, cumu_delay):
    metric = ((10**7//least_bw) + cumu_delay) * 256
    return metric

def full_metric(bw_one, bw_two, delay_one, delay_two):
    cumu_delay = delay_one + delay_two
    if bw_one < bw_two:
        metric = ((10 ** 7 // bw_one) + cumu_delay) * 256
        return metric
    else:
        metric = ((10 ** 7 // bw_two) + cumu_delay) * 256
        return metric

def more_metric(bw_one, bw_two, delay_one, delay_two):
    # need formula to cal mb to kbs, then to turn microseconds into tens-of-microseconds for delay
    mb_kb_one = bw_one**4
    mb_kb_two = bw_two**4
    ten_micro_sec_one = delay_one // 10
    ten_micro_sec_two = delay_two // 10
    cumu_delay = ten_micro_sec_one + ten_micro_sec_two
    if bw_one < bw_two:
        metric = ((10 ** 7 // mb_kb_one) + cumu_delay) * 256
        return metric
    else:
        metric = ((10 ** 7 // mb_kb_two) + cumu_delay) * 256
        return metric
