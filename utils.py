import requests
from datetime import datetime


BASE_URl = "https://cbu.uz/ru/arkhiv-kursov-valyut/json"



# get string date
def get_now():
    now = datetime.now()

    date_string = now.strftime("%Y-%m-%d")

    return date_string


# get all currencies 
async def get_all_currs():
    date_string = get_now()

    response = requests.get(BASE_URl + f"/all/{date_string}")

    if response.status_code != 200:
        return None
    
    try:
        response = response.json()
    except:
        return None

    return response


# get single currency
async def get_currency(code):
    date_string = get_now()

    response = requests.get(BASE_URl + f"/{code}/{date_string}")


    if response.status_code != 200:
        return None

    try:
        response = response.json()

        if isinstance(response, list):
            response = response[0]

    except:
        return None

    return response  


# get currencies by list
async def get_currencies_from_list(codes: list):
    results = []

    for code in codes:
        cur_info = await get_currency(code)

        if cur_info is not None:
            results.append(cur_info)

    return results