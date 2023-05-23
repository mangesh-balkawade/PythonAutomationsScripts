# Modules Required

import requests
import bs4
from html_table_parser import HTMLTableParser
import pandas as pd
from pymongo import MongoClient

######################## Database Connection #######################

def get_database():

    # Mongo Atlas String
    CONNECTION_STRING = "mongodb+srv://marvellous:marvellous@marvellous.ihqyjz4.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)

    # Database Name
    return client['DataOfDORAndStampRevenueFinal']

# function
# output : Collection Name
def get_Collection():
    dbname = get_database()
    # Collection Name
    collection_name = dbname["DeedDetails"]

    # Schema Of Collection
    data = {
        "Deed Details": {
            "Transaction": '',
            "Registered At": "",
            "Deed No": '',
            "Volume & Page No": '',
            "Date of Registration": "",
            "Date of Completion": "",
            "Date of Delivery": "",
            "Serial No": '',
            "Name & Address of the Party": [
                {
                    "Name": "",
                    "Address": "",
                    "Status": ""
                },
                {
                    "Name": "",
                    "Address": "",
                    "Status": ""
                }
            ],
            "Details of Property":
                [
                    {
                        "Property Location": "",
                        "Property Type & Transaction": "",
                        "Plot & Khatian No and Zone": "",
                        "Area of Property": ""
                    }
            ]
        }
    }

    collection_name.insert_many([data])
    return collection_name
############################################################################

collection_name = get_Collection()

url = "https://wbregistration.gov.in/(S(dm0hmq5sndrymlxnngfqsamo))/index/SearchBy_QueryNo_DeedNo.aspx"

