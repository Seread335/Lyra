# XỬ LÝ LỖI VÀ GỠLỖI - LYRA NNLT v2.3.22.1

## Mục Đích

Tài liệu này hướng dẫn cách xử lý lỗi, gỡ lỗi chương trình, và khắc phục sự cố.

---

## 1. HỆ THỐNG XỬ LÝ LỖI

### 1.1 Kiểu Lỗi và Mã Lỗi

Lyra NNLT cung cấp 150+ mã lỗi cụ thể, phân loại theo nhóm:

| Nhóm | Phạm Vi | Ví Dụ |
|------|---------|-------|
| **VM Errors** | 1000-1199 | Stack underflow, stack overflow |
| **Memory Errors** | 2000-2199 | Allocation failed |
| **Type Errors** | 3000-3199 | Type mismatch |
| **Bounds Errors** | 4000-4199 | Index out of range |
| **Concurrency Errors** | 5000-5199 | Deadlock |
| **Compiler Errors** | 6000-6199 | Invalid bytecode |
| **Security Errors** | 7000-7199 | Integer overflow |
| **Validation Errors** | 8000-8199 | Constraint violation |

---

## 2. PHÁT HIỆN LỖI

### 2.1 Kiểm Tra Xem Có Lỗi

```lyra
// Khởi tạo hệ thống
initLyraOptimized()

// Cố gắng thực hiện phép toán
var a = 10
var b = 0

if b != 0 {
    var ket_qua = a / b
}
else {
    // Đặt lỗi
    setErrorQuick(1001, "Không thể chia cho zero")
}

// Kiểm tra xem có lỗi xảy ra
if hasError() {
    print("Có lỗi xảy ra")
    
    // Lấy mã lỗi
    var ma_loi = getErrorCode()
    print("Mã lỗi: " + tostring(ma_loi))
    
    // Lấy thông báo lỗi
    var tin_nhan = getErrorMessage()
    print("Thông báo: " + tin_nhan)
}
else {
    print("Không có lỗi")
}
```

Giải thích:
- `hasError()`: Kiểm tra xem có lỗi hiện tại
- `getErrorCode()`: Lấy mã lỗi
- `getErrorMessage()`: Lấy thông báo mô tả lỗi

### 2.2 Xóa Lỗi

```lyra
// Đặt lỗi
setErrorQuick(4001, "Chỉ số âm")
print("Có lỗi: " + tostring(hasError()))  // true

// Xóa lỗi
clearError()
print("Sau xóa: " + tostring(hasError()))  // false
```

---

## 3. KIỂM TRA ĐẦU VÀO

### 3.1 Xác Thực Mảng

```lyra
proc xac_thuc_mang(mang: [i32]) -> bool {
    // Kiểm tra mảng rỗng
    if length(mang) == 0 {
        setErrorQuick(4001, "Mảng không thể rỗng")
        return false
    }
    
    // Kiểm tra kích thước hợp lệ
    if length(mang) > 1000000 {
        setErrorQuick(4002, "Mảng quá lớn")
        return false
    }
    
    return true
}

// Sử dụng
var mang = [1, 2, 3]
if xac_thuc_mang(mang) {
    print("Mảng hợp lệ")
}
else {
    print("Lỗi: " + getErrorMessage())
}
```

### 3.2 Xác Thực Xâu Ký Tự

```lyra
proc xac_thuc_xau(xau: str, do_dai_toi_thieu: i32, do_dai_toi_da: i32) -> bool {
    // Kiểm tra xâu không rỗng
    if length(xau) == 0 {
        setErrorQuick(8001, "Xâu không thể rỗng")
        return false
    }
    
    // Kiểm tra độ dài tối thiểu
    if length(xau) < do_dai_toi_thieu {
        setErrorQuick(8001, "Xâu quá ngắn")
        return false
    }
    
    // Kiểm tra độ dài tối đa
    if length(xau) > do_dai_toi_da {
        setErrorQuick(8001, "Xâu quá dài")
        return false
    }
    
    return true
}

// Sử dụng
if xac_thuc_xau("hello", 3, 10) {
    print("Xâu hợp lệ")
}
else {
    print("Lỗi: " + getErrorMessage())
}
```

### 3.3 Xác Thực Số

```lyra
proc xac_thuc_so(so: i32, toi_thieu: i32, toi_da: i32) -> bool {
    // Kiểm tra phạm vi
    if so < toi_thieu || so > toi_da {
        setErrorQuick(4002, "Số ngoài phạm vi cho phép")
        return false
    }
    
    return true
}

// Sử dụng
var tuoi = 25
if xac_thuc_so(tuoi, 0, 150) {
    print("Tuổi hợp lệ")
}
else {
    print("Lỗi: " + getErrorMessage())
}
```

---

## 4. XỬ LÝ LỖI TRY-CATCH

Mặc dù Lyra không có try-catch, bạn có thể mô phỏng bằng cách kiểm tra lỗi:

