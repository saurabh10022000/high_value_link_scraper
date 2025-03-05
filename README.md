🚀 High-Value Link Scraper & API
This project is a web scraper + REST API that extracts high-value links from any website, prioritizing links with keywords like "Budget", "ACFR", and "Finance Director".
It saves the results in an SQLite database and exposes an API to fetch or trigger scraping.

✅ Features
Scrapes and ranks links based on keywords.
Saves links with metadata (URL, text, relevance score, keywords).
REST API built with FastAPI to:
View stored links.
Scrape new links on demand.
Easy to run locally.
🛠️ Installation & Setup Guide
Follow these steps to run this project on any desktop (Mac, Windows, Linux):

1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/high-value-link-scraper.git
cd high-value-link-scraper
2️⃣ Install Python (if you don't have it)
Ensure Python 3.9+ is installed.

Check version:

bash
Copy
Edit
python3 --version
For macOS:

bash
Copy
Edit
brew install python
For Windows:
Download from https://www.python.org/downloads/

3️⃣ Create and Activate Virtual Environment
bash
Copy
Edit
python3 -m venv env
source env/bin/activate        # Mac/Linux
env\Scripts\activate           # Windows
4️⃣ Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not yet created, run:

bash
Copy
Edit
pip install fastapi uvicorn requests beautifulsoup4 sqlalchemy pydantic
pip freeze > requirements.txt
5️⃣ Run the Scraper (Optional)
To manually scrape a website and save the high-value links:

bash
Copy
Edit
python run_scraper.py
This uses the default URL (https://www.a2gov.org/) inside the script.

6️⃣ Run the API
Start the FastAPI server:

bash
Copy
Edit
uvicorn api:app --reload --host 0.0.0.0 --port 8000
✅ How to Use the API
➤ Open in browser or tools like Postman:
1. Scrape any website on demand:
ruby
Copy
Edit
GET http://127.0.0.1:8000/fetch_links/?url=https://www.a2gov.org/
Scrapes the website.
Saves high-value links in the database.
Returns the links immediately.
2. Get all stored high-value links:
nginx
Copy
Edit
GET http://127.0.0.1:8000/links/
Returns all links stored in the database.
Sorted by relevance score.
3. API Docs:
FastAPI provides automatic documentation:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
✅ View the Database
The scraper uses SQLite.
You can view the links.db database with:

GUI option:
Download DB Browser for SQLite.
Open links.db.
Terminal option:
bash
Copy
Edit
sqlite3 links.db
Then run:

sql
Copy
Edit
SELECT * FROM links;
✅ Project Structure
bash
Copy
Edit
high-value-link-scraper/
│
├── api.py              # FastAPI server and endpoints
├── scraper.py          # Core scraper logic
├── run_scraper.py      # Manual scraper runner
├── models.py           # SQLAlchemy DB models
├── database.py         # Database setup
├── links.db            # SQLite database (auto-generated)
├── requirements.txt    # Python dependencies
├── env/                # Virtual environment
└── README.md           # Project documentation
📝 How to Deploy
Push this project to GitHub.
Share this documentation.
Anyone can clone, set up, and run on their desktop following these steps.
🚀 Optional Future Improvements
Add duplicate link detection.
Store source website info with each link.
Upgrade keyword ranking with AI (OpenAI GPT, etc.).
Switch SQLite to PostgreSQL for large-scale use.
Add export endpoints (CSV, Excel).
✅ Author
Saurabh Jain