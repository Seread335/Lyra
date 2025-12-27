# CÂU HỎI THƯỜNG GẶP - LYRA NNLT v2.3.22.1

## Mục Đích

Tài liệu này trả lời các câu hỏi phổ biến từ người dùng Lyra NNLT.

---

## PHẦN 1: CÂU HỎI CƠ BẢN

### Q1: Lyra NNLT là gì?

**A:** Lyra NNLT là một ngôn ngữ lập trình hiện đại với:
- Cú pháp đơn giản, dễ học
- Bytecode VM hiệu suất cao
- JIT compilation tự động
- Quản lý bộ nhớ thông minh
- Hệ thống xử lý lỗi mạnh mẽ
- Hỗ trợ lập trình đa tiến trình

---

### Q2: Tôi nên bắt đầu từ đâu?

**A:** Làm theo các bước sau:

1. **Đọc Hướng Dẫn Cơ Bản**:
   ```
   docs/01_HUONG_DAN_LAP_TRIN.md
   ```
   - Hiểu cú pháp cơ bản
   - Tìm hiểu kiểu dữ liệu
   - Học cấu trúc điều khiển

2. **Kiểm Tra API Reference**:
   ```
   docs/02_TAI_LIEU_THAM_KHAO_API.md
   ```
   - Khám phá các hàm có sẵn
   - Học cách sử dụng từng hàm
   - Thực hành với ví dụ

3. **Thực Hành Ví Dụ**:
   ```
   docs/03_VI_DU_NANG_CAO.md
   ```
   - Chạy những ví dụ đơn giản
   - Sửa đổi và thử nghiệm
   - Tìm hiểu cách hoạt động

---

### Q3: Lyra NNLT có miễn phí không?

**A:** Vâng, Lyra NNLT hoàn toàn miễn phí và mã nguồn mở.
- Giấy phép: MIT
- Sử dụng tự do
- Có thể sửa đổi
- Có thể phân phối

---

### Q4: Lyra NNLT chạy được trên Windows, Mac, Linux không?

**A:** Vâng, Lyra NNLT chạy trên tất cả nền tảng chính:
- **Windows** - 7, 8, 10, 11
- **Mac** - OS X 10.9+
- **Linux** - Ubuntu, Debian, Fedora, và các bản phân phối khác

---

## PHẦN 2: CÂU HỎI VỀ CÚ PHÁP VÀ TÍNH NĂNG

### Q5: Làm cách nào để khai báo biến?

**A:** Sử dụng từ khóa `var`:

```lyra
var ten: str = "Lyra"
var tuoi: i32 = 25
var diem: f64 = 95.5
var danh_sach: [i32] = []
```

Hoặc để trình biên dịch tự suy luận kiểu:

```lyra
var ten = "Lyra"
var tuoi = 25
```

---

### Q6: Làm cách nào để định nghĩa hàm?

**A:** Sử dụng từ khóa `proc`:

```lyra
proc cong(a: i32, b: i32) -> i32 {
    return a + b
}

// Gọi hàm
var ket_qua = cong(5, 3)
print("Kết quả: " + tostring(ket_qua))  // Output: 8
```

---

### Q7: Làm cách nào để vòng lặp?

**A:** Lyra NNLT hỗ trợ hai loại vòng lặp:

**While loop:**
```lyra
var i = 0
while i < 5 {
    print(tostring(i))
    i = i + 1
}
// Output: 0 1 2 3 4
```

**For loop (không hỗ trợ trực tiếp, dùng while thay thế):**
```lyra
var mang = [10, 20, 30, 40]
var i = 0
while i < length(mang) {
    print(tostring(mang[i]))
    i = i + 1
}
// Output: 10 20 30 40
```

---

### Q8: Lyra NNLT có hỗ trợ mảng đa chiều không?

**A:** Không trực tiếp, nhưng có thể mô phỏng:

