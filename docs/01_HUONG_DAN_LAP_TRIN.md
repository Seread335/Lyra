# HƯỚNG DẪN LẬP TRÌNH LYRA NNLT v2.3.22.1

## Mục Đích

Tài liệu này cung cấp hướng dẫn chi tiết về cách sử dụng Lyra NNLT - một trình biên dịch và thực thi mã lệnh được thiết kế cho hiệu năng cao và bảo mật doanh nghiệp.

---

## 1. CÀI ĐẶT VÀ THIẾT LẬP

### 1.1 Yêu Cầu Hệ Thống

- Hệ điều hành: Linux, macOS, Windows
- Bộ nhớ tối thiểu: 10 MB
- Không cần thư viện bên ngoài (Pure Lyra)

### 1.2 Cài Đặt Trên Linux/macOS

```bash
# Bước 1: Tải mã nguồn
git clone https://github.com/your-org/lyra-nnlt.git
cd lyra-nnlt

# Bước 2: Chạy script cài đặt
chmod +x install_lyra.sh
./install_lyra.sh

# Bước 3: Kiểm tra cài đặt
lyra --version
```

### 1.3 Cài Đặt Trên Windows

```powershell
# Bước 1: Tải mã nguồn
git clone https://github.com/your-org/lyra-nnlt.git
cd lyra-nnlt

# Bước 2: Chạy script cài đặt
.\install_lyra.bat

# Bước 3: Kiểm tra cài đặt
lyra --version
```

### 1.4 Xác Minh Cài Đặt

```lyra
// Tệp: test_install.lyra
print("Lyra NNLT đã được cài đặt thành công!")
print("Phiên bản: 2.3.22.1")
```

Chạy:
```bash
lyra test_install.lyra
```

Kết quả dự kiến:
```
Lyra NNLT đã được cài đặt thành công!
Phiên bản: 2.3.22.1
```

---

## 2. CÚ PHÁP CƠ BẢN

### 2.1 Biến và Kiểu Dữ Liệu

Lyra hỗ trợ các kiểu dữ liệu cơ bản:

```lyra
// Khai báo biến
var so_nguyen: i32 = 42
var so_thuc: f64 = 3.14
var xau_ky_tu: str = "Hello Lyra"
var logic: bool = true
var mang_so: [i32] = [1, 2, 3, 4, 5]

// In ra giá trị
print("Số nguyên: " + tostring(so_nguyen))
print("Xâu ký tự: " + xau_ky_tu)
print("Giá trị logic: " + tostring(logic))
```

Giải thích:
- `i32`: Số nguyên 32 bit (từ -2,147,483,648 đến 2,147,483,647)
- `f64`: Số thực 64 bit (số có dấu phẩy động)
- `str`: Xâu ký tự (chuỗi văn bản)
- `bool`: Giá trị logic (true/false)
- `[i32]`: Mảng chứa các số nguyên

### 2.2 Hàm và Thủ Tục

Hàm trong Lyra khai báo bằng từ khóa `proc`:

```lyra
// Hàm tính tổng của hai số
proc cong(a: i32, b: i32) -> i32 {
    return a + b
}

// Hàm không trả về giá trị
proc in_thong_bao(thong_bao: str) {
    print("Thông báo: " + thong_bao)
}

// Sử dụng hàm
var ket_qua = cong(10, 20)
print("Kết quả: " + tostring(ket_qua))  // Output: Kết quả: 30

in_thong_bao("Chương trình đang chạy")  // Output: Thông báo: Chương trình đang chạy
```

Giải thích:
- `proc`: Từ khóa khai báo hàm
- `(a: i32, b: i32)`: Tham số đầu vào (tên và kiểu)
- `-> i32`: Kiểu giá trị trả về (nếu không có, không cần viết)
- `return`: Từ khóa trả về giá trị

### 2.3 Cấu Trúc Điều Khiển

#### If - Else (Điều Kiện)

```lyra
var diem = 75

if diem >= 80 {
    print("Loại A")
}
else if diem >= 70 {
    print("Loại B")
}
else if diem >= 60 {
    print("Loại C")
}
else {
    print("Loại F")
}
// Output: Loại B
```

Giải thích:
- `if`: Kiểm tra điều kiện đầu tiên
- `else if`: Kiểm tra điều kiện thay thế
- `else`: Thực thi nếu tất cả điều kiện trên đều sai

