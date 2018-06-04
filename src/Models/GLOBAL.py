# HEADERS
# JSON_LAPTOPS
DOMAIN = r'https://www3.lenovo.com'
UNDEFINED = r'undefined'


HEADERS = [
    r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
    r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0',
    r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 OPR/44.0.2510.857 (Edition Baidu)',
]

JSON_LAPTOPS = {
    "JP": r"https://www3.lenovo.com/jp/ja/c/products/json?categoryCodes=thinkpad-x-series%2Cthinkpad-yoga-series%2Cthinkpad-a-series%2Cthinkpad-t-series%2Cthinkpad-e-series%2Cthinkpad-l-series%2Cthinkpad-p-series%2Clenovo-v-series%2Clenovo-N-series%2Cideapad-700-series%2Cideapad-500-series%2Cideapad-300-series%2Cideapad-300s-series%2Cideapad-100-series%2Cideapad-100s-series%2Cideapad-legion-y-series%2Cyoga-book%2Cyoga-900-series%2Cyoga-700-series%2Cyoga-300-series",
    "KR": r"https://www3.lenovo.com/kr/ko/c/products/json?categoryCodes=thinkpad-x-series%2Cthinkpad-t-series%2Cthinkpad-l-series%2Cthinkpad-e-series%2Cthinkpad-p-series%2Cideapad-100-series%2Cideapad-300-series%2Cideapad-500-series%2Cideapad-700-series%2Clegion-y-series%2Cideapad-miix-series%2Clenovo-v-series%2Clenovo-yoga-series",
    "MY": r"https://www3.lenovo.com/my/en/c/products/json?categoryCodes=thinkpad-x-series%2Cthinkpad-t-series%2Cthinkpad-e-series%2Cthinkpad-l-series%2Cthinkpad-yoga-series%2Cthinkpad-p-series%2Cthinkpad-a-series%2Cideapad-100-series%2Cideapad-300-series%2Cideapad-300s-series%2Cideapad-500-series%2Cideapad-500s-series%2Cideapad-700-series%2Cideapad-miix-series%2CLegion-y-Series%2Cyoga-500-series%2Cyoga-700-series%2Cyoga-900-series",
    "HK": r"https://www3.lenovo.com/hk/zf/c/products/json?categoryCodes=thinkpad-x-series%2Cthinkpad-t-series%2Cthinkpad-e-series%2Cthinkpad-l-series%2Cthinkpad-p-series%2Cthinkpad-a-series%2Cthinkpad-13-series%2Cthinkpad-yoga-series%2Clenovo-yoga-series%2Clenovo-v-series%2Cideapad-700-series%2Cideapad-500-series%2Cideapad-300-series%2Cideapad-100-series%2Cideapad-500s-series%2CIdeapad+300s%2Cideapad-miix-series%2Clegion-y-series%2Cyoga-900-series%2Cyoga-700-series%2Cyoga-500-series%2Cyoga-300-series",
    "SG": r"https://www3.lenovo.com/sg/en/c/products/json?categoryCodes=thinkpad-13-series%2Cthinkpad-x-series%2Cthinkpad-t-series%2Cthinkpad-e-series%2Cthinkpad-l-series%2Cthinkpad-a-series%2Cthinkpad-yoga-series%2Cthinkpad-p-series%2Cideapad-300-series%2CIdeapad-300s%2Cideapad-500-series%2Cideapad-500s-series%2Cideapad-700-series%2Cideapad-miix-series%2Clegion-y-series%2Clenovo-v-series%2Cyoga-500-series%2Cyoga-700-series%2Cyoga-900-series",
    "TW": r"https://www3.lenovo.com/tw/zh/c/products/json?categoryCodes=thinkpad-x-series%2Cthinkpad-t-series%2Cthinkpad-p-series%2Cthinkpad-yoga-series%2Cthinkpad-13-series%2Cthinkpad-e-series%2Cthinkpad-l-series%2Cthinkpad-a-series%2Cideapad-100-series%2Cideapad-300-series%2Cideapad-500-series%2Cideapad-700-series%2Clegion-y-series%2Cideapad-miix-series%2C300-series%2Cyoga-500-series%2C700-series%2C900-series%2Cyoga-book-series%2Clenovo-yoga-series%2Clenovogseries%2Clenovo-b-series%2Clenovo-v-series",
    "TH": r"https://www3.lenovo.com/th/th/c/products/json?categoryCodes=thinkpad-x-series%2Cthinkpad-t-series%2Cthinkpad-e-series%2Clenovo-yoga-series%2Clenovo-g-series%2Cideapad-300-series%2Cideapad-300s-series%2Cideapad-500-series%2Cideapad-500s-series%2Cideapad-700-series%2Cideapad-miix-series%2CLegion-y-Series%2Cyoga-500-series%2Cyoga-700-series%2Cyoga-900-series",
    "ID": r"https://www3.lenovo.com/id/in/c/products/json?categoryCodes=thinkpad-p-series%2Clenovo-yoga-series%2Clenovo-m-series%2Clenovo-v-series%2Cideapad-100-series%2Cideapad-300-series%2Cideapad-300s-series%2Cideapad-500-series%2Cideapad-500s-series%2Cideapad-700-series%2Cideapad-y900-series%2CLegion-y-Series%2Cyoga-500-series%2Cyoga-900-series",
    "PH": r"https://www3.lenovo.com/ph/en/c/products/json?categoryCodes=thinkpad-x-series%2Cthinkpad-t-series%2Cthinkpad-e-series%2Cthinkpad-yoga-series%2Cthinkpad-p-series%2Clenovo-yoga-series%2Cideapad-100-series%2Cideapad-300-series%2Cideapad-500-series%2Cideapad-700-series%2Cideapad-y700-series%2Cideapad-miix-series%2CLegion-y-Series%2Cyoga-300-series%2Cyoga-500-series%2Cyoga-700-series%2Cyoga-900-series",
    "MM": r"https://www3.lenovo.com/mm/en/c/products/json?categoryCodes=thinkpad-x-series%2Cthinkpad-t-series%2Cthinkpad-e-series%2Cthinkpad-yoga-series%2Cthinkpad-p-series%2Clenovo-yoga-series%2Cideapad-100-series%2Cideapad-300-series%2Cideapad-500-series%2Cideapad-700-series%2Cideapad-y700-series%2Cideapad-miix-series%2CLegion-y-Series%2Cyoga-300-series%2Cyoga-500-series%2Cyoga-700-series%2Cyoga-900-series",
    "VN": r"https://www3.lenovo.com/vn/vn/c/products/json?categoryCodes=thinkpad-x-series%2Cthinkpad-t-series%2Cthinkpad-e-series%2Cthinkpad-p-series%2Cthinkpad-11e-series%2Cthinkpad-13-series%2Cthinkpad-a-series%2Clenovo-yoga-series%2Clenovo-v-series%2Cideapad-100-series%2Cideapad-300-series%2Cideapad-300s-series%2Cideapad-500-series%2Cideapad-500s-series%2Cideapad-700-series%2CLegion-y-Series%2Cyoga-500-series%2Cyoga-700-series%2Cyoga-900-series"
}