```lyra
// Tạo mảng 2D bằng mảng của mảng
proc tao_ma_tran(hang: i32, cot: i32) -> [[i32]] {
    var ma_tran: [[i32]]
    var h = 0
    
    while h < hang {
        var dong: [i32]
        var c = 0
        
        while c < cot {
            insert(dong, 0)
            c = c + 1
        }
        
        insert(ma_tran, dong)
        h = h + 1
    }
    
    return ma_tran
}

// Sử dụng
var ma_tran = tao_ma_tran(3, 3)
ma_tran[0][0] = 1
print(tostring(ma_tran[0][0]))  // Output: 1
```

---

### Q9: Làm cách nào để sắp xếp mảng?

**A:** Viết hàm quicksort hoặc sử dụng thuật toán khác:

```lyra
proc quicksort(mang: [i32], trai: i32, phai: i32) {
    if trai >= phai {
        return
    }
    
    // Chọn pivot
    var pivot_idx = trai
    var pivot = mang[pivot_idx]
    
    // Phân vùng
    var left = trai + 1
    var right = phai
    
    while left <= right {
        while left <= right && mang[left] <= pivot {
            left = left + 1
        }
        
        while left <= right && mang[right] > pivot {
            right = right - 1
        }
        
        if left < right {
            // Hoán đổi
            var temp = mang[left]
            mang[left] = mang[right]
            mang[right] = temp
        }
    }
    
    // Hoán đổi pivot
    var temp = mang[trai]
    mang[trai] = mang[right]
    mang[right] = temp
    
    // Đệ quy sắp xếp
    quicksort(mang, trai, right - 1)
    quicksort(mang, right + 1, phai)
}

// Sử dụng
var mang = [64, 34, 25, 12, 22, 11, 90]
quicksort(mang, 0, 6)

var i = 0
print("Mảng sau sắp xếp: ")
while i < length(mang) {
    print(tostring(mang[i]) + " ")
    i = i + 1
}
// Output: 11 12 22 25 34 64 90
```

---

### Q10: Làm cách nào để kiểm tra kiểu dữ liệu?

**A:** Sử dụng các hàm kiểm tra:

```lyra
proc kiem_tra_kieu(gia_tri: i32) {
    // Kiểm tra xem có phải số không
    var la_so = true
    
    // Kiểm tra xem có phải âm không
    if gia_tri < 0 {
        print("Là số âm")
    }
    else {
        print("Là số dương")
    }
}

kiem_tra_kieu(-5)   // Output: Là số âm
kiem_tra_kieu(10)   // Output: Là số dương
```

---

## PHẦN 3: CÂU HỎI VỀ HIỆU NĂNG

### Q11: Làm cách nào để viết code nhanh hơn?

**A:** Thực hành các kỹ thuật tối ưu:

```lyra
// 1. Tránh tính toán lặp lại
proc tim_tong_chi_dung(mang: [i32]) -> i32 {
    var tong = 0
    var do_dai = length(mang)  // Tính một lần
    var i = 0
    
    while i < do_dai {
        tong = tong + mang[i]
        i = i + 1
    }
    
    return tong
}

// 2. Tránh vòng lặp lồng không cần thiết
proc tim_phan_tu(mang: [i32], gia_tri: i32) -> bool {
    var i = 0
    
    while i < length(mang) {
        if mang[i] == gia_tri {
            return true  // Thoát sớm
        }
        i = i + 1
    }
    
    return false
}

// 3. Chọn cấu trúc dữ liệu phù hợp
proc tim_trung_binh(mang: [i32]) -> i32 {
    var tong = 0
    var i = 0
    
    // Một vòng lặp thay vì hai
    while i < length(mang) {
        tong = tong + mang[i]
        i = i + 1
    }
    
    return tong / length(mang)
}
```

---

### Q12: Chương trình của tôi chạy chậm, phải làm sao?

