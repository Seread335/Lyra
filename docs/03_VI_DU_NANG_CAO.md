# VÍ DỤ NÂNG CAO - LYRA NNLT v2.3.22.1

## Mục Đích

Tài liệu này cung cấp các ví dụ nâng cao và các kỹ thuật lập trình tiên tiến.

---

## 1. SẮPXẾP MẢNG (SORTING)

### 1.1 Bubble Sort

Sắp xếp bằng cách so sánh và hoán đổi các phần tử kế cận.

```lyra
proc bubble_sort(mang: [i32]) {
    var n = length(mang)
    var i = 0
    
    while i < n {
        var j = 0
        
        while j < n - i - 1 {
            // So sánh hai phần tử kế cận
            if mang[j] > mang[j + 1] {
                // Hoán đổi
                var temp = mang[j]
                mang[j] = mang[j + 1]
                mang[j + 1] = temp
            }
            j = j + 1
        }
        i = i + 1
    }
}

// Sử dụng
var so = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(so)

// In kết quả
var k = 0
while k < length(so) {
    print(tostring(so[k]))
    k = k + 1
}
// Output: 11, 12, 22, 25, 34, 64, 90
```

Giải thích:
- **Bubble Sort**: Sắp xếp bằng cách lặp qua mảng, so sánh từng cặp kế cận
- **Độ phức tạp**: O(n²) - không hiệu quả cho dữ liệu lớn
- **Ưu điểm**: Dễ hiểu, không cần bộ nhớ phụ

---

## 2. TÌM KIẾM (SEARCHING)

### 2.1 Tìm Kiếm Tuyến Tính

```lyra
proc tim_kiem_tuyen_tinh(mang: [i32], gia_tri: i32) -> i32 {
    var i = 0
    
    while i < length(mang) {
        if mang[i] == gia_tri {
            return i  // Tìm thấy
        }
        i = i + 1
    }
    
    return -1  // Không tìm thấy
}

// Sử dụng
var danh_sach = [15, 23, 8, 42, 16, 4]
var gia_tri_tim = 42
var vi_tri = tim_kiem_tuyen_tinh(danh_sach, gia_tri_tim)

if vi_tri != -1 {
    print("Tìm thấy tại vị trí: " + tostring(vi_tri))
}
else {
    print("Không tìm thấy")
}
// Output: Tìm thấy tại vị trí: 3
```

Giải thích:
- **Tìm kiếm tuyến tính**: Kiểm tra từng phần tử lần lượt
- **Độ phức tạp**: O(n)
- **Trường hợp sử dụng**: Dữ liệu nhỏ hoặc không sắp xếp

### 2.2 Tìm Kiếm Nhị Phân

```lyra
proc tim_kiem_nhi_phan(mang: [i32], gia_tri: i32) -> i32 {
    var trai = 0
    var phai = length(mang) - 1
    
    while trai <= phai {
        var giua = (trai + phai) / 2
        
        if mang[giua] == gia_tri {
            return giua  // Tìm thấy
        }
        else if mang[giua] < gia_tri {
            trai = giua + 1  // Tìm ở nửa phải
        }
        else {
            phai = giua - 1  // Tìm ở nửa trái
        }
    }
    
    return -1  // Không tìm thấy
}

// Sử dụng (mảng phải được sắp xếp)
var con_so = [4, 8, 15, 16, 23, 42, 50]
var tim = 23
var chi_so = tim_kiem_nhi_phan(con_so, tim)

if chi_so != -1 {
    print("Tìm thấy tại vị trí: " + tostring(chi_so))
}
else {
    print("Không tìm thấy")
}
// Output: Tìm thấy tại vị trí: 4
```

Giải thích:
- **Tìm kiếm nhị phân**: Chia đôi không gian tìm kiếm mỗi lần
- **Điều kiện**: Mảng phải đã được sắp xếp
- **Độ phức tạp**: O(log n) - rất nhanh
- **Ưu điểm**: Hiệu quả cho dữ liệu lớn

---

## 3. TÍNH TOÁN ĐỘNG (DYNAMIC PROGRAMMING)

### 3.1 Fibonacci Tối Ưu

```lyra
// Phương pháp 1: Đệ quy naive (chậm)
proc fibonacci_naive(n: i32) -> i32 {
    if n <= 1 {
        return n
    }
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
}

// Phương pháp 2: Sử dụng Memoization (tối ưu)
var memo: [i32]
var memo_init = false

proc fibonacci_memo(n: i32) -> i32 {
    if !memo_init {
        var i = 0
        while i <= 40 {
            insert(memo, -1)  // -1 = chưa tính
            i = i + 1
        }
        memo_init = true
    }
    
    if n <= 1 {
        return n
    }
    
    if memo[n] != -1 {
        return memo[n]  // Đã tính rồi
    }
    
    var ket_qua = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    memo[n] = ket_qua
    return ket_qua
}

// Phương pháp 3: Lặp (tối ưu nhất)
proc fibonacci_lap(n: i32) -> i32 {
    if n <= 1 {
        return n
    }
    
    var a = 0
    var b = 1
    var i = 2
    
    while i <= n {
        var temp = a + b
        a = b
        b = temp
        i = i + 1
    }
    
    return b
}

// So sánh hiệu năng
print("Fibonacci(10) = " + tostring(fibonacci_lap(10)))  // Output: 55
print("Fibonacci(20) = " + tostring(fibonacci_lap(20)))  // Output: 6765
```