#### While (Vòng Lặp Có Điều Kiện)

```lyra
var i = 0

while i < 5 {
    print("Giá trị: " + tostring(i))
    i = i + 1
}
// Output:
// Giá trị: 0
// Giá trị: 1
// Giá trị: 2
// Giá trị: 3
// Giá trị: 4
```

Giải thích:
- Vòng lặp tiếp tục chừng nào điều kiện `i < 5` còn đúng
- Mỗi lần lặp, `i` tăng thêm 1

#### Break (Thoát Vòng Lặp)

```lyra
var j = 0

while j < 10 {
    if j == 5 {
        break  // Thoát vòng lặp khi j = 5
    }
    print(tostring(j))
    j = j + 1
}
// Output: 0, 1, 2, 3, 4
```

---

## 3. LÀM VIỆC VỚI MẢNG

### 3.1 Tạo và Khởi Tạo Mảng

```lyra
// Khai báo mảng trống
var mang_rong: [i32]

// Khai báo mảng với giá trị ban đầu
var mang_so = [10, 20, 30, 40, 50]

// Lấy độ dài mảng
var do_dai = length(mang_so)
print("Độ dài mảng: " + tostring(do_dai))  // Output: Độ dài mảng: 5
```

Giải thích:
- Mảng được chỉ định kiểu khi khai báo
- `length()`: Hàm trả về số phần tử trong mảng

### 3.2 Truy Cập Phần Tử

```lyra
var con_so = [5, 10, 15, 20, 25]

// Lấy phần tử tại vị trí 0
var phan_tu_dau = con_so[0]
print("Phần tử đầu: " + tostring(phan_tu_dau))  // Output: 5

// Lấy phần tử tại vị trí cuối
var phan_tu_cuoi = con_so[4]
print("Phần tử cuối: " + tostring(phan_tu_cuoi))  // Output: 25

// Gán giá trị mới
con_so[2] = 99
print(tostring(con_so[2]))  // Output: 99
```

Giải thích:
- Chỉ số bắt đầu từ 0 (phần tử đầu tiên ở vị trí 0)
- Phần tử cuối cùng ở vị trí `length(mang) - 1`

### 3.3 Thêm và Xóa Phần Tử

```lyra
var danh_sach: [str]

// Thêm phần tử
insert(danh_sach, "Việt Nam")
insert(danh_sach, "Thái Lan")
insert(danh_sach, "Campuchia")

// In danh sách
var chi_so = 0
while chi_so < length(danh_sach) {
    print("Quốc gia: " + danh_sach[chi_so])
    chi_so = chi_so + 1
}
// Output:
// Quốc gia: Việt Nam
// Quốc gia: Thái Lan
// Quốc gia: Campuchia
```

Giải thích:
- `insert()`: Thêm phần tử vào cuối mảng

---

## 4. LÀM VIỆC VỚI XÂU KÝ TỰ

### 4.1 Các Hàm Xâu

```lyra
var van_ban = "Lyra Programming Language"

// Độ dài xâu
var do_dai_van_ban = length(van_ban)
print("Độ dài: " + tostring(do_dai_van_ban))  // Output: 25

// Tách xâu (lấy ký tự từ vị trí 0, độ dài 4)
var tu_dau = substr(van_ban, 0, 4)
print("Từ đầu: " + tu_dau)  // Output: Lyra

// Nối xâu
var xau_1 = "Hello "
var xau_2 = "World"
var xau_full = xau_1 + xau_2
print(xau_full)  // Output: Hello World
```

Giải thích:
- `length()`: Trả về số ký tự trong xâu
- `substr(xau, vi_tri, do_dai)`: Tách phần xâu từ vị trí, với độ dài chỉ định
- Nối xâu bằng toán tử `+`

### 4.2 Chuyển Đổi Kiểu

```lyra
// Chuyển số thành xâu
var so = 2024
var xau_so = tostring(so)
print("Năm: " + xau_so)  // Output: Năm: 2024

// Chuyển xâu thành số (nếu có thể)
var xau_number = "42"
// Lyra không có hàm toint trực tiếp, cần xử lý thủ công
```

Giải thích:
- `tostring()`: Chuyển số thành xâu để nối với xâu khác

---

## 5. PHÉP TOÁN VÀ BIỂU THỨC

### 5.1 Phép Toán Số Học

