# TÀI LIỆU THAM KHẢO API - LYRA NNLT v2.3.22.1

## Mục Đích

Tài liệu này cung cấp tham khảo chi tiết về tất cả các hàm và API có sẵn trong Lyra NNLT.

---

## 1. HÀM IN RA VÀ XUẤT DỮ LIỆU

### print(thong_bao: str)

In một xâu ký tự ra màn hình kèm dòng mới.

**Cú pháp:**
```lyra
print("Hello World")
```

**Tham số:**
- `thong_bao`: Xâu ký tự cần in ra

**Kết quả:**
```
Hello World
```

**Ví dụ:**
```lyra
var ten = "Lyra"
print("Ngôn ngữ: " + ten)  // Output: Ngôn ngữ: Lyra
```

---

## 2. HÀM CHUYỂN ĐỔI KIỂU DỮ LIỆU

### tostring(gia_tri: i32) -> str

Chuyển đổi số nguyên thành xâu ký tự.

**Cú pháp:**
```lyra
var so = 2024
var xau = tostring(so)
```

**Tham số:**
- `gia_tri`: Số nguyên cần chuyển đổi

**Trả về:**
- Xâu ký tự biểu diễn số đó

**Ví dụ:**
```lyra
var nam = 2024
print("Năm: " + tostring(nam))  // Output: Năm: 2024
```

---

## 3. HÀM LÀM VIỆC VỚI MẢNG

### length(mang: [T]) -> i32

Trả về số phần tử trong mảng.

**Cú pháp:**
```lyra
var danh_sach = [1, 2, 3, 4, 5]
var so_phan_tu = length(danh_sach)
```

**Tham số:**
- `mang`: Mảng bất kỳ

**Trả về:**
- Số phần tử trong mảng (kiểu i32)

**Ví dụ:**
```lyra
var con_so = [10, 20, 30]
print("Số phần tử: " + tostring(length(con_so)))  // Output: 3
```

### insert(mang: [T], gia_tri: T)

Thêm phần tử vào cuối mảng.

**Cú pháp:**
```lyra
var danh_sach: [str]
insert(danh_sach, "Phần tử 1")
insert(danh_sach, "Phần tử 2")
```

**Tham số:**
- `mang`: Mảng cần thêm phần tử
- `gia_tri`: Giá trị cần thêm (phải cùng kiểu với mảng)

**Ví dụ:**
```lyra
var que = [10, 20]
insert(que, 30)
insert(que, 40)
// Mảng giờ là [10, 20, 30, 40]
```

---

## 4. HÀM LÀM VIỆC VỚI XÂU KÝ TỰ

### length(xau: str) -> i32

Trả về số ký tự trong xâu.

**Cú pháp:**
```lyra
var van_ban = "Lyra"
var do_dai = length(van_ban)
```

**Tham số:**
- `xau`: Xâu ký tự cần tính độ dài

**Trả về:**
- Số ký tự (kiểu i32)

**Ví dụ:**
```lyra
var tin_nhan = "Hello"
print("Độ dài: " + tostring(length(tin_nhan)))  // Output: 5
```

### substr(xau: str, vi_tri: i32, do_dai: i32) -> str

Tách một phần của xâu.

**Cú pháp:**
```lyra
var van_ban = "Lyra Programming"
var phan_tach = substr(van_ban, 0, 4)
```

**Tham số:**
- `xau`: Xâu gốc
- `vi_tri`: Vị trí bắt đầu (từ 0)
- `do_dai`: Số ký tự cần tách

**Trả về:**
- Phần xâu được tách

**Ví dụ:**
```lyra
var chuoi = "VIETNAM"
print(substr(chuoi, 0, 3))  // Output: VIE
print(substr(chuoi, 4, 3))  // Output: NAM
```

---

## 5. HÀM TOÁN HỌC

### Phép cộng, trừ, nhân, chia

Lyra hỗ trợ các phép toán cơ bản sử dụng ký hiệu:

