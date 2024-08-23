import requests

def set_buoy_url(buoy_url):
        buoy_url = buoy_url
        buoy = str(buoy_url)
        url = "https://www.ndbc.noaa.gov/data/realtime2/" + buoy + ".txt"
        return url 

def get_url_content(url):
        page = requests.get(url)
        content = page.content
        content = content.decode('utf-8')
        return content

if __name__ == "__main__":

        buoy_url = set_buoy_url(46277)
        page = get_url_content(buoy_url)
        print(page)