```lyra
var a = 15
var b = 4

// Cộng
var cong = a + b
print("Cộng: " + tostring(cong))  // Output: 19

// Trừ
var tru = a - b
print("Trừ: " + tostring(tru))  // Output: 11

// Nhân
var nhan = a * b
print("Nhân: " + tostring(nhan))  // Output: 60

// Chia (lấy phần nguyên)
var chia = a / b
print("Chia: " + tostring(chia))  // Output: 3

// Chia lấy dư
var du = a % b
print("Dư: " + tostring(du))  // Output: 3
```

Giải thích:
- `/`: Phép chia lấy phần nguyên (15 / 4 = 3, không phải 3.75)
- `%`: Phép chia lấy dư (15 % 4 = 3, vì 15 = 4*3 + 3)

### 5.2 Phép So Sánh

```lyra
var x = 10
var y = 20

// Bằng
if x == y {
    print("Bằng")
}
else {
    print("Không bằng")  // Output: Không bằng
}

// Không bằng
if x != y {
    print("Khác nhau")  // Output: Khác nhau
}

// Lớn hơn
if x < y {
    print("x nhỏ hơn y")  // Output: x nhỏ hơn y
}

// Lớn hơn hoặc bằng
if y >= 20 {
    print("y lớn hơn hoặc bằng 20")  // Output: y lớn hơn hoặc bằng 20
}
```

Giải thích:
- `==`: So sánh bằng
- `!=`: So sánh không bằng
- `<`, `>`: Nhỏ hơn, lớn hơn
- `<=`, `>=`: Nhỏ hơn hoặc bằng, lớn hơn hoặc bằng

### 5.3 Phép Toán Logic

```lyra
var dieu_kien_1 = true
var dieu_kien_2 = false

// AND (cả hai phải đúng)
if dieu_kien_1 && dieu_kien_2 {
    print("Cả hai đúng")
}
else {
    print("Không phải cả hai đều đúng")  // Output
}

// OR (ít nhất một cái đúng)
if dieu_kien_1 || dieu_kien_2 {
    print("Có ít nhất một cái đúng")  // Output
}

// NOT (phủ định)
if !dieu_kien_2 {
    print("dieu_kien_2 là sai")  // Output
}
```

Giải thích:
- `&&`: AND logic (phải cả hai đều đúng)
- `||`: OR logic (chỉ cần một cái đúng)
- `!`: NOT logic (phủ định giá trị)

---

## 6. VÍ DỤ THỰC TẾ

### 6.1 Tính Tổng Các Số Từ 1 Đến N

```lyra
proc tinh_tong(n: i32) -> i32 {
    var tong = 0
    var i = 1
    
    while i <= n {
        tong = tong + i
        i = i + 1
    }
    
    return tong
}

// Sử dụng
var ket_qua = tinh_tong(10)
print("Tổng từ 1 đến 10: " + tostring(ket_qua))
// Output: Tổng từ 1 đến 10: 55
```

Giải thích:
- Hàm `tinh_tong()` nhận một số `n` làm tham số
- Vòng lặp while cộng dồn giá trị từ 1 đến n
- Công thức: 1 + 2 + 3 + ... + n = n*(n+1)/2, với n=10 là 55

### 6.2 Tìm Số Chẵn Trong Mảng

```lyra
proc tim_so_chan(danh_sach: [i32]) -> [i32] {
    var ket_qua: [i32]
    var i = 0
    
    while i < length(danh_sach) {
        if danh_sach[i] % 2 == 0 {  // Kiểm tra chia hết cho 2
            insert(ket_qua, danh_sach[i])
        }
        i = i + 1
    }
    
    return ket_qua
}

// Sử dụng
var mang_goc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var so_chan = tim_so_chan(mang_goc)

var j = 0
while j < length(so_chan) {
    print("Số chẵn: " + tostring(so_chan[j]))
    j = j + 1
}
// Output:
// Số chẵn: 2
// Số chẵn: 4
// Số chẵn: 6
// Số chẵn: 8
// Số chẵn: 10
```

Giải thích:
- Kiểm tra `danh_sach[i] % 2 == 0`: Nếu dư 0 khi chia cho 2, là số chẵn
- Hàm trả về mảng chứa tất cả số chẵn từ mảng đầu vào

### 6.3 Tính Giai Thừa

