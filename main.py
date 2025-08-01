# Amazon URL Validator by Jorge Rodriguez, written for us by Ying Zhang's Amazon Price Checker
#CS361 - Software Engineering I - Summer 2025 - OSU

# Receives a string containing a URL and returns a JSON which reports its status as either valid or not
# If the URL is valid, it returns also the ASIN and domain
# If the URL is not valid, it returns also the reason why it failed validation
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/validate', methods=["post"])
def post_handler():
    data = request.json
    url = data.get('URL')
    result = json.dumps(is_valid_Amazon_URL(url))

    return result

def is_valid_Amazon_URL(incoming_url: str) -> dict:
    url_split = incoming_url.split('/')

    if url_split[0].lower() not in ['https:', 'http:']:
        return {'status': 'invalid', 'reason': 'malformed http header'}

    if url_split[1] != '':
        return {'status': 'invalid', 'reason': 'malformed http header'}

    domain = url_split[2]
    if domain[:4].lower() == 'www.':
        domain = domain[4:]

    if domain not in [
        'amazon.ae',
        'amazon.ca',
        'amazon.cn',
        'amazon.co.jp',
        'amazon.co.uk',
        'amazon.com',
        'amazon.com.au',
        'amazon.com.be',
        'amazon.com.br',
        'amazon.com.tr',
        'amazon.com.mx',
        'amazon.de',
        'amazon.es',
        'amazon.eg',
        'amazon.fr',
        'amazon.in',
        'amazon.it',
        'amazon.nl',
        'amazon.pl',
        'amazon.sa',
        'amazon.se',
        'amazon.sg',
        'amazon.co.za']:
        return {'status': 'invalid', 'reason': 'invalid domain'}

    if url_split[3] == '':
        return {'status': 'invalid', 'reason': 'missing product name'}

    if url_split[4] != 'dp':
        return {'status': 'invalid', 'reason': 'missing /dp/ from URL'}

    asin = url_split[5]
    if len(asin) != 10:
        return {'status': 'invalid', 'reason': 'invalid ASIN/ISBN'}

    return {'status': 'valid', 'ASIN': asin, 'domain': domain}


app.run(debug=True)
