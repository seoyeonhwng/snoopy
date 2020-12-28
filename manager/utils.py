import os
import json
from datetime import datetime, timedelta


def read_config():
    with open(os.path.dirname(os.path.realpath(__file__)) + '/../config.json', 'r') as _config_file:
        return json.load(_config_file)


def get_current_time(date_format=None, day_delta=None):
    today = datetime.utcnow() + timedelta(hours=9)

    if day_delta is not None:
        today += timedelta(days=day_delta)
    
    if date_format is None:
        return today
    return today.strftime(date_format)

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
    '공개매수': '21',
    '공개매수청약': '22',
    '교환': '23',
    '임원퇴임': '24',
    '신규주요주주': '25',
    '자사주상여금': '26',
    '계약기간만료': '27',
    '대물변제': '28',
    '대여': '29',
    '상속': '30',
    '수증취소': '31',
    '신고대량매매': '32',
    '신규등록': '33',
    '신주인수권사채의권리행사': '34',
    '실권주인수': '35',
    '실명전환': '36',
    '자본감소': '37',
    '전환권등소멸': '38',
    '제자배정유상증자': '39',
    '주식매수청구권행사': '40',
    '주식병합': '41',
    '주식분할': '42',
    '차입': '43',
    '콜옵션권리행사배정에따른주식처분': '44',
    '콜옵션권리행사에따른주식취득': '45',
    '피상속': '46',
    '회사분할': '47',
    '계약중도해지': '48',
    '계열사편입': '49',
    '교환사채의권리행사': '50',
    '담보주식처분권보유': '51',
    '대물변제수령': '52',
    '매출': '53',
    '상속포기': '54',
    '신주인수권증권의권리행사': '55',
    '우선주무배당': '56',
    '우선주배당': '57',
    '주식배당': '58',
    '주식소각': '59',
    '증여취소': '60',
    '출자전환': '61',
    '특별관계해소': '62',
    '풋옵션권리행사배정에따른주식취득': '63',
    '기타': '99'
}

STOCK_TYPE_CODE = {
    '보통주': '01',
    '우선주': '02',
    '전환사채권': '03',
    '신주인수권이표시된것': '04',
    '신주인수권부사채권': '05',
    '증권예탁증권': '06',
    '교환사채권': '07',
    '기타': '99'
}