```lyra
proc giai_thua(n: i32) -> i32 {
    if n == 0 || n == 1 {
        return 1
    }
    
    var ket_qua = 1
    var i = 2
    
    while i <= n {
        ket_qua = ket_qua * i
        i = i + 1
    }
    
    return ket_qua
}

// Sử dụng
var n = 5
var gt = giai_thua(n)
print("Giai thừa của " + tostring(n) + " là: " + tostring(gt))
// Output: Giai thừa của 5 là: 120
```

Giải thích:
- Giai thừa: n! = 1 * 2 * 3 * ... * n
- 5! = 1 * 2 * 3 * 4 * 5 = 120
- Trường hợp đặc biệt: 0! = 1, 1! = 1

### 6.4 Kiểm Tra Số Nguyên Tố

```lyra
proc la_so_nguyen_to(n: i32) -> bool {
    if n < 2 {
        return false
    }
    
    var i = 2
    while i * i <= n {
        if n % i == 0 {
            return false  // Có ước số, không phải số nguyên tố
        }
        i = i + 1
    }
    
    return true  // Không có ước số, là số nguyên tố
}

// Sử dụng
var danh_sach_kiem_tra = [2, 3, 4, 5, 10, 11, 13]
var k = 0

while k < length(danh_sach_kiem_tra) {
    var so = danh_sach_kiem_tra[k]
    if la_so_nguyen_to(so) {
        print(tostring(so) + " là số nguyên tố")
    }
    else {
        print(tostring(so) + " không phải số nguyên tố")
    }
    k = k + 1
}
// Output:
// 2 là số nguyên tố
// 3 là số nguyên tố
// 4 không phải số nguyên tố
// 5 là số nguyên tố
// 10 không phải số nguyên tố
// 11 là số nguyên tố
// 13 là số nguyên tố
```

Giải thích:
- Số nguyên tố là số chỉ chia hết cho 1 và chính nó
- Chỉ cần kiểm tra đến căn bậc hai (i * i <= n)
- Nếu tìm được ước số, không phải số nguyên tố

---

## 7. LỖI PHỔ BIẾN VÀ CÁCH XỬ LÝ

### 7.1 Lỗi Chỉ Số Mảng

```lyra
var mang = [10, 20, 30]

// Lỗi: Vượt quá giới hạn
// print(mang[10])  // Lỗi! Mảng chỉ có 3 phần tử (chỉ số 0, 1, 2)

// Cách đúng: Kiểm tra trước
var chi_so = 1
if chi_so >= 0 && chi_so < length(mang) {
    print("Giá trị: " + tostring(mang[chi_so]))
}
```

Giải thích:
- Luôn kiểm tra `chi_so >= 0 && chi_so < length(mang)` trước khi truy cập
- Chỉ số hợp lệ: từ 0 đến length - 1

### 7.2 Lỗi Chia Cho Zero

```lyra
var a = 10
var b = 0

// Lỗi: Chia cho zero
// var ket_qua = a / b  // Lỗi!

// Cách đúng: Kiểm tra trước
if b != 0 {
    var ket_qua = a / b
    print("Kết quả: " + tostring(ket_qua))
}
else {
    print("Lỗi: Không thể chia cho zero")
}
```

Giải thích:
- Luôn kiểm tra số chia không bằng 0 trước khi thực hiện phép chia

### 7.3 Lỗi Vòng Lặp Vô Hạn

```lyra
// Lỗi: Vòng lặp vô hạn
// var x = 0
// while x < 5 {
//     print("Lặp")
//     // Quên tăng x, nên x luôn < 5
// }

// Cách đúng:
var x = 0
while x < 5 {
    print("Lặp " + tostring(x))
    x = x + 1  // Đảm bảo đạt được điều kiện dừng
}
```

Giải thích:
- Vòng lặp phải có cách thoát (đạt điều kiện dừng)
- Đảm bảo biến điều kiện thay đổi mỗi lần lặp

---

## 8. HÌNH ẢNH CẤP ĐỘ

### 8.1 Các Cấp Độ Tối Ưu Hóa

Lyra NNLT cung cấp ba cấp độ tối ưu hóa:

```lyra
// Cấp độ 0: Không tối ưu hóa (nhanh để biên dịch)
setOptimizationLevel(0)
print("Đã thiết lập cấp độ 0")

// Cấp độ 1: Tối ưu hóa cơ bản
setOptimizationLevel(1)
print("Đã thiết lập cấp độ 1 - Tối ưu hóa cơ bản")

// Cấp độ 2: Tối ưu hóa cao (chậm hơn để biên dịch, nhưng mã chạy nhanh hơn)
setOptimizationLevel(2)
print("Đã thiết lập cấp độ 2 - Tối ưu hóa cao")
```