**A:** Thực hiện các bước gỡ lỗi hiệu năng:

1. **Xác định bottleneck (điểm nghẽn)**:
   ```lyra
   // Thêm print để đo thời gian
   print("Bắt đầu vòng lặp")
   
   var i = 0
   while i < 1000000 {
       // Xử lý dữ liệu
       i = i + 1
   }
   
   print("Kết thúc vòng lặp")
   ```

2. **Tối ưu hóa vòng lặp**:
   ```lyra
   // Tránh gọi hàm trong vòng lặp
   var do_dai = length(mang)  // Gọi một lần
   var i = 0
   
   while i < do_dai {
       // Xử lý dữ liệu
       i = i + 1
   }
   ```

3. **Sử dụng JIT optimization**:
   ```lyra
   // JIT tự động tối ưu hóa code
   // Không cần làm gì, chỉ viết code tốt
   ```

---

### Q13: Tôi nên sử dụng mảng hay biến đơn lẻ?

**A:** Tùy vào nhu cầu:

- **Biến đơn lẻ**: Khi bạn chỉ cần lưu một giá trị
  ```lyra
  var tuoi = 25
  var ten = "Ly"
  ```

- **Mảng**: Khi bạn cần lưu nhiều giá trị cùng kiểu
  ```lyra
  var tuoi_nhieu_nguoi = [25, 30, 22, 28]
  var ten_nhieu_nguoi = ["Ly", "An", "Bình"]
  ```

---

## PHẦN 4: CÂU HỎI VỀ DEBUG VÀ KHẮC PHỤC SỰ CỐ

### Q14: Chương trình tôi bị lỗi, tôi phải làm sao?

**A:** Làm theo các bước sau:

1. **Đọc thông báo lỗi cẩn thận**:
   ```
   Lỗi: Chỉ số vượt quá giới hạn: 5
   ```

2. **Tìm dòng gây lỗi**: Kiểm tra dòng có đặc điểm được mô tả

3. **Thêm in theo dõi** (print debugging):
   ```lyra
   var mang = [1, 2, 3]
   print("Độ dài mảng: " + tostring(length(mang)))
   print("Truy cập chỉ số: 5")
   var gia_tri = mang[5]  // Lỗi ở đây
   ```

4. **Sửa lỗi**: Thêm kiểm tra giới hạn
   ```lyra
   var mang = [1, 2, 3]
   var chi_so = 5
   
   if chi_so >= 0 && chi_so < length(mang) {
       var gia_tri = mang[chi_so]
   }
   else {
       print("Lỗi: Chỉ số ngoài phạm vi")
   }
   ```

---

### Q15: Làm cách nào để kiểm tra lỗi trong chương trình?

**A:** Sử dụng hệ thống xử lý lỗi:

```lyra
proc chia_co_kiem_tra(a: i32, b: i32) -> i32 {
    // Kiểm tra chia cho zero
    if b == 0 {
        setErrorQuick(7001, "Không thể chia cho zero")
        return -1
    }
    
    return a / b
}

// Gọi và kiểm tra
var ket_qua = chia_co_kiem_tra(10, 0)

if hasError() {
    print("Có lỗi: " + getErrorMessage())
}
else {
    print("Kết quả: " + tostring(ket_qua))
}
```

---

### Q16: Code của tôi biên dịch nhưng không chạy?

**A:** Kiểm tra các vấn đề phổ biến:

1. **Quên gọi initLyraOptimized()**:
   ```lyra
   // Sai
   var mang = []
   insert(mang, 10)  // Có thể bị lỗi
   
   // Đúng
   initLyraOptimized()
   var mang = []
   insert(mang, 10)  // Hoạt động bình thường
   ```

2. **Quên khai báo biến**:
   ```lyra
   // Sai
   print(tuoi)  // tuoi chưa được khai báo
   
   // Đúng
   var tuoi = 25
   print(tostring(tuoi))
   ```