payload='ctl00%24CPH%24RadioButtonList1=d&ctl00%24CPH%24DDL_Dist=20&ctl00%24CPH%24DDL_RO=02&ctl00%24CPH%24txt_deedno=00099&ctl00%24CPH%24txt_deed_year=2022&ctl00%24CPH%24txtCapcha=W4N4R7&ctl00%24CPH%24btnSubmitQuery=Submit&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=eCFSx0asCv1LSZRmMYO1pI7vwzRqk4hJB7FrjfIFCtIDSYkLhAWW3DUnAFoZGt2ExeKHkZzzbQVor6%2Be5Njp%2F5DmW4xEGfOUf8IJBexUHYCwV5IM1C%2BJdK9HXJWV522REP3BZiA4QmoqWt17ElHHkzGTVadzopzCyiW6Lzi%2FXlCmhbn4XfpmeTmvIFNljXKEZQIYI6t4YY00qLWZ%2Brk%2FDgs7TVciI6VdwVLHuEqw7uW2IyaOQTWxNn7u9l35lKWsglAtyMueHiuKBZwYTheFlI5H%2FSalSsKYGvSiwSWOfGGbV47WVp3VHKziZXtOCU3LTvczxXuiSiaasfHe%2BwLs5bXdZGnN7s2uOI1WxUUPa6W1JW1NrN0MBSfaE3Ww4cLFsbR4G1i3HVC3SokWnPDvRPfXJLFU%2BiKnK4CUAC%2BiOvW2GAQy0AqaDMOvQALrDl2ET1fuiH%2FAfYcHUnqv2347TzAS%2FZAb02OcXr%2BveAFKxEA%2FWdyWJ%2B2eGo0qxRC5jycPHSP16cZOt4zY3bI%2FWMvEdUhuk4aG4X4x3K%2FDSyKDlYajqqz084AqIxDEqTpeChWtVJx%2B%2FObgTmvsMDtajhyAJWYfkIHCdpVP%2Bq1BNYsYUrci358jHD%2FiKka5l5tEJukNb79BFE7OZnq8wcaSj%2FySfAJACiKKDNDijrYLNcDh6WCYcyAvfNieCvVpOZGN6f3PbXMsKTxMGc3vx4Yeg79KKzpKu%2Fzgha%2Byo35n9%2BUo6VfUOMDvNjm7KR51fdgw7UhIB1hpAtLffq0mXc0EL%2BAc9UJhTEpuTDaVgLLACJWqlxKE2sIGjJWfcElYZVEjLlPt%2FNRjiYuJBKEZ0pmcbjeVS1dwZP8niqCLhg3UamCkgvsWjzd8xjlk0E8x5kCL9RUHvHD3dNXAf3MzHLzWwSfz8Mh%2B4sGsGq4vydPFCsEobCwy%2BM5h21Wd4I6Yfv14krMYluXxZcTUv46njVm8GoRbpjO2Gmt%2FHVmSs45LrQrsfjZv59R8rkaoC%2BBGI9FRfDmX4ldX7eox%2FRptJDsc8qLJ%2FDVnhut23OhTLnJFs4SJ8UdbIeJ13lL0Lr1tYttUEbi9oJcYNre3UlDvIdHf5OXJ4EQxx7zSbcO9nuzdSHL2nGIUV6F4Xuu70IkxUA8iBRQrKqES%2B0s2CHpDfn5iQlqU5524vI20L05F6hd87kG21WOu1AQAoSWau0SqjsJ5XGWYcJ6KWEv10avL7IocKJE6Mr3tbzVA9GJ21bUN9bls%2FPf5BHDn3ltLV6sbG1%2BQu2wEiDm1%2BrR5xpUl4rA1MN7x1HnYFOVFmWY0STo9NGR2QqD5ROTF039TT%2FeZ5kCbe%2FP3aXcobAKeEN4nEM1F5nVLFT0XeispXQHtAECIFjeSR6UcVd5uJt3jd0GHm7k44yWVz0LEZ1pL05zjnq0Y7DBqtL6ctqFIhQFl4fHPlTexjRBW2F0WO1nslBXFSooiQ%2FSDfkIXlgdD%2FSzqzbOlrQUaBo9f7hQ9YjdQtJ%2B3lYTUMS569TT%2BaMIJB87nyKite59cEspbv1L%2BipQCxnP28nKa6gtC%2BZv2sMDlCDVeggJuE4LlnAXVGbUsdOYk004hnlyzjLMtOV3y1y2ONZS53dK0xPdZtr9wb8IZRysMbQteVr2%2FjmJiAdnTsZlBNupO7zWhHdkXhwH8hUezcdxKHSJfxMPcYzTdNqrhVSmRQJjjnK09KS6zb%2FdAUvlo6O0t0BSEkxumZ1FvF5Myd2aEqdmFPOK52MPOPE9F8lvPfIrhbcOQlv91LxDfZALDyoF4WnR3hPG2%2FV0rkI%2FPdce%2Fc8z0mORaxi98y7hML42EE006xnKgcZgNpJ2ulA4OKCGJrt9zsFrM8rzcaY8ZSG9SXym6gnCA7V3E4txmKBwuoxnaVCrSyxY0Ots9KMK1IrYgoVdL%2BtMz3vwXGn%2BTvp8JxuOklIxqChJEi%2BkeQa7VJB2nnGGpy%2FwUA%2FYaZOktQ93Era0gsG%2F7yabn0%2F80Ot7J0sm%2BIZ3XU0HO1ea61I9k5zY6zMn9pUO4MfC7OtTXKURN%2BfySpbBWfFiTD0fTPAjQOsRGY77GUnYU9KqBDde1lb7k0Po%3D&__VIEWSTATEGENERATOR=6012E183&__EVENTVALIDATION=gpoEdwbsJZ0oa%2FYkwCwiqsghKwBLrFmKnA6YWhvzmN2%2BZvYLWQGPFYl1obZxzQxXwgyZy9jhr6CTTtaLKKZfVDuvXNPoiTOhGophjVc4oLpRTqlbUjjgEgTY8egaN3toe%2BtKbs35B1%2BMA0dqibZ5KBwjJ1ablir9CesdAvVWiMGk%2Ft2waNJJRz4UjitdsKop9TUg%2B5w%2Bg8t3uWZFWFmZeLv1NPWm7GSWAvoZxZRQ9PgIoXjjYV8a1YR2TdsXh2AA9Oc7TVQ95mKXDsuRNGJA43FPjxzoeG33BFhdtawdLC1cu9TSqruUl97OPXab9RAMu2fiSX4V25pzLUtBfEXgIE04a6tPaB4EXLcmqqIMRUt4rqEUGPd68%2Bvv2F6Z%2BL6lJ7OnjtpatpQzlnyhhqRilbYbVWU1VCTKSJt5QkcvYnvYfwywtLR%2FejNKCqTL6gm9N5g1VQnScK2VtRv3WHd65aiNNlkkdOU0dxLFAM8CwhsCThLmPA1vZmhBX4HOfRZNEkgd2IQnMVBbUSJzvD6bll3rHia82jUtZ4xwGdUiLmg7Mj8ESJnEajYCZ6XEuUO9SGeaxMuKIdvRqRVhF0vV37z7ePFUZnNm%2BVbe0EGdamP%2Fpq22B7voV0G4ZdtSAEXsgcjBjWdh%2FwnO3VIJAUPjnc4yv%2Fhy5DLJ%2FZ20HP3nhO837MoXiu2FTBLEUFgdhGjrS6Piuu8g7Z%2Bk25fMW9z4WrVThwlh8qc1mK6gvieaUTJQVbzo9YmdS5oCyYzwPrTrCxySisftbn5pblFZ7MEEjWFpBbAEPBEVehl19LIEoLG7KZpV42gzAE0e0HWGIOnrk0VnQ8DLHspdhJZOW6p9DQqPkp2o43ItwR5Mb1BZKg57Y%2FkkzDbGRsk9QtHiBz%2BY&__VIEWSTATEENCRYPTED='

headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'regas_cookie=Regas_New1; regas_cookie=Regas_New1; regas_cookie=Regas_New1; regas_cookie=Regas_New1',
  'Origin': 'https://wbregistration.gov.in',
  'Referer': 'https://wbregistration.gov.in/(S(dm0hmq5sndrymlxnngfqsamo))/index/SearchBy_QueryNo_DeedNo.aspx',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"'
}

response = requests.request("POST", url, headers=headers, data=payload)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

################# Finding The Districts ############################

try:
    select_tag = soup.find('select')
    option_tags = select_tag.find_all('option')
except Exception:
    print("Unable to Send Post Request Due To Wrong Body Or Please Change ViewState And Other Fields In Payload")
    exit()

options = []
for i in option_tags:
    options.append(i.get('value'))

select_tag = soup.find('select')
option_tags = select_tag.find_all('option')
districts = []

for i in option_tags:
    districts.append(i.get('value'))
districts.remove('00')

##################################################################

#Set for Storing Only Unique Values in Database
uniqueData = set()

###################### Fetching The Data ########################

for district in districts:
    for regOff in range(2, 26):
        for deedNo in range(1, 101):
            for year in range(2021, 2023):
                try:
                    if (deedNo < 10):
                        deedNo = str('0000' + str(deedNo))
                    else:
                        deedNo = str('000' + str(deedNo))
                    if (regOff < 10):
                        regOff = str('0'+str(regOff))
                    if (district < 10):
                        district = '0'+str(district)

                    payload = f'ctl00%24CPH%24RadioButtonList1=d&ctl00%24CPH%24DDL_Dist={district}&ctl00%24CPH%24DDL_RO={regOff}&ctl00%24CPH%24txt_deedno={deedNo}&ctl00%24CPH%24txt_deed_year={year}&ctl00%24CPH%24txtCapcha=W4N4R7&ctl00%24CPH%24btnSubmitQuery=Submit&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=eCFSx0asCv1LSZRmMYO1pI7vwzRqk4hJB7FrjfIFCtIDSYkLhAWW3DUnAFoZGt2ExeKHkZzzbQVor6%2Be5Njp%2F5DmW4xEGfOUf8IJBexUHYCwV5IM1C%2BJdK9HXJWV522REP3BZiA4QmoqWt17ElHHkzGTVadzopzCyiW6Lzi%2FXlCmhbn4XfpmeTmvIFNljXKEZQIYI6t4YY00qLWZ%2Brk%2FDgs7TVciI6VdwVLHuEqw7uW2IyaOQTWxNn7u9l35lKWsglAtyMueHiuKBZwYTheFlI5H%2FSalSsKYGvSiwSWOfGGbV47WVp3VHKziZXtOCU3LTvczxXuiSiaasfHe%2BwLs5bXdZGnN7s2uOI1WxUUPa6W1JW1NrN0MBSfaE3Ww4cLFsbR4G1i3HVC3SokWnPDvRPfXJLFU%2BiKnK4CUAC%2BiOvW2GAQy0AqaDMOvQALrDl2ET1fuiH%2FAfYcHUnqv2347TzAS%2FZAb02OcXr%2BveAFKxEA%2FWdyWJ%2B2eGo0qxRC5jycPHSP16cZOt4zY3bI%2FWMvEdUhuk4aG4X4x3K%2FDSyKDlYajqqz084AqIxDEqTpeChWtVJx%2B%2FObgTmvsMDtajhyAJWYfkIHCdpVP%2Bq1BNYsYUrci358jHD%2FiKka5l5tEJukNb79BFE7OZnq8wcaSj%2FySfAJACiKKDNDijrYLNcDh6WCYcyAvfNieCvVpOZGN6f3PbXMsKTxMGc3vx4Yeg79KKzpKu%2Fzgha%2Byo35n9%2BUo6VfUOMDvNjm7KR51fdgw7UhIB1hpAtLffq0mXc0EL%2BAc9UJhTEpuTDaVgLLACJWqlxKE2sIGjJWfcElYZVEjLlPt%2FNRjiYuJBKEZ0pmcbjeVS1dwZP8niqCLhg3UamCkgvsWjzd8xjlk0E8x5kCL9RUHvHD3dNXAf3MzHLzWwSfz8Mh%2B4sGsGq4vydPFCsEobCwy%2BM5h21Wd4I6Yfv14krMYluXxZcTUv46njVm8GoRbpjO2Gmt%2FHVmSs45LrQrsfjZv59R8rkaoC%2BBGI9FRfDmX4ldX7eox%2FRptJDsc8qLJ%2FDVnhut23OhTLnJFs4SJ8UdbIeJ13lL0Lr1tYttUEbi9oJcYNre3UlDvIdHf5OXJ4EQxx7zSbcO9nuzdSHL2nGIUV6F4Xuu70IkxUA8iBRQrKqES%2B0s2CHpDfn5iQlqU5524vI20L05F6hd87kG21WOu1AQAoSWau0SqjsJ5XGWYcJ6KWEv10avL7IocKJE6Mr3tbzVA9GJ21bUN9bls%2FPf5BHDn3ltLV6sbG1%2BQu2wEiDm1%2BrR5xpUl4rA1MN7x1HnYFOVFmWY0STo9NGR2QqD5ROTF039TT%2FeZ5kCbe%2FP3aXcobAKeEN4nEM1F5nVLFT0XeispXQHtAECIFjeSR6UcVd5uJt3jd0GHm7k44yWVz0LEZ1pL05zjnq0Y7DBqtL6ctqFIhQFl4fHPlTexjRBW2F0WO1nslBXFSooiQ%2FSDfkIXlgdD%2FSzqzbOlrQUaBo9f7hQ9YjdQtJ%2B3lYTUMS569TT%2BaMIJB87nyKite59cEspbv1L%2BipQCxnP28nKa6gtC%2BZv2sMDlCDVeggJuE4LlnAXVGbUsdOYk004hnlyzjLMtOV3y1y2ONZS53dK0xPdZtr9wb8IZRysMbQteVr2%2FjmJiAdnTsZlBNupO7zWhHdkXhwH8hUezcdxKHSJfxMPcYzTdNqrhVSmRQJjjnK09KS6zb%2FdAUvlo6O0t0BSEkxumZ1FvF5Myd2aEqdmFPOK52MPOPE9F8lvPfIrhbcOQlv91LxDfZALDyoF4WnR3hPG2%2FV0rkI%2FPdce%2Fc8z0mORaxi98y7hML42EE006xnKgcZgNpJ2ulA4OKCGJrt9zsFrM8rzcaY8ZSG9SXym6gnCA7V3E4txmKBwuoxnaVCrSyxY0Ots9KMK1IrYgoVdL%2BtMz3vwXGn%2BTvp8JxuOklIxqChJEi%2BkeQa7VJB2nnGGpy%2FwUA%2FYaZOktQ93Era0gsG%2F7yabn0%2F80Ot7J0sm%2BIZ3XU0HO1ea61I9k5zY6zMn9pUO4MfC7OtTXKURN%2BfySpbBWfFiTD0fTPAjQOsRGY77GUnYU9KqBDde1lb7k0Po%3D&__VIEWSTATEGENERATOR=6012E183&__EVENTVALIDATION=gpoEdwbsJZ0oa%2FYkwCwiqsghKwBLrFmKnA6YWhvzmN2%2BZvYLWQGPFYl1obZxzQxXwgyZy9jhr6CTTtaLKKZfVDuvXNPoiTOhGophjVc4oLpRTqlbUjjgEgTY8egaN3toe%2BtKbs35B1%2BMA0dqibZ5KBwjJ1ablir9CesdAvVWiMGk%2Ft2waNJJRz4UjitdsKop9TUg%2B5w%2Bg8t3uWZFWFmZeLv1NPWm7GSWAvoZxZRQ9PgIoXjjYV8a1YR2TdsXh2AA9Oc7TVQ95mKXDsuRNGJA43FPjxzoeG33BFhdtawdLC1cu9TSqruUl97OPXab9RAMu2fiSX4V25pzLUtBfEXgIE04a6tPaB4EXLcmqqIMRUt4rqEUGPd68%2Bvv2F6Z%2BL6lJ7OnjtpatpQzlnyhhqRilbYbVWU1VCTKSJt5QkcvYnvYfwywtLR%2FejNKCqTL6gm9N5g1VQnScK2VtRv3WHd65aiNNlkkdOU0dxLFAM8CwhsCThLmPA1vZmhBX4HOfRZNEkgd2IQnMVBbUSJzvD6bll3rHia82jUtZ4xwGdUiLmg7Mj8ESJnEajYCZ6XEuUO9SGeaxMuKIdvRqRVhF0vV37z7ePFUZnNm%2BVbe0EGdamP%2Fpq22B7voV0G4ZdtSAEXsgcjBjWdh%2FwnO3VIJAUPjnc4yv%2Fhy5DLJ%2FZ20HP3nhO837MoXiu2FTBLEUFgdhGjrS6Piuu8g7Z%2Bk25fMW9z4WrVThwlh8qc1mK6gvieaUTJQVbzo9YmdS5oCyYzwPrTrCxySisftbn5pblFZ7MEEjWFpBbAEPBEVehl19LIEoLG7KZpV42gzAE0e0HWGIOnrk0VnQ8DLHspdhJZOW6p9DQqPkp2o43ItwR5Mb1BZKg57Y%2FkkzDbGRsk9QtHiBz%2BY&__VIEWSTATEENCRYPTED='

                    response = requests.request(
                        "POST", url, headers=headers, data=payload)

                    soup = bs4.BeautifulSoup(response.text, 'html.parser')

                    p = HTMLTableParser()
                    p.feed(response.text)

