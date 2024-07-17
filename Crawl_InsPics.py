import instaloader
#pip install instaloader
# Tạo một đối tượng Instaloader
L = instaloader.Instaloader()

# Tải toàn bộ ảnh từ tài khoản Instagram
profile_name = input("Nhap ten TK: ")
L.download_profile(profile_name, profile_pic_only=False)