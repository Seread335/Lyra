# HƯỚNG DẪN CÀI ĐẶT VÀ NÂNG CẬP - LYRA NNLT v2.3.22.1

## Mục Đích

Tài liệu này hướng dẫn cài đặt, cấu hình, và nâng cấp Lyra NNLT.

---

## PHẦN 1: YÊUVẬT KỸ THUẬT

### 1.1 Yêu Cầu Hệ Thống

#### Tối Thiểu (Chạy cơ bản)
```
CPU:    Intel/AMD 1GHz+
RAM:    512 MB
Đĩa:    100 MB không gian trống
OS:     Windows 7+, macOS 10.9+, Linux (bất kỳ distro)
```

#### Khuyến Nghị (Hiệu suất tốt)
```
CPU:    Intel Core i3/AMD Ryzen 3 trở lên
RAM:    2 GB trở lên
Đĩa:    500 MB không gian trống SSD
OS:     Windows 10+, macOS 10.14+, Linux mới
Python: 3.7+ (nếu chạy từ source)
```

#### Tối Ưu (Hiệu suất cao)
```
CPU:    Intel Core i5/AMD Ryzen 5 trở lên
RAM:    4 GB trở lên
Đĩa:    1 GB SSD
OS:     Windows 10/11, macOS 11+, Linux mới
JIT:    Bật để tối ưu tốc độ
```

---

### 1.2 Phần Mềm Tiên Quyết

**Bắt Buộc:**
- Hệ điều hành tương thích

**Tùy Chọn (để phát triển):**
- Python 3.7+
- Trình soạn thảo (VS Code, Sublime, vv)
- Git (để cập nhật từ repository)

---

## PHẦN 2: CÀI ĐẶT

### 2.1 Trên Windows

#### Cách 1: Sử Dụng Installer (Dễ Nhất)

1. **Tải xuống**:
   - Vào `installers/lyra_distribution/`
   - Tải file `install_lyra.bat`

2. **Chạy Installer**:
   - Nhấp đúp `install_lyra.bat`
   - Hoặc mở Command Prompt:
   ```cmd
   cd C:\Đường\dẫn\Lyra_NNLT
   install_lyra.bat
   ```

3. **Kiểm Tra Cài Đặt**:
   ```cmd
   lyra --version
   ```

4. **Chạy Chương Trình Đầu Tiên**:
   ```cmd
   lyra examples/simple_arithmetic.lyra
   ```

#### Cách 2: Cài Đặt Thủ Công

1. **Tải Mã Nguồn**:
   - Tải từ GitHub hoặc bản phân phối

2. **Sao Chép Các Tệp**:
   ```cmd
   xcopy lyra_interpreter C:\Program Files\Lyra /E /I
   ```

3. **Thêm Vào PATH**:
   - Nhấn Win + X, chọn "System"
   - Vào "Environment Variables"
   - Thêm `C:\Program Files\Lyra\src` vào PATH

4. **Kiểm Tra**:
   ```cmd
   lyra --help
   ```

---

### 2.2 Trên macOS / Linux

#### Cách 1: Sử Dụng Installer Script (Dễ Nhất)

1. **Tải xuống**:
   - Vào `installers/lyra_distribution/`
   - Tải file `install_lyra.sh`

2. **Chạy Installer**:
   ```bash
   cd /đường/dẫn/Lyra_NNLT
   chmod +x install_lyra.sh
   ./install_lyra.sh
   ```

3. **Kiểm Tra Cài Đặt**:
   ```bash
   lyra --version
   ```

4. **Chạy Chương Trình Đầu Tiên**:
   ```bash
   lyra examples/simple_arithmetic.lyra
   ```

#### Cách 2: Cài Đặt Thủ Công

1. **Sao Chép Các Tệp**:
   ```bash
   sudo cp -r lyra_interpreter /usr/local/lyra
   ```

2. **Tạo Liên Kết**:
   ```bash
   sudo ln -s /usr/local/lyra/src/lyra /usr/local/bin/lyra
   ```

3. **Kiểm Tra**:
   ```bash
   lyra --help
   ```

