import traceback
from playwright.sync_api import sync_playwright


def take_screenshot(url:str)->bytes:
    playwright_cli = sync_playwright().start()
    browser = playwright_cli.chromium.launch()
    try:
        # 웹페이지 열기
        page = browser.new_page()
        page.goto(url)
        
        page = page.wait_for_selector("//body", timeout=2000)
        screenshot = page.screenshot()

        return screenshot
    except Exception as E:
        print(traceback.format_exc())
        print(E)
        raise E
    finally:
        browser.close()
        playwright_cli.stop()

if __name__ == "__main__":
    take_screenshot('https://n.news.naver.com/article/584/0000028235?cds=news_media_pc&type=editn')