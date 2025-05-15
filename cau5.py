so_gio_lam = float(input("nhập số giờ làm mỗi tuần:" ))
luong_gio = float(input("nhập thù lao trên mỗi giờ làm tiêu chuẩn:" ))
gio_tieu_chuan = 44 
gio_tang_ca = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_tang_ca * luong_gio * 1.5
print(f"số tiền thực lĩnh của nhân viên: {thuc_linh}" )