---

### 2.3 Cài Đặt Từ Source

#### Trên Tất Cả Nền Tảng

1. **Yêu Cầu**:
   ```
   Python 3.7+
   Git
   ```

2. **Tải Mã Nguồn**:
   ```bash
   git clone https://github.com/lyra-nnlt/lyra.git
   cd lyra
   ```

3. **Cài Đặt Phụ Thuộc** (nếu cần):
   ```bash
   pip install -r requirements.txt
   ```

4. **Kiểm Tra**:
   ```bash
   python lyra_interpreter/src/lyra/main.py --version
   ```

5. **Tạo Alias** (không bắt buộc):
   ```bash
   # Thêm vào ~/.bashrc hoặc ~/.zshrc
   alias lyra="python /đường/dẫn/lyra/lyra_interpreter/src/lyra/main.py"
   ```

---

## PHẦN 3: CẤU HÌNH SAU CÀI ĐẶT

### 3.1 Xác Minh Cài Đặt

1. **Kiểm Tra Phiên Bản**:
   ```bash
   lyra --version
   ```
   Kết quả mong đợi: `Lyra NNLT v2.3.22.1`

2. **Kiểm Tra Trợ Giúp**:
   ```bash
   lyra --help
   ```

3. **Chạy Ví Dụ**:
   ```bash
   lyra examples/simple_arithmetic.lyra
   ```
   Kết quả mong đợi: In ra kết quả tính toán

4. **Chạy REPL** (Interactive Shell):
   ```bash
   lyra
   ```
   Bạn sẽ thấy dấu nhắc: `> `

5. **Thoát REPL**:
   ```
   > exit
   ```

### 3.2 Cấu Hình Môi Trường

#### Biến Môi Trường (Tùy Chọn)

**Windows (Command Prompt)**:
```cmd
set LYRA_HOME=C:\Program Files\Lyra
set LYRA_DEBUG=1
```

**Linux/macOS (Bash)**:
```bash
export LYRA_HOME=/usr/local/lyra
export LYRA_DEBUG=1
```

Thêm vào tệp cấu hình vĩnh viễn:
- Windows: `Cài đặt hệ thống > Biến môi trường`
- Linux/macOS: Thêm vào `~/.bashrc` hoặc `~/.zshrc`

---

### 3.3 Cấu Hình Trình Soạn Thảo

#### VS Code

1. **Cài Đặt Extension**:
   - Mở VS Code
   - Vào Extensions (Ctrl+Shift+X)
   - Tìm "Lyra NNLT"
   - Nhấn "Install"

2. **Xác Nhận Cài Đặt**:
   - Tạo tệp `test.lyra`
   - Bạn sẽ thấy syntax highlighting

3. **Chạy Code**:
   - Mở tệp `.lyra`
   - Nhấn Ctrl+Shift+D
   - Hoặc dùng terminal: `lyra test.lyra`

#### Sublime Text

1. **Cài Đặt Package**:
   - Bạn có thể cấu hình thủ công (xem `lyra-language-extension/`)

2. **Cấu Hình Syntax**:
   - Sao chép `lyra-language-extension/syntaxes/` vào Sublime

#### Các Trình Soạn Thảo Khác

- Tính năng khôi phục: Chỉnh sửa `.lyra` với các lệnh cơ bản
- Không cần cài đặt nếu chỉ muốn soạn thảo

---

## PHẦN 4: NÂNG CẬP

### 4.1 Kiểm Tra Phiên Bản Hiện Tại

```bash
lyra --version
```

### 4.2 Nâng Cấp Từ v2.3.22 Hoặc Cũ Hơn

#### Cách 1: Sử Dụng Installer (Đơn Giản Nhất)

1. **Tải Installer Mới**:
   - Vào `installers/lyra_distribution/`
   - Tải `install_lyra.bat` (Windows) hoặc `install_lyra.sh` (Linux/Mac)

2. **Chạy Installer**:
   ```bash
   # Linux/Mac
   chmod +x install_lyra.sh
   ./install_lyra.sh
   
   # Windows
   install_lyra.bat
   ```

