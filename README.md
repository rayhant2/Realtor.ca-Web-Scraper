# Realtor.ca-Web-Scraper
With thoughts of moving within Toronto, scrolling through countrless pages is tiring; especially with new properties constntly being added to the market. This Python scraper goes through the most recent 600 postings within Toronto, making real-estate listings local to Toronto much easier.

<br>

## Overview
This Python script utilizes Selenium and Undeteced_Chromedriver to scrape property data from Realtor.ca. It is designed to extract key information such as address, price, bedrooms, and bathrooms, and export all the data into an Excel Spreadsheet. 
<br>
<br>

## Prerequisites

Before running the script, make sure the following is installed:
* Python (ideally 3.9 or newer)
* Openpyxl
* Selenium / Selenium-Wire
* Undetected-Chromedriver
* Pandas

You can install the required packages using the following:

```bash
pip install openpyxl selenium selenium-wire undetected-chromedriver pandas
```


## Usage

1. Clone the repository:
```bash
git clone https://github.com/rayhant2/Realtor.ca-Web-Scraper.git
```
2. Run the script:
```bash
python app.py
```
The script will open a Chrome browser, scrape the property data, and export it to "properties.xlsx".
<br>
<br>

## Issues & Contributions

- The scraper only goes through the first, most recent 600 properties (50 pages x 12 listings); if there are more pages with properties listings, they are neglected - need to find a way to scrape all listings based on the number of pages available
- For now, this property scraper only works for the city Toronto, ON - need to find a way to optimize the scraper to work for any cty/region specified
- **Other future updates include:** Automation, Filtering results based on price/beds/baths, Including links,lot size, etc. in the spreadsheet, and more

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
<br>
<br>

## Sample Output

An example of how the property data is stored can be found [here](https://docs.google.com/spreadsheets/d/1aM_vApPpdhtAUYlaJLqrn1uvG76cN5xt/edit?usp=sharing&ouid=110438645510711714527&rtpof=true&sd=true)
<br>
![Image](/output/properties.jpg)
<br>
<br>

## License
MIT
