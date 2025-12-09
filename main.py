import time

from playwright.sync_api import sync_playwright


def getItem():
    with sync_playwright() as p:
        try:

            browser = p.chromium.launch(
                headless=False
            )  # Если headless=True, браузер не будет отображаться
            page = browser.new_page()

            page.goto("https://brain.com.ua/", wait_until="load")

            page.locator("input.quick-search-input").all()[1].fill(
                "Apple iPhone 15 128GB Black"
            )
            page.locator("input[type=submit].qsr-submit").click()
            page.locator("div.br-pp-desc.br-pp-ipd-hidden > a").all()[0].click()

            title = page.locator("h1.main-title").text_content()

            colour = page.locator(
                "div.series-item.series-color.current.active > a > ul > li > div"
            ).get_attribute("style")

            memory = page.locator(
                "div.br-pr-chr-item:nth-of-type(4) > div > div > span > a"
            ).text_content()

            price = page.locator(
                "div.br-pr-price.main-price-block > div > div > span"
            ).text_content()

            action_price = page.locator("div.price-wrapper > span.red-price")
            action_price = action_price.text_content() if action_price else None

            photos = page.locator(".slick-track > div > img > img").all()
            links = [photo.get_attribute("src") for photo in photos]

            code = page.locator("span.br-pr-code-val").all()
            if code:
                code = code[0].text_content()

            reviews_count = page.locator(
                "a[href='#reviews-list'].scroll-to-element"
            ).all()
            if reviews_count:
                reviews_count = reviews_count[0].text_content()

            screen_size = page.locator(
                "div.br-pr-chr-item:nth-child(2) > div > div:nth-child(2) > span:nth-child(2) > a"
            )
            if screen_size:
                screen_size = screen_size.text_content()

            screen_power = page.locator(
                "div:nth-child(2) > div > div:nth-child(3) > span:nth-child(2) > a"
            )
            if screen_power:
                screen_power = screen_power.text_content()

            chars = {}

            blocks = page.locator("div.br-pr-chr-item").all()
            for block in blocks:
                chars[block.locator("div > div > span:first-of-type")] = block.locator(
                    "div > div > span:nth-of-type(2) > a"
                ).text_content()

            page.close()

            return {
                "title": title,
                "colour": colour,
                "memory": memory,
                "price": price,
                "action_price": action_price,
                "links": links,
                "code": code,
                "reviews_count": reviews_count,
                "screen_size": screen_size,
                "screen_power": screen_power,
                "chars": chars,
            }
        except Exception as e:
            print(e)
