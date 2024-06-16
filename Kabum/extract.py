# %%
import requests

cookies = {
    '__LOCALE__null': 'BR',
    'csrftoken': '2WHv8eqHnatbm9NVrcdfL85gAjWE2rwR',
    '_QPWSDCXHZQA': 'f5ff4255-784b-481e-faed-62d8f3ff1da1',
    'REC7iLP4Q': '464de216-08b1-4ce3-8f1e-e3434595cc0b',
    'SPC_F': '1PvKF09wEwDyBWmVdTxw9CACTQO7oIsS',
    'REC_T_ID': 'a82f997c-2aae-11ef-a93d-ae0a8d57358b',
    'SPC_SI': 'LB9oZgAAAAB5RjBVNE5qQe/EWgAAAAAAR2VobktYSzg=',
    'SPC_SEC_SI': 'v1-dEh2eVU3UjdhM0MyQUdKTAK1ZCXsXimCD1hnX2muSp3mO4BLzYoDigHm30MEr/xqKkPNNGw4yghrgmhPv+qRwmo0/0UUw+U3/M9TkKBjaM4=',
    '_sapid': 'c7be9a91305ef6f7852faa8af01e5bbf39bdde5f45040a11721f5d2a',
    'SPC_CLIENTID': 'MVB2S0YwOXdFd0R5ctmeuteuqyzfesgm',
    'SPC_EC': '.Tms5a29XblVHdjF6VHN0YR5ie7YAVWzAstV1MfmX7Y7qroT2oAMG9IlBWXTUDwmCtPDhJAafVX9Tv7dMUEUrKE49PA+qTI/n507BZr1fzBve9dTej3TfY45B8FXEprptsoA8NBXfKAN6+dzbE6pPmKeqYrijfNapRcOrk9x7wUtfceCtQMK45eqQmvHO15PEYyiqicRkzFCksuHbqYAHN9KtFgnCj+ASA7TrwIJupKo=',
    'SPC_ST': '.Tms5a29XblVHdjF6VHN0YR5ie7YAVWzAstV1MfmX7Y7qroT2oAMG9IlBWXTUDwmCtPDhJAafVX9Tv7dMUEUrKE49PA+qTI/n507BZr1fzBve9dTej3TfY45B8FXEprptsoA8NBXfKAN6+dzbE6pPmKeqYrijfNapRcOrk9x7wUtfceCtQMK45eqQmvHO15PEYyiqicRkzFCksuHbqYAHN9KtFgnCj+ASA7TrwIJupKo=',
    'SPC_U': '1282236153',
    'SPC_R_T_ID': 'qvIo5Kpz5u88u118v5GsRFchesCtlXLc/8DN8R2MWXNHhXdwD4Me6x3aCYio3peLjeqOwJOpclZCkvnQLoQXRhwBUn2fK+Tyzf1G3w8nOlgvx4rXtweSJsai2aW1pkRcaO58bv9FX6gI4a1RlrQZZ5ydtuvj7w9hIUBrdaedB3A=',
    'SPC_R_T_IV': 'ZVd6eERSZjNBMGdxZDMyNQ==',
    'SPC_T_ID': 'qvIo5Kpz5u88u118v5GsRFchesCtlXLc/8DN8R2MWXNHhXdwD4Me6x3aCYio3peLjeqOwJOpclZCkvnQLoQXRhwBUn2fK+Tyzf1G3w8nOlgvx4rXtweSJsai2aW1pkRcaO58bv9FX6gI4a1RlrQZZ5ydtuvj7w9hIUBrdaedB3A=',
    'SPC_T_IV': 'ZVd6eERSZjNBMGdxZDMyNQ==',
    'SPC_CDS_CHAT': 'fa410d7b-db97-48a7-ba7e-4aacaec4be07',
    '_med': 'refer',
    '_gcl_au': '1.1.602684269.1718411689',
    'AMP_TOKEN': '%24NOT_FOUND',
    '_gid': 'GA1.3.899504796.1718411690',
    '_dc_gtm_UA-149843394-1': '1',
    '_ga': 'GA1.1.1987147640.1718411689',
    '_ga_T69DLR1QPG': 'GS1.1.1718411689.1.1.1718411846.45.0.0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'af-ac-enc-dat': 'd20e95e873deae1e',
    'af-ac-enc-sz-token': 'DxcBAAAABAAAAIAAAAKu3jHsqAA9MBFEijlwC7OxKozh9MEx6EmdEuNjwvxex4wfeJCFhSngECk7L4C5BgyQUxP2IuZ97JGwFGE+NhPhANDt+hao7f4gKrAXuq1i3beR3vKv5qMWM9Bdsm8wOlm9dTNKl6U0kOKocha/iyWWxcL7XGkHL3D1sV8nYKtMPU+vAN+//N0GYAAAAAYAAAAAAAAAAAIgX6oYpbfybiiWCMFWt7ELVIoJo/tUxfhaaz/jO8qgjYAZB8uUcyzdGIYlIOqfJhy5UKAXN7DT5XSC9UcfR4RKWR4kJWhjpiYutPSYnUQxhG49RJGzK6+RfPyokoZrD62rr7V6MeIr0LypdXzcVCPhWXw+5WmO/E6AOBxN1+hQsqgHl4HRSs0WK0S3c9v9MVAK3+NjMrUSRcMzdOMVreEw7gwXFGd4aK6jY0OJkkTqHpoj1Qs1yHPOc/hLllAwq2TrYG64TBvPnYm79yPLFfYL9WOxrmI3CwznchxjWyvX1cv2eJO87JN9+MTwnUo/O0lT8a5UcUDmXa29BDQ4DJDZFyG7wSn/bxTCg3+050G64HLApNdy7Vhp+wu0CpzF7wr66Qt5F8r3hG6Rpnw9KdYqW6Y+lNi2Q/3Fu0mRomXzMWSuw8glhEOasQZ3NAaMDvuWu8JJSbOpQlJKbVSm4yxEYZ/OMNRZA9BTBQlT1xe7qbiSsQgvDBf1RgUwyFuyqpqL4pTmtakoBOSn8WZxGStSMW5ZUfkSajMGmr+RYrWmkDfn2aIqDoB1119N73krOoFNcynIbGkcMRnMbHM++Q5/7NbdHkvxPWUcMMepEBQTfIaXsizE2ZYnPj1cTLKpZcM3zrNSTY6msibGSpWuR5iDAWSKCeRNg1tKKS7VeYfWKgrYhjDfkxrLl16Il47Xv9IOjTagR16Mp/q9bH+1gOcKdQ==',
    # 'cookie': '__LOCALE__null=BR; csrftoken=2WHv8eqHnatbm9NVrcdfL85gAjWE2rwR; _QPWSDCXHZQA=f5ff4255-784b-481e-faed-62d8f3ff1da1; REC7iLP4Q=464de216-08b1-4ce3-8f1e-e3434595cc0b; SPC_F=1PvKF09wEwDyBWmVdTxw9CACTQO7oIsS; REC_T_ID=a82f997c-2aae-11ef-a93d-ae0a8d57358b; SPC_SI=LB9oZgAAAAB5RjBVNE5qQe/EWgAAAAAAR2VobktYSzg=; SPC_SEC_SI=v1-dEh2eVU3UjdhM0MyQUdKTAK1ZCXsXimCD1hnX2muSp3mO4BLzYoDigHm30MEr/xqKkPNNGw4yghrgmhPv+qRwmo0/0UUw+U3/M9TkKBjaM4=; _sapid=c7be9a91305ef6f7852faa8af01e5bbf39bdde5f45040a11721f5d2a; SPC_CLIENTID=MVB2S0YwOXdFd0R5ctmeuteuqyzfesgm; SPC_EC=.Tms5a29XblVHdjF6VHN0YR5ie7YAVWzAstV1MfmX7Y7qroT2oAMG9IlBWXTUDwmCtPDhJAafVX9Tv7dMUEUrKE49PA+qTI/n507BZr1fzBve9dTej3TfY45B8FXEprptsoA8NBXfKAN6+dzbE6pPmKeqYrijfNapRcOrk9x7wUtfceCtQMK45eqQmvHO15PEYyiqicRkzFCksuHbqYAHN9KtFgnCj+ASA7TrwIJupKo=; SPC_ST=.Tms5a29XblVHdjF6VHN0YR5ie7YAVWzAstV1MfmX7Y7qroT2oAMG9IlBWXTUDwmCtPDhJAafVX9Tv7dMUEUrKE49PA+qTI/n507BZr1fzBve9dTej3TfY45B8FXEprptsoA8NBXfKAN6+dzbE6pPmKeqYrijfNapRcOrk9x7wUtfceCtQMK45eqQmvHO15PEYyiqicRkzFCksuHbqYAHN9KtFgnCj+ASA7TrwIJupKo=; SPC_U=1282236153; SPC_R_T_ID=qvIo5Kpz5u88u118v5GsRFchesCtlXLc/8DN8R2MWXNHhXdwD4Me6x3aCYio3peLjeqOwJOpclZCkvnQLoQXRhwBUn2fK+Tyzf1G3w8nOlgvx4rXtweSJsai2aW1pkRcaO58bv9FX6gI4a1RlrQZZ5ydtuvj7w9hIUBrdaedB3A=; SPC_R_T_IV=ZVd6eERSZjNBMGdxZDMyNQ==; SPC_T_ID=qvIo5Kpz5u88u118v5GsRFchesCtlXLc/8DN8R2MWXNHhXdwD4Me6x3aCYio3peLjeqOwJOpclZCkvnQLoQXRhwBUn2fK+Tyzf1G3w8nOlgvx4rXtweSJsai2aW1pkRcaO58bv9FX6gI4a1RlrQZZ5ydtuvj7w9hIUBrdaedB3A=; SPC_T_IV=ZVd6eERSZjNBMGdxZDMyNQ==; SPC_CDS_CHAT=fa410d7b-db97-48a7-ba7e-4aacaec4be07; _med=refer; _gcl_au=1.1.602684269.1718411689; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.899504796.1718411690; _dc_gtm_UA-149843394-1=1; _ga=GA1.1.1987147640.1718411689; _ga_T69DLR1QPG=GS1.1.1718411689.1.1.1718411846.45.0.0',
    'if-none-match-': '55b03-65337cd8554d7a0a4e95e3c6e78a1ca4',
    'referer': 'https://shopee.com.br/collections/4561540?page=1',
    'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
    'x-api-source': 'pc',
    'x-requested-with': 'XMLHttpRequest',
    'x-sap-ri': '67e26c665806c10967cddd31030121ee9e0b5281632b841945b8',
    'x-sap-sec': 'BT5lHZtQ3etB7etB6UtK7eGB6UtB7eGB7etN7etBjeFB7oGN7etQ7etB4k0V8ZhB7enI7ZtBeeFB7SPpy2h9PpngkqQf4/CSFHZ+oyTQqHDVrNMIbh+6uzsFQFhZj4A9CYyLQsykPUh4Q5su2ztBZHN0bqMVGB8eLz0sI99LZxONgruaZDaoha2+h709aVYjhH3aSRG5PHkphpnghTuCD6afgXCPjgVgGEuJieuFTUfQWZFvSrh4VBjY8HunRedKtHcNs48awVDZCRRSPq3ztebsQQ3yOQMmpuKwZh1ZN5gUII4ZnQKMcEFuXcMbFfT0k8MXEOwENS1TJqhWNg5P5hLMmTr5YSjtLgiHUziEBvQenIAUnnHhYJ103WToSI/08S8eukiPUCHR2jCQ4Uz7sMDXnAWFTSqKsIJOU43j7/aHoZLrajT5rkIK0kpSE4r3NmOn0pGRFu9SwA0RAd02NU1yWNFiJAhh97ax8Gg2q6uHpeK5SC71jrE3pcTEpe9vTyWK5mWqfqPkI2b17iCYyHLXUGkuo75HUxk4LH4LYhvJXuTEuSnLU5cVpzKHt77IhsI7hGSoLpbgYRkUlunIh3uZMuqVFc+pWh8zJKjmuXIpiLcTrL37BuT5Yx8hoeuooRBAqhiq+BM4juwA2xAdHRyTg9eu9jgqicxCLhE4haKJdC35UyG9ta+kX2QeUzuePwYBuOBtZVNWtdFIAucyZFB2RmWYTatGWumeN6PH1RbKoJ73OeWsNLR/U7oOX5TCnH4PJpxOpmTo6oRpy679GejdBOw3fsNFXkabHjPgmIctO3OMvh9VvQMwMNfr9ctxK1E4rbU87Jg81QJZJAAW3yasgAOAvg0F/7RXnhqNJMPUxHoHVNvStDGtvUBcSFcoPde5wPYpBOY818tf0SqjaqA+2++Pz/O+z0TmN+YvnsYshNO4WvB5Ley29vjYToW61lLS1+VzYy7kCm7XxF7/CoOzQf0+ltWmRPqYloofC3SLGAgyaiXHPHv+cqkVrd6yBSbyLIDnZh6yrOYGnHwfoIeRpt2FTtcQBMdle6/bPSzm3VjrW2f8UfugFkUDHXtw5I5wknlon22DSJfL/S2CmiJyU1ZUhDnAtaKX/4O1T4Y3czKMPDSv/Sv3oRXUlZ1zfjJ6FsG8euIhOXbSiWZAZ9xzl3lfUJIKGrDcQw+BQ0Gl7vhgMyZK7etB5uCyNaFF5p8B7etBUkdV8ZhB7etE7etB2etB7sMH2+7lgyfTBnEb8vx9G0c/4elg/etB7pDy5SZF41vj7etB7ehB3etK7eGB/etB7ehB7etE7etB2etB7HJN+mGf4pecoX7Mply180iiQjBJ/etB7SZT5pGA+1h87etB7s==',
    'x-shopee-language': 'pt-BR',
    'x-sz-sdk-version': '1.10.1',
}

params = [
    ('by', 'relevancy'),
    ('limit', '60'),
    ('match_id', '4561540'),
    ('newest', '60'),
    ('order', 'desc'),
    ('page_type', 'collection'),
    ('scenario', 'PAGE_COLLECTION'),
    ('version', '2'),
    ('view_session_id', '89cd877d-af30-4247-89c3-dda38bd7ec97'),
    ('collection_id', '4561540'),
    ('item_order', '0'),
    ('limit', '60'),
    ('offset', '60'),
    ('source', '2'),
]

response = requests.get('https://shopee.com.br/api/v4/collection/get_items', params=params, cookies=cookies, headers=headers)
response.text
# %%