##################### Covert The Data In The Tables to DataFrames #######

                    # Deed Details Table
                    df = pd.DataFrame(p.tables[1])
                    data_dict = df.to_dict(orient='records')
                    data_dict = [{str(k): v for k, v in row.items()}
                                 for row in data_dict]

                    # Name & Address of the Party Table
                    df2 = pd.DataFrame(p.tables[2])
                    data_dict2 = df2.to_dict(orient='records')
                    data_dict2 = [{str(k+10): v for k, v in row.items()}
                                  for row in data_dict2]

                    # Details of Property Table
                    df3 = pd.DataFrame(p.tables[3])
                    data_dict3 = df3.to_dict(orient='records')
                    data_dict3 = [{str(k+20): v for k, v in row.items()}
                                  for row in data_dict3]

                    # Coversion Of The Name & Address Table Data In Array of Dictionary
                    name = {}
                    j = 0
                    for i in range(1, len(data_dict2)):
                        name[str(i-1)] = {"name": data_dict2[j].get('10'),
                                          "Address": data_dict2[j].get('11'), "Status": data_dict2[j].get('12')}
                        j += 1

                    # Coversion The Properties Table Data In Array of Dictionary
                    properties = {}
                    j = 0
                    for i in range(1, len(data_dict3)):
                        properties[str(i-1)] = {"Property Location": data_dict3[j].get('20'), "Property Type & Transaction": data_dict3[j].get(
                            '21'), "Plot & Khatian No and Zone": data_dict3[j].get('22'), "Area of Property": data_dict3[j].get('23')}
                        j += 1

                    # Final Conversion For Storing The Database With Proper Format
                    data = {
                        "Deed Details": {
                            "Transaction": data_dict[1].get('0'),
                            "Registered At": data_dict[1].get('1'),
                            "Deed No": data_dict[1].get('2'),
                            "Volume & Page No": data_dict[1].get('3'),
                            "Date of Registration": data_dict[1].get('4'),
                            "Date of Completion": data_dict[1].get('5'),
                            "Date of Delivery": data_dict[1].get('6'),
                            "Serial No": data_dict[1].get('7'),
                            "Name & Address of the Party": name,
                            "Details of Property": properties
                        }
                    }

                    district = int(district)
                    deedNo = int(deedNo)
                    regOff = int(regOff)

                    # Type Checking So Only Unique Data Can Be Store
                    if str(data) in uniqueData:
                        continue
                    uniqueData.add(str(data))

                    # Adding The Data In Collection
                    collection_name.insert_many([data])
                    print("Data Added In The Database")
                    print(data)

                # Data Not Found For Particualr Inputs
                except Exception:
                    print("Unable to Find Details Please Provide Proper Inputs")
                    district = int(district)
                    deedNo = int(deedNo)
                    regOff = int(regOff)

############################### End Of The Script ########################################
