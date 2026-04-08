import requests
import json
import os

def get_movie_links(movie_slug):
    url = f"https://ophim1.com/phim/{movie_slug}"
    print(f"Đang fetch dữ liệu từ: {url}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if not data.get('status'):
            print(f"Lỗi: {data.get('msg', 'Không tìm thấy phim')}")
            return
        
        movie_name = data['movie']['slug']
        episodes_list = data.get('episodes', [])
        
        if not episodes_list:
            print("Không tìm thấy tập phim nào.")
            return
        
        # Lấy server đầu tiên (thông thường là Vietsub)
        server = episodes_list[0]
        server_data = server.get('server_data', [])
        
        # Sắp xếp theo thứ tự tập phim
        # Cố gắng chuyển name sang số để sort chính xác (1, 2, ..., 10 thay vì 1, 10, 2)
        def sort_key(ep):
            name = ep.get('name', '0')
            try:
                return float(name)
            except ValueError:
                # Nếu là "SP" hoặc các ký tự khác, đẩy xuống cuối
                return float('inf')

        sorted_episodes = sorted(server_data, key=sort_key)
        
        filename = f"{movie_slug}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            for ep in sorted_episodes:
                link = ep.get('link_m3u8')
                if link:
                    f.write(f"{link}\n")
        
        print(f"Đã lưu {len(sorted_episodes)} tập phim vào file: {filename}")
        
    except requests.exceptions.RequestException as e:
        print(f"Lỗi kết nối: {e}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    slug = input("Nhập tên phim (slug, ví dụ: ninh-an-nhu-mong): ").strip()
    if slug:
        get_movie_links(slug)
    else:
        print("Vui lòng nhập slug phim.")
