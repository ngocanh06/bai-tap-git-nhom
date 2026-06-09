def tinh_thue_thu_nhap(thu_nhap):
    # Dev A áp dụng giảm trừ 4 triệu và thuế 5%
    thu_nhap_chiu_thue = thu_nhap - 4000000
    return max(0, thu_nhap_chiu_thue * 0.05)