Giải thích:
- **Naive**: Tính lại cùng giá trị nhiều lần - rất chậm
- **Memoization**: Lưu kết quả đã tính - nhanh hơn
- **Lặp**: Không dùng đệ quy - nhanh nhất, bộ nhớ ít nhất

---

## 4. DANH SÁCH VÀ CẤU TRÚC DỮ LIỆU

### 4.1 Ngăn Xếp (Stack)

```lyra
var stack: [str]

proc push(gia_tri: str) {
    insert(stack, gia_tri)
}

proc pop() -> str {
    if length(stack) == 0 {
        return ""  // Stack rỗng
    }
    var gia_tri = stack[length(stack) - 1]
    // Xóa phần tử cuối cùng (không có hàm remove tích hợp)
    return gia_tri
}

proc top() -> str {
    if length(stack) == 0 {
        return ""
    }
    return stack[length(stack) - 1]
}

proc is_empty() -> bool {
    return length(stack) == 0
}

// Ví dụ: Kiểm tra cân bằng dấu ngoặc
proc kiem_tra_dau_ngoac(bieu_thuc: str) -> bool {
    var stack_ngoac: [str]
    var i = 0
    
    while i < length(bieu_thuc) {
        var ky_tu = substr(bieu_thuc, i, 1)
        
        if ky_tu == "(" {
            insert(stack_ngoac, "(")
        }
        else if ky_tu == ")" {
            if length(stack_ngoac) == 0 {
                return false  // Có dấu đóng nhưng không có mở
            }
            // Pop
            // Ở đây ta cần xóa phần tử cuối
        }
        
        i = i + 1
    }
    
    return length(stack_ngoac) == 0  // Phải rỗng ở cuối
}
```

---

## 5. XỬ LÝ XÂUKY TỰ NÂNG CAO

### 5.1 Kiểm Tra Palindrome

```lyra
proc la_palindrome(xau: str) -> bool {
    var n = length(xau)
    var trai = 0
    var phai = n - 1
    
    while trai < phai {
        if substr(xau, trai, 1) != substr(xau, phai, 1) {
            return false
        }
        trai = trai + 1
        phai = phai - 1
    }
    
    return true
}

// Sử dụng
var test1 = "racecar"
var test2 = "hello"

if la_palindrome(test1) {
    print(test1 + " là palindrome")  // Output: racecar là palindrome
}

if !la_palindrome(test2) {
    print(test2 + " không phải palindrome")  // Output
}
```

Giải thích:
- **Palindrome**: Xâu đọc từ trái sang phải bằng đọc từ phải sang trái
- Ví dụ: "racecar", "madam", "12321"

### 5.2 Đếm Ký Tự

```lyra
proc dem_tan_suat_ky_tu(xau: str) -> [str] {
    var ket_qua: [str]
    var i = 0
    
    while i < length(xau) {
        var ky_tu = substr(xau, i, 1)
        var j = 0
        var tim_thay = false
        
        // Tìm xem ký tự đã có trong kết quả chưa
        while j < length(ket_qua) {
            if substr(ket_qua[j], 0, 1) == ky_tu {
                // Tìm thấy, tăng đếm
                tim_thay = true
                break
            }
            j = j + 1
        }
        
        if !tim_thay {
            // Chưa có, thêm mới
            insert(ket_qua, ky_tu + ":1")
        }
        
        i = i + 1
    }
    
    return ket_qua
}

// Sử dụng
var xau_test = "hello"
var tan_suat = dem_tan_suat_ky_tu(xau_test)

var k = 0
while k < length(tan_suat) {
    print("Ký tự: " + tan_suat[k])
    k = k + 1
}
```

---

## 6. GIẢI QUYẾTVấn ĐỀ TOÁN HỌC

### 6.1 GCD (Ước Chung Lớn Nhất)

```lyra
proc gcd(a: i32, b: i32) -> i32 {
    while b != 0 {
        var temp = b
        b = a % b
        a = temp
    }
    return a
}

// Sử dụng
var x = 48
var y = 18
var uc_chung = gcd(x, y)
print("GCD(" + tostring(x) + ", " + tostring(y) + ") = " + tostring(uc_chung))
// Output: GCD(48, 18) = 6
```

Giải thích:
- **GCD**: Ước chung lớn nhất của hai số
- **Thuật toán Euclidean**: Sử dụng phép chia dư lặp lại
- Công thức: gcd(a, b) = gcd(b, a % b)

### 6.2 LCM (Bội Chung Nhỏ Nhất)

