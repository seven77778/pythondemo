from wechat.wechatfriends import friends_stat

for sex, count in friends_stat["sex"].iteritems():
    # 1代表MALE, 2代表FEMALE
    if sex == 1:
        print ( "MALE %d" % count)
    elif sex == 2:
        print ("FEMALE %d" % count)