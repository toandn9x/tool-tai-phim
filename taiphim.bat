@echo off
setlocal EnableDelayedExpansion

set /p "input_file=Nhập tên file chứa link (mặc định: links.txt): "
if "!input_file!"=="" set "input_file=links.txt"
set "output_dir=output"
set /a count=1

:: Tạo thư mục output nếu chưa tồn tại
if not exist "%output_dir%" mkdir "%output_dir%"

:: Đọc từng dòng trong file links.txt
for /f "tokens=*" %%i in (%input_file%) do (
    set "url=%%i"
    :: Đặt tên file theo thứ tự tap_1, tap_2, ...
    set "filename=tap_!count!"
    echo Đang tải: !url!
    
    :: Kiểm tra xem file đã tồn tại chưa
    if exist "%output_dir%\!filename!.mp4" (
        echo File !filename!.mp4 đã tồn tại, bỏ qua...
    ) else (
        :: Tải file bằng FFmpeg
        ffmpeg -i "!url!" -c copy -bsf:a aac_adtstoasc "%output_dir%\!filename!.mp4"
        if !errorlevel! equ 0 (
            echo Tải thành công: !filename!.mp4
        ) else (
            echo Lỗi khi tải: !url!
        )
    )
    :: Tăng số thứ tự
    set /a count+=1
)

echo Hoàn tất!
pause