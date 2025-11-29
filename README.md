# Selenium Scraper Template

Reusable Selenium template with:
- headless mode
- env config (.env)
- webdriver-manager auto driver setup

## Setup & Run
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt

# create env file
# Windows:
copy .env.example .env
# Linux/Mac:
cp .env.example .env

## Environment variables
- `HEADLESS=1` — run Chrome in headless mode
- `USER_AGENT=` — optional custom user-agent
- `START_URL=` — page to open

python src/scraper.py

