print("การคำนวณพลังงานที่เราใช้ในการดำรงชีวิตในช่วงเวลา")
print("Select Gender")
print("1.Male")
print("2.Female")
Choose = int(input("Enter Gender : "))
if Choose == 1 :
    Weight = int(input("Enter your weight : "))
    Height = int(input("Enter your height : "))
    Age = int(input("Enter your age : "))
    print("BMR = ","5+(10*Weight)+(6.25*Height)-(5*Age)")
    print("BMR = ","5+(10*",Weight,")+(6.25*",Height,")-(5*",Age,")")
    cal_bmr = 5+(10*Weight)+(6.25*Height)-(5*Age)
    print("BMR :",cal_bmr)
    print("<---Choose your exercise--->")
    print("1. การออกกำลังกายน้อยมาก หรือไม่ออกกำลังกายเลย")
    print("2. การออกกำลังกายน้อย ออกกำลังกาย 1-3 วันต่อสัปดาห์")
    print("3. การออกกำลังกายปานกลาง ออกกำลังกาย 3-5 วันต่อสัปดาห์")
    print("4. การออกกำลังกายหนัก ออกกำลังกาย 6-7 วันต่อสัปดาห์")
    print("5. การออกกำลังกายออกกำลังกายหนักมากหรือเป็นนักกีฬา")
    Choose_ex = int(input("Enter your exercise :"))
    if Choose_ex == 1:
        cal_tdee = 1.2*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 2:
        cal_tdee = 1.375*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 3:
        cal_tdee = 1.55*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 4:
        cal_tdee = 1.725*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 5:
        cal_tdee = 1.9*cal_bmr
        print("TDEE :",cal_tdee)
    print("ถ้าต้องการฟิตหุ่น(ลดไขมัน)เลือก1")
    print("ถ้าต้องการเพิ่มน้ำหนัก(กล้ามเนื้อ)เลือก2")
    Choose_2 = int(input("Enter your need :"))
    if Choose_2 == 1:
        x = cal_tdee - 500
        print("Your finale TDEE :",x)
    elif Choose_2 == 2:
        x = cal_tdee + 500
        print("Your finale TDEE :",x)
if Choose == 2 :
    Weight = int(input("Enter your weight : "))
    Height = int(input("Enter your height : "))
    Age = int(input("Enter your age : "))
    print("BMR = ","161-(10*Weight)+(6.25*Height)-(5*Age)")
    print("BMR = ","161-(10*",Weight,")+(6.25*",Height,")-(5*",Age,")")
    cal_bmr = 161-(10*Weight)+(6.25*Height)-(5*Age)
    print("BMR :",cal_bmr)
    print("<---Choose your exercise--->")
    print("1. การออกกำลังกายน้อยมาก หรือไม่ออกกำลังกายเลย")
    print("2. การออกกำลังกายน้อย ออกกำลังกาย 1-3 วันต่อสัปดาห์")
    print("3. การออกกำลังกายปานกลาง ออกกำลังกาย 3-5 วันต่อสัปดาห์")
    print("4. การออกกำลังกายหนัก ออกกำลังกาย 6-7 วันต่อสัปดาห์")
    print("5. การออกกำลังกายออกกำลังกายหนักมากหรือเป็นนักกีฬา")
    Choose_ex = int(input("Enter your exercise :"))
    if Choose_ex == 1:
        cal_tdee = 1.2*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 2:
        cal_tdee = 1.375*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 3:
        cal_tdee = 1.55*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 4:
        cal_tdee = 1.725*cal_bmr
        print("TDEE :",cal_tdee)
    elif Choose_ex == 5:
        cal_tdee = 1.9*cal_bmr
        print("TDEE :",cal_tdee)
    print("ถ้าต้องการฟิตหุ่น(ลดไขมัน)เลือก1")
    print("ถ้าต้องการเพิ่มน้ำหนัก(กล้ามเนื้อ)เลือก2")
    Choose_2 = int(input("Enter your need :"))
    if Choose_2 == 1:
        x = cal_tdee - 500
        print("Your finale TDEE :",x)
    elif Choose_2 == 2:
        x = cal_tdee + 500
        print("Your finale TDEE :",x)
print("<---Thanks you--->")