| Ký hiệu | Phép Toán | Ví dụ |
|---------|-----------|-------|
| `+` | Cộng | `10 + 5 = 15` |
| `-` | Trừ | `10 - 5 = 5` |
| `*` | Nhân | `10 * 5 = 50` |
| `/` | Chia (lấy phần nguyên) | `10 / 3 = 3` |
| `%` | Chia lấy dư | `10 % 3 = 1` |

**Ví dụ:**
```lyra
var a = 20
var b = 3

print(tostring(a + b))  // Output: 23
print(tostring(a - b))  // Output: 17
print(tostring(a * b))  // Output: 60
print(tostring(a / b))  // Output: 6 (lấy phần nguyên)
print(tostring(a % b))  // Output: 2 (dư 2)
```

---

## 6. HÀM QUẢN LÝ TỐI ƯU HÓA

### setOptimizationLevel(muc_do: i32)

Thiết lập cấp độ tối ưu hóa cho chương trình.

**Cú pháp:**
```lyra
setOptimizationLevel(2)
```

**Tham số:**
- `muc_do`: 0 (không tối ưu), 1 (cơ bản), 2 (cao)

**Ví dụ:**
```lyra
// Cho hiệu năng cao
setOptimizationLevel(2)
print("Tối ưu hóa cấp độ 2 kích hoạt")
```

---

## 7. HÀM KHỞI TẠO HỆ THỐNG

### initLyraOptimized()

Khởi tạo toàn bộ hệ thống Lyra với tất cả tính năng.

**Cú pháp:**
```lyra
initLyraOptimized()
```

**Tác dụng:**
- Khởi tạo error handling
- Khởi tạo bytecode VM
- Khởi tạo compiler optimizer
- Khởi tạo memory optimization
- Khởi tạo JIT optimization
- Khởi tạo concurrency framework
- Khởi tạo benchmarking
- Khởi tạo validation rules
- Khởi tạo security hardening

**Ví dụ:**
```lyra
initLyraOptimized()
print("Hệ thống khởi tạo xong")
```

### initLyraQuick()

Khởi tạo hệ thống nhanh chóng (chỉ các thành phần cơ bản).

**Cú pháp:**
```lyra
initLyraQuick()
```

**Ví dụ:**
```lyra
// Khởi tạo nhanh cho ứng dụng đơn giản
initLyraQuick()
print("Khởi tạo nhanh hoàn thành")
```

### startLyraSystem()

Khởi động hệ thống sau khi đã khởi tạo.

**Cú pháp:**
```lyra
initLyraOptimized()
startLyraSystem()
```

---

## 8. HÀM CHẨN ĐOÁN VÀ DEBUGGING

### printSystemStatus()

In trạng thái hiện tại của hệ thống.

**Cú pháp:**
```lyra
initLyraOptimized()
printSystemStatus()
```

**Thông tin in ra:**
- Trạng thái hệ thống
- Số lỗi
- Lỗi cuối cùng
- Các tính năng kích hoạt

### runSystemDiagnostics()

Chạy chẩn đoán toàn bộ hệ thống.

**Cú pháp:**
```lyra
initLyraOptimized()
runSystemDiagnostics()
```

**Tác dụng:**
- Kiểm tra error handling
- Kiểm tra VM stack
- Kiểm tra arithmetic
- Kiểm tra memory
- Kiểm tra concurrency

### dumpComprehensiveReport()

In báo cáo chi tiết của hệ thống.

**Cú pháp:**
```lyra
initLyraOptimized()
dumpComprehensiveReport()
```

---

## 9. HÀM BENCHMARKING VÀ HIỆU NĂNG

### recordBenchmark(ten: str, thoi_gian: i32, lan_lap: i32)

Ghi lại kết quả benchmark.

**Cú pháp:**
```lyra
recordBenchmark("arithmetic_test", 100, 1000)
```

**Tham số:**
- `ten`: Tên benchmark
- `thoi_gian`: Thời gian thực thi (ms)
- `lan_lap`: Số lần lặp

