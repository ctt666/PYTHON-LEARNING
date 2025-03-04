import requests
import bs4
import concurrent.futures

def fetch_content(url):
    try:
        # Add headers to make the request look more like a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        # requests.get是线程安全的
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        if resp.text:
            print('Read {} from {}'.format(len(resp.text), url))
            return resp.text
        else:
            print('Empty response from {}'.format(url))
            return None
    except requests.RequestException as e:
        print('Error fetching {}: {}'.format(url, e))
        return None

def crawl_movie(url):
    init_page = fetch_content(url)
    init_soup = bs4.BeautifulSoup(init_page, 'html.parser')

    movie_names, urls_to_fetch, movie_dates, pages = [], [], [], []
    all_movies = init_soup.find('div', id="showing-soon")
    for movie in all_movies.find_all('div', class_='item'):
        all_a_tag = movie.find_all('a')
        all_li_tag = movie.find_all('li')
        # eg:<a href="http://example.com/1">Link 1</a>
        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        movie_names.append(movie_name)
        urls_to_fetch.append(url_to_fetch)
        movie_dates.append(movie_date)


    with concurrent.futures.ProcessPoolExecutor() as executor:
        pages.extend(executor.map(fetch_content, urls_to_fetch))
    
    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = bs4.BeautifulSoup(page, 'html.parser')
        img_tag = soup_item.find("img")
        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

if __name__ == "__main__":
    url = "https://movie.douban.com/cinema/later/beijing/"
    crawl_movie(url)