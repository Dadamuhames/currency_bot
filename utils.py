import requests
from datetime import datetime


BASE_URl = "https://gh-pinned-repos-5l2i19um3.vercel.app/"
PROXY = {
    "https": "https://proxy.server:3128"
}


# get all currencies 
async def get_all_currs():
    response = requests.get(BASE_URl + f"/currencies/", proxies=PROXY)

    if response.status_code != 200:
        return None
    
    try:
        response = response.json()
    except:
        return None

    return response['result']


# get single currency
async def get_currency(code):

    response = requests.get(BASE_URl + f"/currencies/{code}", proxies=PROXY)


    if response.status_code != 200:
        return None

    try:
        response = response.json()

        if isinstance(response, dict):
            response = response['result']

        if isinstance(response, dict):
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

    # https://gh-pinned-repos-5l2i19um3.vercel.app/currencies