```lyra
proc thuc_hien_voi_xu_ly_loi(a: i32, b: i32) -> i32 {
    // "TRY": Cố gắng thực hiện
    if b == 0 {
        // "CATCH": Xử lý lỗi
        setErrorQuick(7001, "Không thể chia cho zero")
        return -1  // Giá trị lỗi
    }
    
    // Thực hiện phép toán
    return a / b
}

// Sử dụng
var ket_qua = thuc_hien_voi_xu_ly_loi(10, 0)

if ket_qua == -1 && hasError() {
    print("Lỗi xảy ra: " + getErrorMessage())
}
else {
    print("Kết quả: " + tostring(ket_qua))
}
```

---

## 5. GỠ LỖI VỚI PRINT

### 5.1 Theo Dõi Giá Trị

```lyra
proc tinh_toan_co_theo_doi(a: i32, b: i32) -> i32 {
    print("=== BẮT ĐẦU TÍNH TOÁN ===")
    print("Đầu vào: a=" + tostring(a) + ", b=" + tostring(b))
    
    var buoc_1 = a + b
    print("Bước 1 (a + b): " + tostring(buoc_1))
    
    var buoc_2 = buoc_1 * 2
    print("Bước 2 (kết quả * 2): " + tostring(buoc_2))
    
    var buoc_3 = buoc_2 / 4
    print("Bước 3 (kết quả / 4): " + tostring(buoc_3))
    
    print("=== KẾT THÚC TÍNH TOÁN ===")
    return buoc_3
}

// Chạy với in theo dõi
tinh_toan_co_theo_doi(10, 20)
// Output:
// === BẮT ĐẦU TÍNH TOÁN ===
// Đầu vào: a=10, b=20
// Bước 1 (a + b): 30
// Bước 2 (kết quả * 2): 60
// Bước 3 (kết quả / 4): 15
// === KẾT THÚC TÍNH TOÁN ===
```

### 5.2 Ghi Nhật Ký (Logging)

```lyra
var nhat_ky: [str]

proc ghi_nhat_ky(thong_bao: str) {
    insert(nhat_ky, thong_bao)
}

proc in_nhat_ky() {
    var i = 0
    print("=== NHẬT KÝ ===")
    
    while i < length(nhat_ky) {
        print(tostring(i + 1) + ". " + nhat_ky[i])
        i = i + 1
    }
}

// Sử dụng
ghi_nhat_ky("Bắt đầu chương trình")
ghi_nhat_ky("Khởi tạo biến")
ghi_nhat_ky("Thực hiện tính toán")
ghi_nhat_ky("Kết thúc thành công")

in_nhat_ky()
// Output:
// === NHẬT KÝ ===
// 1. Bắt đầu chương trình
// 2. Khởi tạo biến
// 3. Thực hiện tính toán
// 4. Kết thúc thành công
```

---

## 6. XỬ LÝ TÌNH HUỐNG RANH GIỚI

### 6.1 Truy Cập Mảng An Toàn

```lyra
proc truy_cap_mang_an_toan(mang: [i32], chi_so: i32) -> i32 {
    // Kiểm tra chỉ số âm
    if chi_so < 0 {
        setErrorQuick(4001, "Chỉ số không thể âm: " + tostring(chi_so))
        return -1
    }
    
    // Kiểm tra chỉ số vượt quá
    if chi_so >= length(mang) {
        setErrorQuick(4002, "Chỉ số vượt quá giới hạn: " + tostring(chi_so))
        return -1
    }
    
    // Truy cập an toàn
    return mang[chi_so]
}

// Sử dụng
var danh_sach = [10, 20, 30, 40, 50]

var gia_tri = truy_cap_mang_an_toan(danh_sach, 2)
if !hasError() {
    print("Giá trị: " + tostring(gia_tri))  // Output: 30
}

var gia_tri_2 = truy_cap_mang_an_toan(danh_sach, 10)
if hasError() {
    print("Lỗi: " + getErrorMessage())  // Output: Lỗi: Chỉ số vượt quá giới hạn: 10
}
```

### 6.2 Phép Chia An Toàn

```lyra
proc chia_an_toan(so_bi_chia: i32, so_chia: i32) -> i32 {
    // Kiểm tra chia cho zero
    if so_chia == 0 {
        setErrorQuick(7001, "Không thể chia cho zero")
        return 0
    }
    
    // Kiểm tra overflow (tràn)
    if so_bi_chia == -2147483648 && so_chia == -1 {
        setErrorQuick(7001, "Phép chia gây tràn số")
        return 0
    }
    
    return so_bi_chia / so_chia
}

// Sử dụng
var ket_qua = chia_an_toan(20, 4)
if !hasError() {
    print("Kết quả: " + tostring(ket_qua))  // Output: 5
}

var ket_qua_2 = chia_an_toan(20, 0)
if hasError() {
    print("Lỗi: " + getErrorMessage())  // Output: Lỗi: Không thể chia cho zero
}
```

---

## 7. CHẨN ĐOÁN HỆ THỐNG

### 7.1 Chạy Chẩn Đoán

