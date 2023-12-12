danhSachSinhVien = [
    {
        "maSV": 1,
        "tenSV": "Nguyen Van A",
        "diemToan": 9.5,
        "diemVan": 8.5,
        "diemHoa": 7,
    },
    {
        "maSV": 2,
        "tenSV": "Nguyen Van B",
        "diemToan": 5.5,
        "diemVan": 6.75,
        "diemHoa": 4,
    },
    {
        "maSV": 3,
        "tenSV": "Nguyen Van C",
        "diemToan": 4.5,
        "diemVan": 2.5,
        "diemHoa": 9,
    },
    {
        "maSV": 4,
        "tenSV": "Nguyen Van D",
        "diemToan": 9.5,
        "diemVan": 10,
        "diemHoa": 7.75,
    },
    {
        "maSV": 5,
        "tenSV": "Nguyen Van E",
        "diemToan": 6,
        "diemVan": 8.5,
        "diemHoa": 9,
    },
]

danhSachTrenTB = []
danhSachHoaDuoi5 = []

for sv in danhSachSinhVien:
    diemTB = round((sv["diemToan"] + sv["diemVan"] + sv["diemHoa"]) / 3, 2)
    if diemTB > 5.0:
        danhSachTrenTB.append(sv)
    
    if sv["diemHoa"] < 5.0:
        danhSachHoaDuoi5.append(sv)
    
#* SV có điểm trung bình dưới 5
print("1. Thông tin sinh viên có điểm trung bình lớn hơn 5: ")
print(danhSachTrenTB)


#* SV có điểm trung bình dưới 5
print("2. Thông sinh viên có điểm hoá dưới 5: ")
print(danhSachHoaDuoi5)