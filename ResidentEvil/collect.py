# %%
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd

HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': '_gid=GA1.2.120245518.1717943796; _gat_gtag_UA_29446588_1=1; __gads=ID=c095485368e8c9ef:T=1717943796:RT=1717944960:S=ALNI_MZEkvwGXTIYawp9vO0Nh_qUqQYBZQ; __gpi=UID=00000a2c7cff322c:T=1717943796:RT=1717944960:S=ALNI_MZ8xHaMoGBCOUjHqFNEzhspE6QEDg; __eoi=ID=6ca9f5cb89526503:T=1717943796:RT=1717944960:S=AA-AfjY4PccA6QwBbPKxlwCibpKr; _ga=GA1.2.1069484833.1717943796; FCNEC=%5B%5B%22AKsRol9FbyLqcK_VWtAem15uFJxyJ35it1RIou14FPDpPtjNLWJghGE_QpWE2w4jm48fcr-8TTudg2DXsg5OzXUaNz9TVX9qGYftl4sOc2J_rNI84wK6sXdUmiio5F9NjQjzZYqEr2nvhd36PoDPQGhxISYdeSoJ5Q%3D%3D%22%5D%5D; _ga_DJLCSW50SC=GS1.1.1717943795.1.1.1717944991.28.0.0; _ga_D6NF5QC4QT=GS1.1.1717943795.1.1.1717944991.29.0.0',
        'referer': 'https://www.residentevildatabase.com/personagens/',
        'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
    }



def get_links():
    url ='https://www.residentevildatabase.com/personagens'
    resp = requests.get(url, headers=HEADERS)
    soup_chars = BeautifulSoup(resp.text)
    ancoras = (soup_chars.find("div", class_="td-page-content")
            .find_all("a"))
    links = [i["href"] for i in ancoras]
    return links

def get_content(url):    
    return requests.get(url,headers=HEADERS)

def get_basic_info(soup):
    div_page = soup.find("div",class_ ="td-page-content")
    div_page
    paragrafo = div_page.find_all("p")[1]
    ems = paragrafo.find_all("em")
    data = {}
    for i in ems:
        chave,valor, *_ = i.text.split(":")
        chave = chave.strip(" ")
        data[chave] = valor.strip(" ")
    return data


def get_aparicoes(soup):
    lis  = (soup.find("div", class_="td-page-content")
            .find("h4")
            .find_next()
            .find_all("li"))
    aparicoes = [i.text for i in lis]
    return aparicoes
# %%
def get_char_info(url):
    resp = get_content(url)
    print(url)
    if resp.status_code != 200:
        print("Não foi possivel retornar a página")
        print(resp.status_code)
        return {}
    else:
        soup  = BeautifulSoup(resp.text)
        data = get_basic_info(soup=soup)
        data['Aparicoes'] = get_aparicoes(soup)
        return data
# %%
links = get_links()
data = []
for i in tqdm(links):
    d = get_char_info(i)
    nome = i.split("/")[-1].replace("-", " ").title()
    d["Nome"] = nome
    d["link"] = i
    data.append(d)
# %%
df = pd.DataFrame(data)
df.to_parquet("dados_re.parquet", index=False)

df_new = pd.read_parquet("dados_re.parquet")
# %%