```lyra
proc lcm(a: i32, b: i32) -> i32 {
    return (a * b) / gcd(a, b)
}

// Sử dụng
var p = 12
var q = 18
var bc_chung = lcm(p, q)
print("LCM(" + tostring(p) + ", " + tostring(q) + ") = " + tostring(bc_chung))
// Output: LCM(12, 18) = 36
```

---

## 7. MATRIX VÀ MẢNG 2 CHIỀU

### 7.1 Phép Nhân Ma Trận

```lyra
proc nhan_ma_tran(a: [i32], b: [i32], hang_a: i32, cot_a: i32, cot_b: i32) -> [i32] {
    var ket_qua: [i32]
    var i = 0
    
    while i < hang_a {
        var j = 0
        while j < cot_b {
            var tong = 0
            var k = 0
            
            while k < cot_a {
                var phan_tu_a = a[i * cot_a + k]
                var phan_tu_b = b[k * cot_b + j]
                tong = tong + (phan_tu_a * phan_tu_b)
                k = k + 1
            }
            
            insert(ket_qua, tong)
            j = j + 1
        }
        i = i + 1
    }
    
    return ket_qua
}

// Sử dụng: Ma trận 2x3 nhân 3x2
// A = [1 2 3]    B = [7 8]
//     [4 5 6]        [9 10]
//                    [11 12]
// Kết quả = [58 64]
//           [139 154]

var ma_tran_a = [1, 2, 3, 4, 5, 6]
var ma_tran_b = [7, 8, 9, 10, 11, 12]

var tich = nhan_ma_tran(ma_tran_a, ma_tran_b, 2, 3, 2)

print("Kết quả phép nhân ma trận:")
var m = 0
while m < length(tich) {
    print(tostring(tich[m]))
    m = m + 1
}
```

---

## 8. TỐI ƯU HÓA VÀ HIỆU NĂNG

### 8.1 So Sánh Hiệu Năng

```lyra
proc benchmark_so_sanh() {
    var n = 1000
    
    // Test 1: Vòng lặp đơn giản
    var ket_qua_1 = 0
    var i = 0
    while i < n {
        ket_qua_1 = ket_qua_1 + i
        i = i + 1
    }
    print("Vòng lặp đơn: " + tostring(ket_qua_1))
    
    // Test 2: Vòng lặp lồng (chậm hơn)
    var ket_qua_2 = 0
    var j = 0
    while j < 100 {
        var k = 0
        while k < 100 {
            ket_qua_2 = ket_qua_2 + 1
            k = k + 1
        }
        j = j + 1
    }
    print("Vòng lặp lồng: " + tostring(ket_qua_2))
}

benchmark_so_sanh()
```

---

## 9. KIỂM THỬ VÀ XÁC THỰC

### 9.1 Test Cases

```lyra
proc test_cong() {
    var ket_qua = 2 + 3
    if ket_qua == 5 {
        print("Test cong: PASSED")
    }
    else {
        print("Test cong: FAILED")
    }
}

proc test_tru() {
    var ket_qua = 5 - 3
    if ket_qua == 2 {
        print("Test tru: PASSED")
    }
    else {
        print("Test tru: FAILED")
    }
}

proc test_nhan() {
    var ket_qua = 4 * 5
    if ket_qua == 20 {
        print("Test nhan: PASSED")
    }
    else {
        print("Test nhan: FAILED")
    }
}

proc chay_tat_ca_test() {
    print("Chạy test suite...")
    test_cong()
    test_tru()
    test_nhan()
    print("Xong")
}

chay_tat_ca_test()
```

---

## 10. ĐIỀU CHỈNH VÀ CÁCH GIẢI QUYẾT

### 10.1 Kiểm Tra Điều Kiện Ranh Giới

```lyra
proc xo_ly_mang(mang: [i32]) {
    // Kiểm tra mảng rỗng
    if length(mang) == 0 {
        print("Cảnh báo: Mảng rỗng")
        return
    }
    
    // Kiểm tra một phần tử
    if length(mang) == 1 {
        print("Mảng có một phần tử: " + tostring(mang[0]))
        return
    }
    
    // Xử lý bình thường
    var i = 0
    while i < length(mang) {
        print("Phần tử " + tostring(i) + ": " + tostring(mang[i]))
        i = i + 1
    }
}

// Test
var mang_test = [10, 20, 30]
xo_ly_mang(mang_test)
```

---

## KẾT LUẬN

Các ví dụ nâng cao này giúp bạn:
- Hiểu rõ các thuật toán phổ biến
- Viết mã hiệu quả hơn
- Tối ưu hóa hiệu năng
- Xử lý các tình huống phức tạp

Để tìm hiểu thêm:
- Xem `01_HUONG_DAN_LAP_TRIN.md` cho cơ bản
- Xem `02_TAI_LIEU_THAM_KHAO_API.md` cho API
- Xem `04_XU_LY_LOI.md` cho xử lý lỗi
