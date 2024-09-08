import traceback
from playwright.async_api import async_playwright, Playwright


async def take_screenshot(url: str) -> bytes:
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=True)
    try:
        page = await browser.new_page()
        await page.goto(url)
        # await page.wait_for_selector("//body", timeout=30000)
        screenshot = await page.screenshot(full_page=True)
        return screenshot
    except Exception as E:
        print(traceback.format_exc())
        print(E)
        raise E
    finally:
        await browser.close()
        await playwright.stop()
