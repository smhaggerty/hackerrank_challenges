from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for ele in attrs:
            print('-> ' + str(ele[0]) + ' > ' + str(ele[1]))

    def handle_endtag(self, tag):
        print("End   :", tag)
        
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for ele in attrs:
            print('-> ' + str(ele[0]) + ' > ' + str(ele[1]))
        

n = int(input())
html = "".join([input() for _ in range(n)])
parser = HTMLParser()
parser.feed(html)