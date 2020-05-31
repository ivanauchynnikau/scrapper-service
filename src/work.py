import requests
import codecs
from bs4 import BeautifulSoup as bs


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Accept': '*/*',
}

def work(url):
    jobs = []
    errors = []

    domain = 'https://www.work.ua'
    url = 'https://www.work.ua/jobs-kyiv-python/'
    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        soup = bs(resp.content, 'html.parser')
        main_div = soup.find('div', id='pjax-job-list')
        if main_div:
            div_list = main_div.find_all('div', attrs={'class': 'job-link'})

            for div in div_list:
                title_tag = div.find('h2')
                title = title_tag.text
                href = title_tag.a['href']
                content = div.p.text
                company = 'No name'
                logo = div.find('img')

                if logo:
                    company = logo['alt']

                jobs.append({'title': title, 'url': domain + href, 'description': content,
                             'company': company})
        else:
            errors.append({'url': url, 'title': 'Main div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page not response'})

    return jobs, errors


def rabota(url):
    jobs = []
    errors = []
    domain = 'https://www.radota.ua'

    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        soup = bs(resp.content, 'html.parser')
        main_table = soup.find('table', id='ctl00_content_ctl00_gridList')

        if main_table:
            tr_list = main_table.find_all('tr', attrs={'id': True})

            for tr in tr_list:
                title_tag = tr.find('p', attrs={'class': 'card-title'})
                href = title_tag.find('a')['href']
                title = title_tag.find('a')['title']
                content = tr.find('div', attrs={'class': 'card-description'}).text
                company = ''
                company_div = tr.find('a', attrs={'class': 'company-profile-name'})

                if company_div:
                    company = company_div.text

                jobs.append({'title': title, 'url': domain + href, 'description': content,
                             'company': company})
        else:
            errors.append({'url': url, 'title': 'Table does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page not response'})

    return jobs, errors


if __name__ == '__main__':
    url = 'https://rabota.ua/jobsearch/vacancy_list?regionId=1&keyWords=python'
    jobs, errors = rabota(url)
    h = codecs.open('work.json', 'w', 'utf-8')  # 'w' work with file in write mode
    h.write(str(jobs))  # write to file
    h.close()