3. **Gỡ Cài Đặt Cũ** (Tùy Chọn):
   ```bash
   # Linux/Mac
   sudo rm -rf /usr/local/lyra
   
   # Windows
   rmdir /s C:\Program Files\Lyra
   ```

4. **Kiểm Tra**:
   ```bash
   lyra --version
   # Kết quả: Lyra NNLT v2.3.22.1
   ```

#### Cách 2: Nâng Cấp Thủ Công

1. **Sao Lưu Cấu Hình Cũ** (Tùy Chọn):
   ```bash
   cp -r ~/.lyra ~/.lyra.backup
   ```

2. **Tải Phiên Bản Mới**:
   - Từ GitHub hoặc bản phân phối

3. **Thay Thế Tệp**:
   ```bash
   # Linux/Mac
   sudo cp -r lyra_interpreter /usr/local/lyra
   
   # Windows
   xcopy lyra_interpreter C:\Program Files\Lyra /E /I /Y
   ```

4. **Kiểm Tra Tương Thích**:
   ```bash
   lyra examples/simple_arithmetic.lyra
   ```

### 4.3 Nâng Cấp Từ Phiên Bản Rất Cũ

Nếu bạn nâng cấp từ v2.0 hoặc cũ hơn, hãy kiểm tra:

1. **Thay Đổi Cú Pháp**:
   - v2.3.22.1 tương thích ngược với v2.3.x
   - Có thể cần điều chỉnh cho v2.0.x

2. **Kiểm Tra CHANGELOG**:
   - Xem `CHANGELOG_v2.3.22.1.md`
   - Tìm các thay đổi phá vỡ (breaking changes)

3. **Cập Nhật Code**:
   - Sử dụng ví dụ mới trong `examples/`
   - Kiểm tra từng hàm có còn khả dụng

---

## PHẦN 5: GỠ CÀI ĐẶT

### 5.1 Gỡ Trên Windows

#### Cách 1: Thông Qua Control Panel
1. Mở Control Panel
2. Vào "Programs and Features"
3. Tìm "Lyra NNLT"
4. Nhấn "Uninstall"

#### Cách 2: Thủ Công
```cmd
rmdir /s C:\Program Files\Lyra
```

### 5.2 Gỡ Trên Linux/macOS

```bash
# Gỡ thực thi
sudo rm /usr/local/bin/lyra

# Gỡ thư mục cài đặt
sudo rm -rf /usr/local/lyra

# Gỡ tệp cấu hình (Tùy Chọn)
rm -rf ~/.lyra
```

---

## PHẦN 6: KHẮC PHỤC SỰ CỐ CÀI ĐẶT

### 6.1 "Lệnh lyra Không Tìm Thấy"

**Windows:**
```cmd
# Kiểm tra PATH
echo %PATH%

# Thêm thủ công vào PATH (nếu cần)
set PATH=%PATH%;C:\Program Files\Lyra\src
```

**Linux/macOS:**
```bash
# Kiểm tra PATH
echo $PATH

# Tạo liên kết
sudo ln -s /usr/local/lyra/src/lyra /usr/local/bin/lyra
```

### 6.2 "Lỗi Cấp Quyền" (Linux/macOS)

```bash
# Cho phép thực thi
chmod +x install_lyra.sh

# Hoặc sử dụng sudo
sudo ./install_lyra.sh
```

### 6.3 "Tệp Python Không Tìm Thấy"

Nếu chạy từ source:

```bash
# Kiểm tra Python
python --version
python3 --version

# Sử dụng đường dẫn đầy đủ
python3 /đường/dẫn/lyra_interpreter/src/lyra/main.py
```

### 6.4 "Không Thể Tìm Thấy Thư Viện"

```bash
# Cài đặt phụ thuộc
pip install -r requirements.txt

# Hoặc cài đặt từng gói
pip install [tên_gói]
```

### 6.5 "Lỗi Khi Chạy Ví Dụ"

1. **Kiểm Tra Đường Dẫn**:
   ```bash
   cd /đường/dẫn/Lyra_NNLT
   lyra examples/simple_arithmetic.lyra
   ```

