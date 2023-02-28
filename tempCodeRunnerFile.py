    appoint_time = input("请输入时间")
    get_date = appoint_time.split('-')
    begin_time =  get_date[0:4]
    begin_time[0] += '年'
    begin_time[1] += '月'
    begin_time[2] += '日'
    print(begin_time)