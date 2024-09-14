from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import os
import requests
import csv


def setup_driver() -> webdriver:
    options: Options = Options()
    options.headless = True
    options.add_argument("--incognito")
    driver: webdriver = webdriver.Chrome(options=options)
    driver.implicitly_wait(7)
    return driver


def navigate_to_repository(driver: webdriver, repo_name: str) -> None:
    url: str = f"https://github.com/code-423n4/{repo_name}"
    driver.get(url)


def check_report_md_exists(driver: webdriver) -> str:
    try:
        report_link = driver.find_element(
            By.XPATH, '//a[contains(@href, "report.md")]')
        report_url = report_link.get_attribute('href')
        # modify the URL to access the raw content
        raw_report_url = report_url.replace(
            'github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
        return raw_report_url
    except NoSuchElementException:
        return None


def download_and_save_report(report_url: str, repo_name: str) -> None:
    response = requests.get(report_url)
    report_content = response.text

    # save the content to a file
    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open(f"reports/{repo_name}_report.md", 'w', encoding='utf-8') as file:
        file.write(report_content)


def save_to_csv(data: list) -> None:
    with open('data/repository_reports.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['repository_name', 'report_available']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    # load repository names from the txt file
    with open('data/findings_repositories_code4rena.txt', 'r', encoding='utf-8') as file:
        repo_names: list = [line.strip() for line in file.readlines()]

    driver = setup_driver()
    csv_data: list = []

    try:
        for repo_name in repo_names:
            print(f"Processing repository: {repo_name}")
            navigate_to_repository(driver, repo_name)
            time.sleep(2)  # give some time for the page to load

            report_url = check_report_md_exists(driver)
            if report_url:
                print(f"Found report.md in {repo_name}. Downloading...")
                download_and_save_report(report_url, repo_name)
                csv_data.append(
                    {'repository_name': repo_name, 'report_available': 1})
            else:
                print(f"No report.md found in {repo_name}.")
                csv_data.append(
                    {'repository_name': repo_name, 'report_available': 0})

        # save the CSV data
        save_to_csv(csv_data)
        print("CSV file saved as 'repository_reports.csv'.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
