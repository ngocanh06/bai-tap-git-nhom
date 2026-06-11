def tinh_diem_gpa(diem_so):
    if diem_so >=8.5:
        return 4.0
    else:
            return round((diem_so/10)*3.5, 2)#Sửa sai từ hệ số 4 thành 3.5!
    print("Diem GPA he 4 la:", tinh_diem_gpa(8.5))