### setBaseline(ten: str)

Đặt giá trị cơ sở để so sánh.

**Cú pháp:**
```lyra
recordBenchmark("test", 50, 1000)
setBaseline("test")
```

### checkRegressions(nguong: i32) -> bool

Kiểm tra xem có suy giảm hiệu năng không.

**Cú pháp:**
```lyra
var co_suy_giam = checkRegressions(10)  // Ngưỡng 10%
```

**Tham số:**
- `nguong`: Ngưỡng phần trăm suy giảm được chấp nhận

**Trả về:**
- true nếu có suy giảm, false nếu không

### runAllBenchmarks()

Chạy tất cả các benchmark.

**Cú pháp:**
```lyra
initLyraOptimized()
runAllBenchmarks()
```

---

## 10. HÀM XỨ LÝ LỖI

### setErrorQuick(ma_loi: i32, thong_bao: str)

Thiết lập lỗi nhanh chóng.

**Cú pháp:**
```lyra
setErrorQuick(1001, "Lỗi stack underflow")
```

**Tham số:**
- `ma_loi`: Mã lỗi (xem bảng mã lỗi)
- `thong_bao`: Thông báo lỗi

### hasError() -> bool

Kiểm tra xem có lỗi xảy ra không.

**Cú pháp:**
```lyra
if hasError() {
    print("Có lỗi")
}
```

**Trả về:**
- true nếu có lỗi, false nếu không

### getErrorCode() -> i32

Lấy mã lỗi hiện tại.

**Cú pháp:**
```lyra
var ma = getErrorCode()
print("Mã lỗi: " + tostring(ma))
```

**Trả về:**
- Mã lỗi (kiểu i32)

### getErrorMessage() -> str

Lấy thông báo lỗi hiện tại.

**Cú pháp:**
```lyra
var tin_nhan = getErrorMessage()
print("Thông báo: " + tin_nhan)
```

**Trả về:**
- Xâu thông báo lỗi

### clearError()

Xóa lỗi hiện tại.

**Cú pháp:**
```lyra
setErrorQuick(1001, "Lỗi test")
clearError()
if !hasError() {
    print("Lỗi đã được xóa")
}
```

---

## 11. BẢNG MÃ LỖI

| Mã Lỗi | Tên | Ý Nghĩa |
|--------|-----|--------|
| 1001 | ERR_VM_STACK_UNDERFLOW | Mảng stack quá ít phần tử |
| 1002 | ERR_VM_STACK_OVERFLOW | Mảng stack quá nhiều phần tử |
| 2001 | ERR_MEM_ALLOCATION_FAILED | Không thể cấp phát bộ nhớ |
| 3001 | ERR_TYPE_MISMATCH | Kiểu dữ liệu không phù hợp |
| 4001 | ERR_BOUNDS_NEGATIVE_INDEX | Chỉ số âm (tối thiểu 0) |
| 4002 | ERR_BOUNDS_OUT_OF_RANGE | Chỉ số vượt quá giới hạn |
| 5001 | ERR_CONC_LOCK_DEADLOCK | Deadlock trong khóa |
| 6001 | ERR_COMP_INVALID_BYTECODE | Bytecode không hợp lệ |
| 7001 | ERR_SEC_INTEGER_OVERFLOW | Tràn số nguyên |
| 8001 | ERR_VAL_CONSTRAINT_VIOLATION | Vi phạm ràng buộc |

---

## 12. KIỂU DỮ LIỆU

| Kiểu | Phạm Vi | Kích Thước |
|------|---------|-----------|
| `i32` | -2,147,483,648 đến 2,147,483,647 | 4 bytes |
| `f64` | Số thực 64-bit | 8 bytes |
| `str` | Xâu ký tự | Thay đổi |
| `bool` | true/false | 1 byte |
| `[i32]` | Mảng số nguyên | Thay đổi |
| `[str]` | Mảng xâu | Thay đổi |

---

## 13. HẰNG SỐ HỆ THỐNG

