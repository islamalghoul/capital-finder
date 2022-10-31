from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    s=self.path
    url=parse.urlsplit(s)
    query=parse.parse_qsl(url.query)
    Query=query[0][0]
    print(Query)
    x=query[0][1]
    if Query.lower()=="country":
        URL=f"https://restcountries.com/v3.1/name/{x}"
        r=requests.get(URL)
        r=r.json()
        capital=r[0]["capital"][0]
        massage=f"The capital of {x} is {capital}"
    if Query.lower()=="capital":
        URL=f"https://restcountries.com/v3.1/capital/{x}"
        r=requests.get(URL)
        r=r.json()
        country=r[0]["name"]["common"]
        massage=f"{x} is the capital of {country}"
    else:
        massage="you entered an invaled query"
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(massage.encode())
    return