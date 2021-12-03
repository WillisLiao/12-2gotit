#for i in range(1,16):  
    #url = "https://www.majortests.com/word-lists/word-list-{:02d}.html".format(i)
    #print(url)
import requests
import csv
from bs4 import BeautifulSoup as bs
import time
def generate_search_url(url,seq):
    return url.format(seq)

def get_resource(url):
    headers = {'user-agent':'Mozilla/5.0 (Macintoshi; Intel Mac OS X 10_11_6'
                'AppleWebKit/537.36(KHTML, like Gecko)'
                'Chrome/56.0.2924.87 Safari/537.36'}
    return requests.get(url, headers = headers)            
def parse_html(r):
    if r.status_code == requests.codes.ok:
        r.encoding = "utf8"
        #soup = BeautifulSoup(r.text, "lxml")
        soup = bs(r.text, "html.parser")
    else:
        print('Parse_html Error...')
        soup = None
    return soup    

def get_words(soup):
    words = []
    for wordlist_table in soup.find_all(class_='wordlist'):
        for word_entry in wordlist_table.find_all("tr"):
            new_word = []
            print(word_entry.th.text)
            new_word.append(word_entry.td.text)
            words.append(new_word)
    return words        

def save_wordList_csv(wordlist):
    with open('wordlist.csv', mode='a', encoding='utf8') as outp:
        writer = csv.writer(outp)
        for row in wordlist:
            writer.writerow(row)
        outp.close()

def start_scrapting():
    url = "https://www.majortests.com/word-lists/word-list-{:02d}.html"
    totalList = []
    for i in range(1, 2):
        tmpurl = generate_search_url(url, i)
        # print(tmpurl)
        r = get_resource(tmpurl)
        # print(r.text)
        soup = parse_html(r)
        wordlist = get_words(soup)
        totalList.append(wordlist)
        save_wordList_csv(wordlist)
    return totalList

if __name__ == '__main__':
    start_scrapting()