```lyra
// Giới hạn mảng
var MAX_ARRAY_LENGTH = 1000000

// Giới hạn stack
var MAX_STACK_DEPTH = 100000

// Mã tối ưu hóa
var OPT_LEVEL_NONE = 0
var OPT_LEVEL_BASIC = 1
var OPT_LEVEL_AGGRESSIVE = 2
```

---

## 14. TOÁN TỬ

### So Sánh

| Toán Tử | Ý Nghĩa | Ví Dụ |
|---------|--------|-------|
| `==` | Bằng | `5 == 5` → true |
| `!=` | Không bằng | `5 != 3` → true |
| `<` | Nhỏ hơn | `3 < 5` → true |
| `>` | Lớn hơn | `5 > 3` → true |
| `<=` | Nhỏ hơn hoặc bằng | `5 <= 5` → true |
| `>=` | Lớn hơn hoặc bằng | `5 >= 5` → true |

### Logic

| Toán Tử | Ý Nghĩa | Ví Dụ |
|---------|--------|-------|
| `&&` | AND (cả hai) | `true && false` → false |
| `\|\|` | OR (ít nhất một) | `true \|\| false` → true |
| `!` | NOT (phủ định) | `!true` → false |

### Toán Học

| Toán Tử | Ý Nghĩa | Ví Dụ |
|---------|--------|-------|
| `+` | Cộng | `5 + 3` → 8 |
| `-` | Trừ | `5 - 3` → 2 |
| `*` | Nhân | `5 * 3` → 15 |
| `/` | Chia (phần nguyên) | `7 / 2` → 3 |
| `%` | Chia lấy dư | `7 % 2` → 1 |

---

## 15. CẤU TRÚC ĐIỀU KHIỂN

### If - Else If - Else

```lyra
if dieu_kien_1 {
    // Thực thi nếu dieu_kien_1 đúng
}
else if dieu_kien_2 {
    // Thực thi nếu dieu_kien_2 đúng
}
else {
    // Thực thi nếu cả hai đều sai
}
```

### While Loop

```lyra
while dieu_kien {
    // Thực thi lặp lại khi dieu_kien đúng
    // Phải thay đổi dieu_kien để thoát
}
```

### Break

```lyra
while dieu_kien {
    if thoat_dieu_kien {
        break  // Thoát khỏi vòng lặp ngay lập tức
    }
}
```

---

## 16. KHAI BÁO BIẾN VÀ HÀM

### Biến

```lyra
var ten_bien: kieu_du_lieu = gia_tri_ban_dau
```

### Hàm

```lyra
proc ten_ham(tham_so_1: kieu_1, tham_so_2: kieu_2) -> kieu_tra_ve {
    // Thân hàm
    return gia_tri_tra_ve
}
```

---

## 17. THỨ TỰ ƯU TIÊN TOÁN TỬ

| Mức | Toán Tử |
|-----|---------|
| 1 (Cao nhất) | Parentheses `()` |
| 2 | Nhân `*`, Chia `/`, Chia dư `%` |
| 3 | Cộng `+`, Trừ `-` |
| 4 | So sánh `<`, `>`, `<=`, `>=` |
| 5 | Bằng `==`, Không bằng `!=` |
| 6 | AND `&&` |
| 7 (Thấp nhất) | OR `\|\|` |

**Ví dụ:**
```lyra
var ket_qua = 2 + 3 * 4  // = 2 + (3 * 4) = 14
var ket_qua_2 = (2 + 3) * 4  // = 5 * 4 = 20
```

---

## KẾT LUẬN

Đây là danh sách toàn bộ API có sẵn trong Lyra NNLT. Để tìm hiểu thêm:

- Xem `01_HUONG_DAN_LAP_TRIN.md` cho hướng dẫn với ví dụ
- Xem `03_VI_DU_NANG_CAO.md` cho các ví dụ phức tạp
- Xem `04_XU_LY_LOI.md` cho xử lý lỗi chi tiết
