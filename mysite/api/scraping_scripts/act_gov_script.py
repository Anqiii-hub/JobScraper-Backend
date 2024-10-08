from datetime import datetime
import requests
from bs4 import BeautifulSoup
from ..models import JobPost

def get_record(card):
    '''Extract job data from a single record'''
    
    ad_title = card.h3.text
    job_title = ad_title.split('|')[0].strip() # Job title
    job_type = ad_title.split('|')[1].strip() # Job type

    div1 = card.find_all('div', 'span50')[0]
    div2 = card.find_all('div', 'span50')[1]
    
    
    # Clean the close date by removing the 'Closes: ' part
    close_date_raw = div1.p.find_all('br')[1].next_sibling.strip()
    close_date_cleaned = close_date_raw.replace('Closes: ', '').strip()
    # Parse the date
    close_date = datetime.strptime(close_date_cleaned, '%d %B %Y').date()

    company_name = div1.p.find_all('br')[0].next_sibling.strip() # Company name
    card_href = div2.a.get('href') # Job link

    card_response = requests.get(card_href)
    card_content_soup = BeautifulSoup(card_response.text, 'html.parser')

    position_details_div = card_content_soup.find('div', 'position-details') # Position details
    release_date = position_details_div.find(string="Advertised (Gazettal date):").find_next(string=True).strip() # Release Date
    
    
    location = 'Canberra' # Location
    job_ori = 'ACT Government Website' # From

    record = {
        'job_title': job_title,
        'job_type': job_type,
        'close_date': close_date,
        'company_name': company_name,
        'job_link': card_href,
        'position_details': position_details_div.text.strip(),
        'release_date': release_date,
        'location': location,
        'job_origin': job_ori,
    }

    return record

def main():
    url = 'https://www.jobs.act.gov.au/opportunities/latest'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', 'position')

    for card in cards:
        record = get_record(card)
        
        # Save data into the Django model
        JobPost.objects.create(
            job_title = record['job_title'],
            job_type = record['job_type'],
            close_date = record['close_date'],
            company_name = record['company_name'],
            job_link = record['job_link'],
            position_details = record['position_details'],
            release_date = datetime.strptime(record['release_date'], '%d %B %Y').date(),  # Convert to date format
            location = record['location'],
            job_origin = record['job_origin']
        )