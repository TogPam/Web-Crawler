import requests

for x in range(51019000, 51019500):
#x = input("Nhập số báo danh: ")
	url = "https://dantri.com.vn/thpt/1/0/99/"+ str(x) +"/2024/0.2/search-gradle.htm"
	payload = {}
	headers = {}
	response = requests.request("GET", url, headers = headers, data = payload)
	info = response.json()['student']
	diem = "SBD: {} Toan: {} Van: {} Anh: {} Li: {} Hoa: {} Sinh: {} TBKHTN: {} Su: {} Dia: {} GDCD: {} TBKHXH: {}".format(
		info['sbd'],info['toan'],info['van'],info['ngoaiNgu'],info['vatLy'],info['hoaHoc'],info['sinhHoc'],
		info['diemTBTuNhien'],info['lichSu'],info['diaLy'],info['gdcd'],info['diemTBXaHoi'],)
	diemthi = str(diem)
	print(diemthi)