2. **Kiểm Tra Quyền**:
   ```bash
   ls -la examples/simple_arithmetic.lyra
   chmod +r examples/simple_arithmetic.lyra
   ```

3. **Kiểm Tra Mã Unicode**:
   - Nếu lỗi liên quan đến mã hóa
   - Đảm bảo tệp là UTF-8

---

## PHẦN 7: CẬP NHẬT TỰ ĐỘNG (TÙY CHỌN)

### 7.1 Kiểm Tra Cập Nhật

```bash
lyra --check-updates
```

### 7.2 Cập Nhật Tự Động

Nếu hỗ trợ (phiên bản tương lai):

```bash
lyra --auto-update
```

---

## PHẦN 8: KIỂM THỬCÀI ĐẶT TOÀN BỘ

Chạy bộ thử nghiệm cài đặt:

```bash
# 1. Kiểm tra phiên bản
lyra --version

# 2. Chạy REPL (gõ: exit để thoát)
lyra

# 3. Chạy ví dụ đơn giản
lyra examples/simple_arithmetic.lyra

# 4. Chạy ví dụ phức tạp
lyra examples/fibonacci.lyra

# 5. Chạy bộ kiểm thử
lyra examples/run_tests.lyra
```

Nếu tất cả 5 bước thành công, cài đặt là hoàn chỉnh.

---

## PHẦN 9: CHẠY CHƯƠNG TRÌNH LẦN ĐẦU

### 9.1 Chạy File Lyra

```bash
lyra tên_file.lyra
```

### 9.2 Chạy Tương Tác (REPL)

```bash
lyra
```

Bạn sẽ thấy:
```
Lyra NNLT v2.3.22.1
Type 'exit' to quit

>
```

Nhập code và nhấn Enter:
```
> var x = 10
> var y = 20
> print(tostring(x + y))
30
```

### 9.3 Chạy Với Tuỳ Chọn

```bash
lyra --debug tên_file.lyra          # Chạy với gỡ lỗi
lyra --optimize tên_file.lyra       # Bật tối ưu hóa
lyra --benchmark tên_file.lyra      # Chạy benchmark
```

---

## PHẦN 10: DANH SÁCH KIỂM TRA CÀI ĐẶT

- [ ] Tải xuống phiên bản v2.3.22.1
- [ ] Chạy installer hoặc cài đặt thủ công
- [ ] Kiểm tra PATH hoặc biến môi trường
- [ ] Chạy `lyra --version` thành công
- [ ] Chạy ví dụ đơn giản thành công
- [ ] Cấu hình trình soạn thảo (tùy chọn)
- [ ] Chạy `lyra` vào REPL (tùy chọn)
- [ ] Tạo tệp `.lyra` đầu tiên của bạn

---

## DANH SÁCH LỆNH NHANH

```bash
# === CÀI ĐẶT ===
# Windows
install_lyra.bat

# Linux/macOS
./install_lyra.sh

# === KIỂM TRA ===
lyra --version
lyra --help

# === CHẠY ===
lyra tên_file.lyra
lyra                          # REPL

# === GỠ ===
# Windows: Control Panel > Programs and Features
# Linux/macOS: sudo rm -rf /usr/local/lyra

# === CẬP NHẬT ===
# Tải bản mới và chạy installer
```

---

## KẾT LUẬN

Bây giờ bạn đã có:
✅ Lyra NNLT v2.3.22.1 được cài đặt
✅ Các ví dụ chạy thành công
✅ Trình soạn thảo được cấu hình (nếu muốn)

Bước tiếp theo:
- Xem `01_HUONG_DAN_LAP_TRIN.md` để học cú pháp
- Xem `02_TAI_LIEU_THAM_KHAO_API.md` để tìm hiểu các hàm
- Xem `03_VI_DU_NANG_CAO.md` cho ví dụ nâng cao
- Xem `04_XU_LY_LOI.md` để xử lý lỗi
- Xem `05_CAU_HOI_THUONG_GAP.md` cho FAQ
