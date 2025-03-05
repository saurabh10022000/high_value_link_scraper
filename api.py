from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Link
import requests
from bs4 import BeautifulSoup

app = FastAPI()

Base.metadata.create_all(bind=engine)

KEYWORDS = ["budget", "acfr", "finance director", "contact"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def scrape_links(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    
    links = []
    
    for tag in soup.find_all('a', href=True):
        link_url = tag['href']
        link_text = tag.get_text(strip=True).lower()
        score = sum(1 for kw in KEYWORDS if kw in link_text or kw in link_url.lower())
        matched_keywords = [kw for kw in KEYWORDS if kw in link_text or kw in link_url.lower()]
        
        if score > 0:
            full_link = link_url
            if link_url.startswith("/"):
                full_link = url.rstrip("/") + link_url
            links.append({
                "url": full_link,
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

@app.get("/fetch_links/")
def fetch_links(url: str = Query(..., description="Website URL to scrape")):
    high_value_links = scrape_links(url)
    save_links(high_value_links)
    return {"total_links": len(high_value_links), "links": high_value_links}

@app.get("/links/")
def read_links(db: Session = Depends(get_db)):
    return db.query(Link).order_by(Link.score.desc()).all()
