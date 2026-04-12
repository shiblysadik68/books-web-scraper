# 📚 Books Web Scraper

<div align="center">

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.15-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*A Python-based web scraping project built with Selenium*

[Overview](#-overview) •
[Features](#-what-this-project-does) •
[Installation](#-how-to-run) •
[Usage](#-output-file) •
[Challenges](#-challenges-i-faced)

</div>

---

## 🎯 Overview

This is a **Python-based web scraping project** built with Selenium. I created this project to practice real-world scraping techniques like **handling pagination**, **extracting structured data**, and **optimizing performance**.

The scraper collects book data from an e-commerce-style demo site and stores everything in a clean CSV file.

---

## ✨ What this project does

<table>
<tr>
<td>

🔄 **Automated Navigation**
- Automatically navigates through multiple pages
- Handles pagination without breaking

</td>
<td>

📊 **Smart Data Extraction**
- Extracts title, price, rating, and availability
- Saves all data into a structured CSV file

</td>
<td>

⚡ **Performance Optimized**
- Runs efficiently without unnecessary delays
- Processes 1000+ books in 2-3 minutes

</td>
</tr>
</table>

---

## 📊 Output

The script scrapes **1000+ books** across **50 pages** and saves them into a CSV file.

### 📋 Collected data includes:

| Field | Description | Example |
|-------|-------------|---------|
| 📖 **Book Title** | Full title of the book | "A Light in the Attic" |
| 💰 **Price** | Price in GBP | "£51.77" |
| ⭐ **Rating** | Star rating (1-5) | "Three" (3 stars) |
| ✅ **Availability** | Stock status | "In stock" |

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|:----------:|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Core programming language |
| ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white) | Browser automation |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) | Data manipulation |

</div>

**Additional Tools:**
- ChromeDriver (Chrome browser automation)

---

## 🚀 How to run

### 📦 1. Clone the repository
```bash
git clone https://github.com/shiblysadik68/books-web-scraper.git
cd books-web-scraper
```

### ⚙️ 2. Install dependencies
```bash
pip install selenium pandas
```

### 🔧 3. Setup ChromeDriver

Download [ChromeDriver](https://chromedriver.chromium.org/downloads) based on your Chrome version and either:
- Add it to **PATH**, or
- Place it inside the **project folder**

> 💡 **Tip:** Check your Chrome version: `Chrome > Settings > About Chrome`

### ▶️ 4. Run the script
```bash
python web_scraper.py
```

---

## 📁 Output File

After running the script, you will get:

```
books_data.csv
```

**Sample output:**
```
Moving to next page 1....
Moving to next page 2....
...
Moving to next page 50....
No more pages to scrape!
✓ Successfully scraped 1000+ books
✓ Data saved to books_data.csv
```

---

## 🧠 What I learned

<details>
<summary><b>Click to expand learning journey</b></summary>

While working on this project, I focused on improving practical scraping skills:

- ✅ How to work with **Selenium** for real-world use cases
- ✅ Writing better **XPath selectors**
- ✅ Handling **pagination** properly
- ✅ **Debugging** when elements are not found
- ✅ Improving **performance** by reducing unnecessary delays
- ✅ Organizing scraped data using **Pandas**

</details>

---

## 🐛 Challenges I faced

<table>
<tr>
<td width="50%">

### 1️⃣ Pagination Issue

**Problem:**  
At first, the scraper failed to move to the next page. The XPath I used for the "Next" button was incorrect.

**Solution:**  
After inspecting the element again, I fixed it by targeting the correct structure:

```python
# ❌ Before
next_page = driver.find_element(By.XPATH, "//a[text()='next']")

# ✅ After
next_page = driver.find_element(By.XPATH, "//li[@class='next']/a")
```

</td>
<td width="50%">

### 2️⃣ Slow Performance

**Problem:**  
Initially, the script was slow because of extra `time.sleep()` usage.

**Solution:**  
After removing unnecessary delays, execution time dropped from **~60 minutes** to **~2-3 minutes**!

```python
# ❌ Before: Slow
time.sleep(5)  # Every book

# ✅ After: Fast
time.sleep(1)  # Only page change
```

</td>
</tr>
</table>

---

## 📈 Performance

<div align="center">

| Metric | Value |
|:------:|:-----:|
| 📄 **Total Pages** | 50 |
| 📚 **Total Books** | 1000+ |
| ⏱️ **Execution Time** | ~2–3 minutes |
| ⚡ **Speed** | ~8-10 books/second |

</div>

---

## 🔧 Project Structure

```
books-web-scraper/
│
├── 📄 web_scraper.py          # Main scraper script
├── 📊 books_data.csv          # Output data
├── 📝 README.md               # Project documentation
└── 📜 LICENSE                 # MIT License
```

---

## 🚧 Future Improvements

- [ ] Add **headless mode** for background execution
- [ ] Export data to **JSON / Excel** formats
- [ ] Add **basic UI** for easier interaction
- [ ] Improve **error handling** and recovery
- [ ] Add **multi-threading** (for learning purposes)
- [ ] Implement **progress bar** for visual feedback

---

## ⚠️ Note

> **Important:** This project is made for **learning purposes only**.  
> Always respect website rules and `robots.txt` before scraping.

---

## 👤 Author

<div align="center">

**Shibly Sadik**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/shiblysadik68)

*Open for feedback and collaboration!*

</div>

---

## 🌟 Support

<div align="center">

**If you found this project helpful, please give it a ⭐!**

It motivates me to create more projects and share knowledge.

[![Star this repo](https://img.shields.io/github/stars/shiblysadik68/books-web-scraper?style=social)](https://github.com/shiblysadik68/books-web-scraper)

</div>

---

<div align="center">

**Happy Scraping! 🚀**

Made with ❤️ by [Shibly Sadik](https://github.com/shiblysadik68)

</div>
