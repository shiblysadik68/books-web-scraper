📚 Books Web Scraper






🎯 Overview

This is a Python-based web scraping project built with Selenium. I created this project to practice real-world scraping techniques like handling pagination, extracting structured data, and optimizing performance.

The scraper collects book data from an e-commerce-style demo site and stores everything in a clean CSV file.

✨ What this project does
Automatically navigates through multiple pages
Extracts useful data like title, price, rating, and availability
Handles pagination without breaking
Saves all data into a structured CSV file
Runs efficiently without unnecessary delays
📊 Output

The script scrapes 1000+ books across 50 pages and saves them into a CSV file.

Collected data includes:

Book Title
Price (GBP)
Star Rating
Availability
🛠️ Tech Stack
Python
Selenium WebDriver
Pandas
ChromeDriver
🚀 How to run
1. Clone the repository
git clone https://github.com/shiblysadik68/books-web-scraper.git
cd books-web-scraper
2. Install dependencies
pip install selenium pandas
3. Setup ChromeDriver

Download ChromeDriver based on your Chrome version and either:

Add it to PATH, or
Place it inside the project folder
4. Run the script
python web_scraper.py
📁 Output File

After running the script, you will get:

books_data.csv
🧠 What I learned

While working on this project, I focused on improving practical scraping skills:

How to work with Selenium for real-world use cases
Writing better XPath selectors
Handling pagination properly
Debugging when elements are not found
Improving performance by reducing unnecessary delays
Organizing scraped data using Pandas
🐛 Challenges I faced

1. Pagination issue
At first, the scraper failed to move to the next page. The XPath I used for the “Next” button was incorrect. After inspecting the element again, I fixed it by targeting the correct structure.

2. Slow performance
Initially, the script was slow because of extra time.sleep() usage. After removing unnecessary delays, execution time dropped significantly.

📈 Performance
Total Pages: 50
Total Books: 1000+
Execution Time: ~2–3 minutes
🔧 Project Structure
books-web-scraper/
│
├── web_scraper.py
├── books_data.csv
├── README.md
└── LICENSE
🚧 Future improvements
Add headless mode
Export data to JSON / Excel
Add basic UI
Improve error handling
Add multi-threading (for learning purposes)
⚠️ Note

This project is made for learning purposes only.
Always respect website rules before scraping.

👤 Author

Shibly Sadik
GitHub: https://github.com/shiblysadik68

⭐ If you found this helpful, feel free to give it a star.