Giải thích:
- Cấp độ 0: Phù hợp cho phát triển (biên dịch nhanh)
- Cấp độ 1: Cân bằng giữa tốc độ biên dịch và hiệu năng chạy
- Cấp độ 2: Tối ưu hóa tối đa cho hiệu năng sản xuất

---

## 9. CHẨN ĐOÁN VÀ DEBUGGING

### 9.1 In Giá Trị Để Gỡ Lỗi

```lyra
proc tinh_toan_phuc_tap(a: i32, b: i32) -> i32 {
    print("Giá trị đầu vào: a=" + tostring(a) + ", b=" + tostring(b))
    
    var tong = a + b
    print("Sau khi cộng: tong=" + tostring(tong))
    
    var tich = tong * 2
    print("Sau khi nhân: tich=" + tostring(tich))
    
    return tich
}

// Gọi hàm và theo dõi
var ket_qua = tinh_toan_phuc_tap(5, 3)
print("Kết quả cuối cùng: " + tostring(ket_qua))
// Output:
// Giá trị đầu vào: a=5, b=3
// Sau khi cộng: tong=8
// Sau khi nhân: tich=16
// Kết quả cuối cùng: 16
```

Giải thích:
- Sử dụng `print()` để in giá trị tại từng bước
- Giúp xác định vị trí lỗi xảy ra

### 9.2 Kiểm Tra Trạng Thái Hệ Thống

```lyra
// Khởi tạo hệ thống
initLyraOptimized()

// In trạng thái hệ thống
printSystemStatus()

// Chạy chẩn đoán
runSystemDiagnostics()
```

Giải thích:
- `initLyraOptimized()`: Khởi tạo tất cả các thành phần
- `printSystemStatus()`: Hiển thị trạng thái hệ thống
- `runSystemDiagnostics()`: Chạy kiểm tra chẩn đoán toàn bộ hệ thống

---

## 10. HIỆU NĂNG VÀ TỐI ƯU HÓA

### 10.1 Tránh Các Vòng Lặp Lồng Nhau Phức Tạp

```lyra
// Hiệu năng kém: O(n²) vòng lặp lồng
proc tim_cap_tong_nhanh_nhat_v1(mang: [i32], tong_mong_muon: i32) -> bool {
    var i = 0
    while i < length(mang) {
        var j = i + 1
        while j < length(mang) {
            if mang[i] + mang[j] == tong_mong_muon {
                return true
            }
            j = j + 1
        }
        i = i + 1
    }
    return false
}

// Hiệu năng tốt hơn: O(n) một vòng lặp
proc tim_cap_tong_nhanh_nhat_v2(mang: [i32], tong_mong_muon: i32) -> bool {
    // Phương pháp: Sử dụng hai con trỏ
    var trai = 0
    var phai = length(mang) - 1
    
    while trai < phai {
        var tong_hien_tai = mang[trai] + mang[phai]
        if tong_hien_tai == tong_mong_muon {
            return true
        }
        else if tong_hien_tai < tong_mong_muon {
            trai = trai + 1
        }
        else {
            phai = phai - 1
        }
    }
    return false
}
```

Giải thích:
- Phiên bản 1: O(n²) - rất chậm với dữ liệu lớn
- Phiên bản 2: O(n) - nhanh hơn nhiều
- Sử dụng thuật toán tối ưu (hai con trỏ) thay vì vòng lặp lồng

### 10.2 Sử Dụng Cấp Độ Tối Ưu Hóa

```lyra
// Ứng dụng cần hiệu năng cao
proc ung_dung_thuc_te() {
    setOptimizationLevel(2)  // Bật tối ưu hóa cao
    
    // Khởi tạo hệ thống
    initLyraOptimized()
    
    // Chạy chương trình
    // ...
}
```

---

## KẾT LUẬN

Tài liệu này cung cấp các kiến thức cơ bản để bắt đầu lập trình với Lyra NNLT. Để tìm hiểu thêm chi tiết:

- Xem file `02_TAI_LIEU_THAM_KHAO.md` cho API đầy đủ
- Xem file `03_VI_DU_NANG_CAO.md` cho các ví dụ phức tạp
- Xem file `04_XU_LY_LOI.md` cho xử lý lỗi chi tiết
