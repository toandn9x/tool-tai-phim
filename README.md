# Tải Phim Ophim

Tải phim hàng loạt từ [Ophim](https://ophim1.com) bằng Python + FFmpeg. Gồm 2 bước: lấy link m3u8 từ API và tải video về máy.

## Yêu cầu

- **Python 3** + thư viện `requests`
- **FFmpeg**

### Cài đặt Python

**Windows:** Tải tại [python.org](https://www.python.org/downloads/), tích chọn **"Add Python to PATH"** khi cài.

**Linux:**

```bash
sudo apt install python3 python3-pip
```

Cài thư viện:

```bash
pip install requests
```

### Cài đặt FFmpeg

**Windows (Winget):**

```powershell
winget install ffmpeg
```

**Windows (Thủ công):** Tải tại [gyan.dev](https://www.gyan.dev/ffmpeg/builds/), giải nén và thêm thư mục `bin` vào PATH.

**Linux:**

```bash
sudo apt install ffmpeg
```

## Cách sử dụng

### Bước 1 — Lấy danh sách link m3u8

```bash
python main.py
```

Nhập slug phim khi được hỏi (ví dụ: `ninh-an-nhu-mong`). Script sẽ gọi API Ophim, lấy danh sách link m3u8 của tất cả các tập và lưu vào file `<slug>.txt`.

> Slug phim lấy từ URL trên Ophim, ví dụ: `https://ophim1.com/phim/ninh-an-nhu-mong` → slug là `ninh-an-nhu-mong`

### Bước 2 — Tải phim về máy

```bash
taiphim.bat
```

Script sẽ hỏi tên file chứa link (nhấn Enter để dùng mặc định `links.txt`). Video được tải vào thư mục `output/` với tên `tap_1.mp4`, `tap_2.mp4`, ...

Nếu file đã tồn tại sẽ tự động bỏ qua, không tải lại.

## Cấu trúc thư mục

```text
apiphim/
├── main.py          # Lấy link m3u8 từ API Ophim
├── taiphim.bat      # Tải video từ file link bằng FFmpeg
├── <slug>.txt       # File chứa danh sách link m3u8
└── output/          # Thư mục chứa video đã tải
    ├── tap_1.mp4
    ├── tap_2.mp4
    └── ...
```

## Lưu ý

- Sử dụng `-c copy` nên tốc độ tải nhanh, giữ nguyên chất lượng gốc 100%.
- Đảm bảo internet ổn định trong quá trình tải.
