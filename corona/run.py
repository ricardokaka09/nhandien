import json
from module import CoronaTracker

ct = CoronaTracker()
ct.parse()
def world():
    w = ct.all_statistic
    res= ("Tong so    : " + str(w['Tong so']) + "<br>"+ 
          "Dang nhiem : " + str(w['Dang nhiem']) + "<br>" + 
          "Khoi benh  : "  + str(w['Khoi benh']) + "<br>" +
          "Tu vong    : "  + str(w['Tu vong'])
        )
    print(res)
    return res
def Vietnam():
    vn = ct.country_statistic['Vietnam']
    res= ("Tong so    : " + str(vn['Tong so']) + "<br>"+ 
          "Dang nhiem : " + str(vn['Dang nhiem']) + "<br>" + 
          "Khoi benh  : "  + str(vn['Khoi benh']) + "<br>" +
          "Tu vong    : "  + str(vn['Tu vong'])
        )
    print(res)
    return res 
world()
Vietnam()
# if __name__ == '__main__':
#     ct = CoronaTracker()
#     ct.parse()

#     print(json.dumps(
#         ct.all_statistic,
#         indent=4,
#     ))
#     Vietnam = ct.country_statistic['Vietnam']
#     res= ("Tong so : " + str(Vietnam['Tong so']) + "\n"+ 
#           "Dang nhiem : " + str(Vietnam['Dang nhiem']) + "\n" + 
#           "Khoi benh : "  + str(Vietnam['Khoi benh']) + "\n" +
#           "Tu vong : "  + str(Vietnam['Tu vong'])
#          )
#     print(res)
#     thongtin = json.dumps(
#         ct.country_statistic,
#         indent=4,
#     )
    # print(thongtin)