3. **Kiểu dữ liệu không khớp**:
   ```lyra
   // Sai
   var xau = "hello"
   var so = xau + 5  // Lỗi: cộng xâu và số
   
   // Đúng
   var xau = "hello"
   var so = 5
   var ket_qua = xau + tostring(so)
   ```

---

## PHẦN 5: CÂU HỎI NÂNG CAO

### Q17: Làm cách nào để viết code có thể tái sử dụng?

**A:** Chia code thành các hàm nhỏ:

```lyra
// Hàm tái sử dụng được
proc tinh_chu_vi_hinh_vuong(canh: i32) -> i32 {
    return canh * 4
}

proc tinh_dien_tich_hinh_vuong(canh: i32) -> i32 {
    return canh * canh
}

// Sử dụng lại
var canh = 5
var chu_vi = tinh_chu_vi_hinh_vuong(canh)
var dien_tich = tinh_dien_tich_hinh_vuong(canh)

print("Cạnh: " + tostring(canh))
print("Chu vi: " + tostring(chu_vi))      // 20
print("Diện tích: " + tostring(dien_tich))  // 25
```

---

### Q18: Làm cách nào để debug code phức tạp?

**A:** Sử dụng nhật ký chi tiết:

```lyra
var nhat_ky: [str]

proc log(thong_bao: str) {
    insert(nhat_ky, thong_bao)
}

proc xuat_nhat_ky() {
    var i = 0
    print("\n=== NHẬT KÝ ===\n")
    
    while i < length(nhat_ky) {
        print(nhat_ky[i])
        i = i + 1
    }
    
    print("\n=== KẾT THÚC NHẬT KÝ ===\n")
}

// Sử dụng
proc tao_ma_tran(hang: i32, cot: i32) -> [[i32]] {
    log("Bắt đầu tạo ma trận " + tostring(hang) + "x" + tostring(cot))
    
    var ma_tran: [[i32]]
    var h = 0
    
    while h < hang {
        log("Tạo hàng " + tostring(h))
        var dong: [i32]
        var c = 0
        
        while c < cot {
            insert(dong, 0)
            c = c + 1
        }
        
        insert(ma_tran, dong)
        h = h + 1
    }
    
    log("Kết thúc tạo ma trận")
    return ma_tran
}

// Chạy
var ma_tran = tao_ma_tran(2, 2)
xuat_nhat_ky()
```

---

### Q19: Làm cách nào để hãng tải lớn?

**A:** Sử dụng cấu trúc tối ưu:

```lyra
// Tránh: Tạo mảng quá lớn không cần thiết
// var mang_lon_vo_ich: [i32]

// Dùng: Xử lý dữ liệu từng phần
proc xu_ly_du_lieu(so_luong: i32) {
    var i = 0
    
    while i < so_luong {
        // Xử lý từng phần tử
        var gia_tri = i * 2
        
        // Không lưu tất cả, chỉ xử lý
        print(tostring(gia_tri))
        
        i = i + 1
    }
}

xu_ly_du_lieu(1000000)  // Xử lý 1 triệu mà không tạo mảng
```

---

### Q20: Tôi nên tổ chức code như thế nào?

**A:** Sử dụng cấu trúc rõ ràng:

```lyra
// ====== PHẦN 1: KHAI BÁO BIẾN GLOBAL ======
var dat_tich: [i32]

// ====== PHẦN 2: HÀM HELPER ======
proc in_mang(mang: [i32]) {
    var i = 0
    while i < length(mang) {
        print(tostring(mang[i]) + " ")
        i = i + 1
    }
    print("")
}

// ====== PHẦN 3: HÀM CHÍNH ======
proc main() {
    // Khởi tạo hệ thống
    initLyraOptimized()
    
    // Xử lý dữ liệu
    insert(dat_tich, 10)
    insert(dat_tich, 20)
    insert(dat_tich, 30)
    
    // In kết quả
    print("Dữ liệu: ")
    in_mang(dat_tich)
}

// ====== PHẦN 4: CHẠY CHƯƠNG TRÌNH ======
main()
```

