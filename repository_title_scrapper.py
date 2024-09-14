from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import time


def setup_driver() -> webdriver:
    options: Options = Options()
    options.headless = True
    options.add_argument("--incognito")
    driver: webdriver = webdriver.Chrome(options=options)
    driver.implicitly_wait(7)
    return driver


def navigate_to_page(driver: webdriver, url: str) -> None:
    driver.get(url)


def extract_repositories(driver: webdriver) -> list:
    repo_titles: list = []
    while True:
        try:
            repos = driver.find_elements(
                # repository class
                By.CSS_SELECTOR, 'span.Text-sc-17v1xeu-0.gPDEWA')
            for repo in repos:
                title: str = repo.text.strip()
                # checking if 'findings' is in title
                if 'findings' in title.lower():
                    repo_titles.append(title)

            if not navigate_to_next_page(driver):
                break
        except StaleElementReferenceException:
            continue
    return repo_titles


def navigate_to_next_page(driver: webdriver) -> bool:
    try:
        # find to click the next button
        next_link = driver.find_element(By.XPATH,
                                        '//a[@rel="next"]')
        if next_link and not next_link.get_attribute('aria-disabled') == 'true':
            next_link.click()
            time.sleep(5)
            return True
        else:
            return False
    except:
        print("Reached the last page or 'Next' link not found.")
        return False


def write_titles_to_file(titles: list) -> None:
    with open('findings_repositories_code4rena.txt', 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(title + '\n')


def main() -> None:
    driver = setup_driver()
    navigate_to_page(driver, "https://github.com/orgs/code-423n4/repositories")
    try:
        repo_titles = extract_repositories(driver)
        if repo_titles:
            print(f"Collected {len(repo_titles)} Repository Titles")
            write_titles_to_file(repo_titles)
        else:
            print("No matching repositories found.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