```lyra
proc chay_chan_doan_toan_bo() {
    // Khởi tạo hệ thống
    initLyraOptimized()
    
    // Chạy chẩn đoán
    print("Chạy chẩn đoán hệ thống...")
    runSystemDiagnostics()
    
    // In trạng thái
    print("\nTranh thái hệ thống:")
    printSystemStatus()
    
    // Chạy benchmark
    print("\nChạy benchmark...")
    runAllBenchmarks()
}

chay_chan_doan_toan_bo()
```

### 7.2 Kiểm Tra Từng Thành Phần

```lyra
proc kiem_tra_thanh_phan() {
    // Khởi tạo
    initLyraOptimized()
    
    // Test error handling
    print("Testing error handling...")
    setErrorQuick(1001, "Test error")
    if hasError() {
        print("Error handling: OK")
        clearError()
    }
    else {
        print("Error handling: FAILED")
    }
    
    // Test arithmetic
    print("Testing arithmetic...")
    var test = 2 + 3
    if test == 5 {
        print("Arithmetic: OK")
    }
    else {
        print("Arithmetic: FAILED")
    }
    
    // Test arrays
    print("Testing arrays...")
    var mang: [i32]
    insert(mang, 10)
    insert(mang, 20)
    if length(mang) == 2 {
        print("Arrays: OK")
    }
    else {
        print("Arrays: FAILED")
    }
}

kiem_tra_thanh_phan()
```

---

## 8. CÁC SỰ CỐ PHỔ BIẾN

### 8.1 Vòng Lặp Vô Hạn

**Vấn đề:**
```lyra
var x = 0
while x < 5 {
    print("Lặp")
    // Quên tăng x!
}
```

**Giải pháp:**
```lyra
var x = 0
while x < 5 {
    print("Lặp " + tostring(x))
    x = x + 1  // Đảm bảo thoát khỏi vòng lặp
}
```

### 8.2 Mảng Vượt Giới Hạn

**Vấn đề:**
```lyra
var mang = [1, 2, 3]
var gia_tri = mang[10]  // Lỗi: chỉ số 10 không tồn tại
```

**Giải pháp:**
```lyra
var mang = [1, 2, 3]
var chi_so = 10

if chi_so >= 0 && chi_so < length(mang) {
    var gia_tri = mang[chi_so]
}
else {
    setErrorQuick(4002, "Chỉ số ngoài phạm vi")
}
```

### 8.3 Chia Cho Zero

**Vấn đề:**
```lyra
var a = 10
var b = 0
var ket_qua = a / b  // Lỗi
```

**Giải pháp:**
```lyra
var a = 10
var b = 0

if b != 0 {
    var ket_qua = a / b
}
else {
    setErrorQuick(7001, "Không thể chia cho zero")
}
```

---

## 9. HÌNH ẢNH LÀM VIỆC TRÊN WINDOWS VÀ LINUX

### 9.1 Windows

```lyra
// Khởi tạo
initLyraOptimized()

// Chạy chương trình
print("Chương trình đang chạy trên Windows...")

// In đường dẫn (nếu cần)
print("Sử dụng đường dẫn: C:\\Users\\YourName\\lyra_program")

// Dọn dẹp
clearError()
```

### 9.2 Linux/Mac

```lyra
// Khởi tạo
initLyraOptimized()

// Chạy chương trình
print("Chương trình đang chạy trên Linux/Mac...")

// In đường dẫn (nếu cần)
print("Sử dụng đường dẫn: /home/username/lyra_program")

// Dọn dẹp
clearError()
```

---

## 10. DANH SÁCH KIỂM TRA GỠ LỖI

Khi gặp vấn đề, kiểm tra danh sách này:

1. Lỗi Cú Pháp
   - [ ] Kiểm tra dấu ngoặc cân bằng
   - [ ] Kiểm tra dấu hai chấm trong khai báo
   - [ ] Kiểm tra từ khóa chính tả

2. Lỗi Logic
   - [ ] Kiểm tra điều kiện if/while
   - [ ] Kiểm tra giá trị ban đầu biến
   - [ ] Kiểm tra vòng lặp có thoát được không

3. Lỗi Dữ Liệu
   - [ ] Kiểm tra chỉ số mảng hợp lệ
   - [ ] Kiểm tra kiểu dữ liệu phù hợp
   - [ ] Kiểm tra các giá trị null/rỗng

4. Lỗi Hiệu Năng
   - [ ] Kiểm tra vòng lặp lồng không cần thiết
   - [ ] Kiểm tra mảng quá lớn
   - [ ] Kiểm tra thuật toán tối ưu

---

## KẾT LUẬN

Xử lý lỗi tốt giúp chương trình:
- Ổn định hơn
- Dễ bảo trì hơn
- Cung cấp thông báo lỗi rõ ràng

Để tìm hiểu thêm:
- Xem `01_HUONG_DAN_LAP_TRIN.md` cho kiến thức cơ bản
- Xem `02_TAI_LIEU_THAM_KHAO_API.md` cho API
- Xem `03_VI_DU_NANG_CAO.md` cho ví dụ phức tạp
