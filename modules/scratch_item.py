from playwright.sync_api import sync_playwright, Page


def search_tag(page: Page, block: str, name: str):
    elements = page.locator(
        f"xpath={block}"
    ).all()

    for el in elements:
        for inner in el.locator("xpath=./div/div").all():
            element1 = inner.locator("xpath=.//span").first
            element2 = inner.locator("xpath=.//span[position() = 2]").first

            if element1.text_content(timeout=1000).strip().find(name) != -1:

                if element2.locator("xpath=.//a").text_content(timeout=1000):
                    return element2.locator("xpath=.//a").text_content()
                return element2.text_content()
    return None

def collect_characteristics(page: Page, block: str):
    characteristics = {}

    for element in page.locator(block).all():
        element1 = element.locator("xpath=.//div/div/span").first
        element2 = element.locator("xpath=.//div/div/span[position()=2]").first

        characteristics[element1.text_content(timeout=1000).strip()] \
            = element2.text_content(timeout=1000).strip()
    return characteristics

def getItem(url: str):
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(
                headless=False
            )  # If headless=True, browser ll not show
            page = browser.new_page()


            page.goto(url, wait_until="load")

            try:
                page.locator("xpath=//input[@class='quick-search-input']").all()[1].fill(
                    "Apple iPhone 15 128GB Black"
                )
            except Exception as e:
                print(e)

            page.locator("//*[contains(@class, 'search-form')][contains(@class, 'header-search-form')]"
              "/form/input[position()=2]").all()[1].click()

            page.locator("xpath=//div[@class='br-pp-imadds']/div/a").all()[0].click()

            title = page.locator("xpath=//*[@id='br-pr-1']/h1").text_content().strip()

            colour = search_tag(page, "//div[@class='br-pr-chr-item']", "Колір")
            memory = search_tag(page, "//div[@class='br-pr-chr-item']", "Вбудована")

            price = page.locator("xpath=//div[@class='price-wrapper']/span").first.text_content().strip()

            try:
                action_price = page.locator("xpath=//span[@class='red-price']").text_content(timeout=1000)
            except Exception:
                action_price = None

            photos = page.locator("xpath=//*[@class='slick-track']/div/img").all()

            links = [photo.get_attribute("src") for photo in photos]

            try:
                code = page.locator("xpath=//span[@class='br-pr-code-val']").first.text_content(timeout=1000)
            except Exception:
                code = None

            try:
                reviews_count = page.locator(
                    "xpath=//a[@href='#reviews-list' and @class='scroll-to-element']/span"
                ).first.text_content(timeout=1000)
            except Exception:
                reviews_count = None

            screen_size = search_tag(page, "//div[@class='br-pr-chr-item']", "Діагональ екрану")
            screen_power = search_tag(page, "//div[@class='br-pr-chr-item']", "Роздільна здатність екрану")

            chars = collect_characteristics(page, "//div[@class='br-pr-chr-item']")

            page.close()

            return {
                "title": title,
                "colour": colour,
                "memory": memory,
                "price": price,
                "action_price": action_price,
                "photo_links": links,
                "code": code,
                "reviews_count": reviews_count,
                "screen_size": screen_size,
                "screen_power": screen_power,
                "characteristics": chars,
            }

        except Exception as e:
            print(e)
