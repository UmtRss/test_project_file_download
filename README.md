# 📥 Selenium PyTest Project 7 – File Download Test

## 📁 Project Name: `test_project_file_download`

This test automation project demonstrates how to verify that a file is successfully downloaded using Selenium by checking its presence in a custom download directory.




## 🧪 Test Scenario:

1. Configure Chrome to use a custom download folder (e.g. `/downloads`)
2. Navigate to the test page
3. Click on a downloadable file (e.g. `some-file.txt`)
4. Wait briefly for the file to download
5. Assert that the file now exists in the specified directory



## 📂 Files

| File Name              | Description                          |
|------------------------|--------------------------------------|
| `test_file_download.py` | Automates the download verification  |
| `downloads/`           | Folder where the downloaded file is saved |



## 🛠️ Tools & Technologies:
- Python
- Selenium WebDriver
- PyTest
- Chrome Options



## 🎯 Goal
To verify file download functionality using custom download paths and filesystem checks with Selenium.
