# Scrapy Job Scraper
A very basic Scrapy-based web crawler that is configured to extract clean, structured job listing data from **Python.org**.

## 🚀 Features

- **Automated Extraction**: Scrapes job titles, companies, locations, posting dates, and categories.
- **Structured Data**: Exports gathered data into `jobs.json` for analysis.
- **Configurable Architecture**: Built using the Scrapy framework, allowing for high performance and easy expansion to more job boards.

## 🛠️ Getting Started

### Prerequisites

- Python 3.10+
- Scrapy

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zgander/scrapy1.git
   cd tutorial
   ```

2. Install dependencies:
   ```bash
   pip install scrapy
   ```

### Running the Spider

To start the job scraping process and save the results:

```bash
scrapy crawl careers -o jobs.json
```

## 📂 Project Structure

- `tutorial/spiders/`: Contains the core scraping logic (`career_spider.py`).
- `jobs.json`: The latest scraped job listings.
- `scrapy.cfg`: Project configuration file.

