from bs4 import BeautifulSoup
import requests


def get_data_prity(d):
    r = d.find(text=True, recursive=False)
    return str(r.strip())


class IMDB(object):
    """Get all information of a imdb movie, pass html content of imdb page"""

    def __init__(self, html=None):
        if not html:
            self.soup = None
        else:
            self.soup = BeautifulSoup(html, "html.parser")

    def _get_year(self):

        d = self.soup.select(".title_bar_wrapper .titleBar .subtext a")
        release_date = get_data_prity(d[len(d) - 1])

        return release_date.split()[2]

    def _get_rating(self):
        d = self.soup.select(".title_bar_wrapper .ratingValue span")[0]

        return get_data_prity(d)

    def _get_name(self):
        d = self.soup.select(".title_bar_wrapper .titleBar .title_wrapper h1")[0]

        return get_data_prity(d)

    def get_info(self):
        """
        :return: {'category': ['Drama', 'Romance', 'War'], 'rate': '8.5', 'review_count': '469,931', 'name': 'Casablanca', 'year': '1943'}
        """
        m = {}
        m["name"] = self._get_name()
        m["year"] = self._get_year()
        m["rate"] = self._get_rating()
        m["review_count"] = self.get_review_count()
        m["category"] = self._get_category()

        return m

    def _get_category(self):
        w = []
        a = self.soup.select(".title_bar_wrapper .subtext a")
        for i in range(0, len(a) - 1):
            n = a[i]
            w.append(get_data_prity(n))
        return w

    def get_review_count(self):
        d = self.soup.select(".title_bar_wrapper .imdbRating .small")[0]
        return get_data_prity(d)

def get_url_content(url):
    r = requests.get(url)
    print (r.status_code)
    content = r.text.encode('utf-8', 'ignore')
    return content

if __name__ == '__main__':

    url = "https://www.imdb.com/title/tt0034583/"
    imdbHtml = get_url_content(url)
    imdb = IMDB(imdbHtml)
    print (imdb.get_info())