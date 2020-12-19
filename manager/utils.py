import os
import json
from datetime import datetime, timedelta
import re

def read_config():
    with open(os.path.dirname(os.path.realpath(__file__)) + '/../config.json', 'r') as _config_file:
        return json.load(_config_file)

def get_date(delta):
    """
    오늘부터 delta만큼의 날짜를 반환
    """
    date = (datetime.today() + timedelta(days=delta)).strftime('%Y%m%d')
    return date

def filter_text(text, hangeul=True, digit=True):
    """
    한글 또는 숫자로 이루어진 데이터만 반환한다.
    """
    h_exp = re.compile('[^가-힣]+')
    d_exp = re.compile('[^0-9]+')

    if hangeul:
        text = h_exp.sub('', text)
    if digit:
        text = d_exp.sub('', text)
    return text


REASON_CODE = {
    '장내매수': '01',
    '장내매도': '02',
    '장외매도': '03',
    '장외매수': '04',
    '신규상장': '05',
    '신규선임': '06',
    '신규보고': '07',
    '합병': '08',
    '인수': '09',
    '증여': '10',
    '무상신주취득': '11',
    '유상신주취득': '12',
    '주식매수선택권': '13',
    '풋옵션권리행사에따른주식처분': '14',
    'CB인수': '15',
    '시간외매매': '16',
    '전환등': '17',
    '전환사채의권리행사': '18',
    '수증': '19',
    '행사가액조정': '20',
    '기타': '99'
}

STOCK_TYPE_CODE = {
    '보통주': '01',
    '우선주': '02',
    '전환사채권': '03',
    '신주인수권이표시된것': '04',
    '신주인수권부사채권': '05'
}
