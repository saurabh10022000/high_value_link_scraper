import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Link

KEYWORDS = ["budget", "acfr", "finance director", "contact"]

Base.metadata.create_all(bind=engine)

def scrape_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    links = []
    
    for tag in soup.find_all('a', href=True):
        link_url = tag['href']
        link_text = tag.get_text(strip=True).lower()
        score = sum(1 for kw in KEYWORDS if kw in link_text or kw in link_url.lower())
        matched_keywords = [kw for kw in KEYWORDS if kw in link_text or kw in link_url.lower()]
        
        if score > 0:
            links.append({
                "url": link_url,
                "text": link_text,
                "score": score,
                "matched_keywords": matched_keywords
            })
    
    return sorted(links, key=lambda x: x['score'], reverse=True)

def save_links(links):
    db: Session = SessionLocal()
    for link in links:
        db_link = Link(
            url=link["url"],
            text=link["text"],
            score=link["score"],
            matched_keywords=link["matched_keywords"]
        )
        db.add(db_link)
    db.commit()
    db.close()

if __name__ == "__main__":
    url = "https://www.a2gov.org/"
    high_value_links = scrape_links(url)
    save_links(high_value_links)
    print(f"{len(high_value_links)} high-value links saved to the database.")
