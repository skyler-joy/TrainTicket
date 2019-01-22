
TYPE_LOGIN_NORMAL_WAY = 0
TYPE_LOGIN_OTHER_WAY = 1


class TourFlag(object):
    SINGLE = 'dc'
    GO_BACK = 'wc'


class SeatName(object):
    BUSINESS_SEAT = '商务座'
    SPECIAL_SEAT = '特等座'
    FIRST_CLASS_SEAT = '一等座'
    SECOND_CLASS_SEAT = '二等座'
    ADVANCED_SOFT_SLEEP = '高级软卧'
    SOFT_SLEEP = '软卧'
    HARD_SLEEP = '硬卧'
    SOFT_SEAT = '软座'
    HARD_SEAT = '硬座'
    NO_SEAT = '无座'


# seatType:商务座(9),特等座(P),一等座(M),二等座(O),高级软卧(6),软卧(4),硬卧(3),软座(2),硬座(1),无座(1)
SEAT_TYPE = {
    SeatName.BUSINESS_SEAT: '9',
    SeatName.SPECIAL_SEAT: 'P',
    SeatName.FIRST_CLASS_SEAT: 'M',
    SeatName.SECOND_CLASS_SEAT: 'O',
    SeatName.ADVANCED_SOFT_SLEEP: '6',
    SeatName.SOFT_SLEEP: '4',
    SeatName.HARD_SLEEP: '3',
    SeatName.SOFT_SEAT: '2',
    SeatName.HARD_SEAT: '1',
    SeatName.NO_SEAT: '1',
}

PASSENGER_TYPE_ADULT = "ADULT"
PASSENGER_TYPE_STUDENT = "0X00"
PASSENGER_TYPE_CHILD = ''
PASSENGER_TYPE_CRIPPLE_ARMY = ''
PASSENGER_TYPE_ADULT_CODE = '1'
PASSENGER_TYPE_CHILD_CODE = '2'
PASSENGER_TYPE_STUDENT_CODE = '3'
PASSENGER_TYPE_CRIPPLE_ARMY_CODE = '4'
# 成人票:1,儿童票:2,学生票:3,残军票:4
PASSENGER_TICKET_TYPE_CODES = {
    '成人票': PASSENGER_TYPE_ADULT_CODE,
    '儿童票': PASSENGER_TYPE_CHILD_CODE,
    '学生票': PASSENGER_TYPE_STUDENT_CODE,
    '残军票': PASSENGER_TYPE_CRIPPLE_ARMY_CODE,
}
PASSENGER_TICKET_TYPE_CODE_TO_DESC = {
    PASSENGER_TYPE_ADULT_CODE: PASSENGER_TYPE_ADULT,
    PASSENGER_TYPE_STUDENT_CODE: PASSENGER_TYPE_STUDENT,
    PASSENGER_TYPE_CHILD_CODE: PASSENGER_TYPE_CHILD,
    PASSENGER_TYPE_CRIPPLE_ARMY_CODE: PASSENGER_TYPE_CRIPPLE_ARMY,
}
