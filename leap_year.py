def final_days(month, year):
    final_day_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month != 2:
        return final_day_of_month[month-1]
    else:
        fd = final_day_of_month[month-1]
        if year%4 == 0:
            #윤년
            fd += 1
            if year%100 == 0:
                #평년
                fd -= 1
                if year%400 ==0:
                    #윤년
                    fd += 1
        return fd
