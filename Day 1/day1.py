from time import sleep
import random
import requests
from IPython import embed
from bs4 import BeautifulSoup
import re

def delay(seconds):
    print(f"sleeping for {seconds} second(s)")
    sleep(seconds)

def get_random_number():
    return random.randint(1,5)

def generate_html():
    return """
    <html>
	    <head></head>
	    <body>
		    <div href = "/a.html">A</div>
            <div href = "/b.html">B</div>
            <div href = "/c.html">C</div>
            <div href = "/d.html">D</div>

            <script>
                var hello = "yoh";
                alert(hello);
            </script>
	    </body>
    </html>
    """

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}

sleep(2)

BASE_URL = "https://albertyumol.github.io/"

def extract_html_content(target_url):
    response = requests.get(target_url, headers)
    return response.text

titles = []

def main():

    ## 2nd to the last challenge
    html_content = generate_html()
    soup = BeautifulSoup(html_content, 'html.parser')

    print(soup.find('script').string.split()[3].replace('"', '')[:-1])

    ## Last challenge
    # for i in range(1,5):
    #     if i == 1:
    #         target_page = BASE_URL + "index.html"
    #     else:
    #         target_page = BASE_URL + 'page' + str(i) + '/' + "index.html"

    #     html_content = extract_html_content(target_page)
            
    #     soup = BeautifulSoup(html_content, 'html.parser')
    #     div_elements = soup.find_all(rel='permalink')

    #     for div_element in div_elements:
    #         titles.append( div_element.get_text().strip('\n') )

    # print( titles )            
    # print( f"\nThe no. of articles is {len(titles)}.\n" )


    
if __name__ == "__main__":
    main()