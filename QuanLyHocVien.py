from datetime import datetime

# Đối tượng Khoá Học
class KhoaHoc: 
    def __init__(self, maKhoaHoc: str, tenKhoaHoc: str, hinhThuc: str, hocPhi: float):
        #* Constructor
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    #? Method: đăng kí khoá học
    def thongTinKhoaHoc(self) -> str:
        return "Mã khoá học: {}, Tên khoá học: {}, Hình thức: {}, Học phí: {}".format(self.maKhoaHoc, self.tenKhoaHoc, self.hinhThuc, self.hocPhi)

# Đối tượng Sinh Viên
class HocVien:
    #* Constructor
    def __init__(self, maHV: str, tenHV: str, ngaySinh: datetime, khoaHoc: list):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = khoaHoc
    
    #? Method: đăng kí khoá học
    def dangKiKhoaHoc(self, khoaHoc: KhoaHoc):
        self.khoaHoc.append(khoaHoc)
    
    #? Method: hiển thị tất cả khoá học
    def hienThiKhoaHoc(self) -> str:
        result = "{\n"
        for kh in self.khoaHoc:
            result += i + kh.thongTinKhoaHoc() + "\n"
        
        result += "}"
        return result

    
#TODO: MAIN PROGRAM

#* Tạo khoá học
khoaHoc1 = KhoaHoc("a1", "ReactJS", "Offline", 15.0)
khoaHoc2 = KhoaHoc("a2", "NodeJS", "Online", 7.5)
khoaHoc3 = KhoaHoc("b1", "React Native", "Online", 11.25)
khoaHoc4 = KhoaHoc("b2", "Data Analyst", "Hybrid", 12.1)
khoaHoc5 = KhoaHoc("c1", "TypeScript", "Hybrid", 5.2)

# print("Khoá 1", khoaHoc1.thongTinKhoaHoc())
# print("Khoá 3", khoaHoc3.thongTinKhoaHoc())

#* Tạo học viên
hocVien1 = HocVien("hv1", "Nguyen Van A", datetime(2002, 11, 23), [])
hocVien2 = HocVien("hv2", "Tran Van B", datetime(2004, 5, 18), [khoaHoc1, khoaHoc5])

#print("Học Viên 1: ", hocVien1.hienThiKhoaHoc())
# print("Học Viên 2: ", hocVien2.hienThiKhoaHoc())

#* Đăng kí khoá học cho học viên 1
hocVien1.dangKiKhoaHoc(khoaHoc2)
hocVien1.dangKiKhoaHoc(khoaHoc4)
hocVien1.dangKiKhoaHoc(khoaHoc5)
print("Học Viên 1: ", hocVien1.hienThiKhoaHoc())
