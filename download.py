import requests

# URL of the file
url = "https://mosdac.gov.in/opendata/GSMaP_SAC_RAIN/2000/GPMMRG_MAP_0003010000_H_L3S_MCH_03F.h5"

# Your cookies (replace with the actual ones from DevTools)
cookies = {
    "mod_auth_openidc_session": "7b313a3d-03ff-461d-8592-b8fbeb0b4e71",
    "has_js": "1",
    "_pk_id.1.e0e7": "b7b5a8fa535dc026.1737384787.7.1738426503.1738426495."
}

# Headers (remove `If-Modified-Since` to force fresh download)
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
    "Referer": "https://mosdac.gov.in/opendata/GSMaP_SAC_RAIN/2000/",
    "Accept": "*/*",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "no-cache"  # Forces fresh request
}

# File save path
save_path = "GPMMRG_MAP_0003010000_H_L3S_MCH_03F.h5"

# Send GET request
response = requests.get(url, headers=headers, cookies=cookies, stream=True)

# Check response status
if response.status_code == 200:
    with open(save_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"File downloaded successfully: {save_path}")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