---

## PHẦN 6: LIÊN HỆ VÀ HỖ TRỢ

### Q21: Làm cách nào để báo cáo lỗi?

**A:** Cung cấp thông tin chi tiết:

1. **Mô tả vấn đề**: Code của bạn làm gì?
2. **Code bị lỗi**: Đăng đoạn code nhỏ nhất gây lỗi
3. **Thông báo lỗi**: Sao chép thông báo lỗi đầy đủ
4. **Nền tảng**: Hệ điều hành và phiên bản Lyra NNLT

**Ví dụ báo cáo tốt:**
```
Vấn đề: Chương trình bị lỗi khi sắp xếp mảng lớn
Code:
var mang = [64, 34, 25]
quicksort(mang, 0, 2)

Lỗi: Stack overflow
Nền tảng: Windows 11, Lyra NNLT v2.3.22.1
```

---

### Q22: Có tham khảo API đầy đủ không?

**A:** Vâng, xem tại:
```
docs/02_TAI_LIEU_THAM_KHAO_API.md
```

Hoặc kiểm tra code nguồn trong:
```
lyra_interpreter/src/lyra/
```

---

### Q23: Tôi có thể đóng góp cho Lyra NNLT không?

**A:** Vâng, bạn có thể:

1. **Báo cáo lỗi**: Giúp chúng tôi phát hiện vấn đề
2. **Đề xuất tính năng**: Chia sẻ ý tưởng của bạn
3. **Sửa lỗi**: Gửi pull request
4. **Viết tài liệu**: Cải thiện hướng dẫn

---

### Q24: Tôi cần học trước kiến thức gì?

**A:** Các kiến thức nền tảng lập trình:
- Biến và kiểu dữ liệu
- Vòng lặp và điều kiện
- Hàm và thủ tục
- Mảng và cấu trúc dữ liệu
- Giải quyết vấn đề logic

Không cần kinh nghiệm ngôn ngữ cụ thể nào, nhưng sẽ giúp nếu bạn đã học:
- Python
- Java
- C/C++
- JavaScript

---

## DANH SÁCH KIỂM TRA (CHEAT SHEET)

```lyra
// ===== KHAI BÁO =====
var ten: str = "Giá trị"
var so: i32 = 42
var danh_sach: [i32] = []

// ===== HÀM =====
proc ten_ham(param: kieu) -> kieu_tra_ve {
    return gia_tri_tra_ve
}

// ===== ĐIỀU KIỆN =====
if dieu_kien {
    // Code nếu đúng
}
else {
    // Code nếu sai
}

// ===== VÒNG LẶP =====
while dieu_kien {
    // Code lặp lại
}

// ===== MẢNG =====
var mang: [i32]
insert(mang, 10)
var phan_tu = mang[0]
var do_dai = length(mang)

// ===== IN RA =====
print("Text")
print(tostring(so))

// ===== XỬ LÝ LỖI =====
setErrorQuick(ma_loi, "Thông báo")
if hasError() {
    print(getErrorMessage())
    clearError()
}

// ===== KHỞI TẠO =====
initLyraOptimized()
```

---

## KẾT LUẬN

Hy vọng tài liệu này trả lời được những câu hỏi của bạn. Để biết thêm:

- **Bắt đầu**: Xem `01_HUONG_DAN_LAP_TRIN.md`
- **API**: Xem `02_TAI_LIEU_THAM_KHAO_API.md`
- **Ví dụ**: Xem `03_VI_DU_NANG_CAO.md`
- **Xử lý lỗi**: Xem `04_XU_LY_LOI.md`

Nếu câu hỏi không được trả lời ở đây, hãy kiểm tra tài liệu khác hoặc xem code nguồn.
