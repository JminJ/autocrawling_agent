import traceback
from playwright.async_api import async_playwright, Playwright


async def take_screenshot(url: str) -> bytes:
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
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
        
# async def take_screenshot(url: str) -> bytes:
#     playwright_cli = await async_playwright().start()
#     browser = await playwright_cli.chromium.launch()
#     try:
#         # 웹페이지 열기
#         page = await browser.new_page()
#         await page.goto(url)

#         page = await page.wait_for_selector("//body", timeout=30000)
#         screenshot = await page.screenshot()

#         return screenshot
#     except Exception as E:
#         print(traceback.format_exc())
#         print(E)
#         raise E
#     finally:
#         await browser.close()
#         await playwright_cli.stop()

# if __name__ == "__main__":
#     screenshots = take_screenshot(
#         "https://n.news.naver.com/article/584/0000028235?cds=news_media_pc&type=editn"
#     )
#     print(screenshots)

async def main():
    screenshot = await take_screenshot(url="https://n.news.naver.com/article/584/0000028235?cds=news_media_pc&type=editn")
    print(screenshot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())