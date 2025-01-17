import asyncio
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:
    # create browser instance
    browser = pw.firefox.launch(
        # we can choose either a Headful (With GUI) or Headless mode:
        headless=False,
        firefox_user_prefs={
            "pdfjs.disabled": False,  # Enable built-in PDF viewer
            "browser.download.always_ask_before_handling_new_types": False,
            "plugin.disable_full_page_plugin_for_types": "application/pdf"
        }
    )
    # create context
    # using context we can define page properties like viewport dimensions
    context = browser.new_context(
        # most common desktop viewport is 1920x1080
        viewport={"width": 1320, "height": 1080}
    )
    # create page aka browser tab which we'll be using to do everything
    page = context.new_page()

    # navigate to the specific page
    page.goto(f"https://arxiv.org/pdf/2401.04088")

    # wait for the page to load completely
    page.wait_for_load_state('networkidle')

    # wait for the text layer to be visible
    page.wait_for_selector('div.textLayer', state='visible')

    # additional wait to ensure the text content is fully loaded
    time.sleep(2)

    # get the total number of pages
    total_pages = int(page.evaluate("""
        () => {
            const numPagesElement = document.querySelector('#numPages');
            return numPagesElement ? parseInt(numPagesElement.getAttribute('data-l10n-args').match(/"pagesCount":(\d+)/)[1]) : 0;
        }
    """))

    all_text_content = []

    for page_number in range(1, total_pages + 1):
        # Scroll to the page
        page.evaluate(f"""
            () => {{
                const pageElement = document.querySelector('div.page[data-page-number="{page_number}"]');
                if (pageElement) {{
                    pageElement.scrollIntoView();
                }}
            }}
        """)

        # Wait for the text layer of the current page to be visible
        page.wait_for_selector(f'div.page[data-page-number="{page_number}"] div.textLayer', state='visible')

        # additional wait to ensure the text content is fully loaded
        time.sleep(2)

        # extract the text content of the current page
        text_content = page.evaluate("""
            (page_number) => {
                const pageElement = document.querySelector(`div.page[data-page-number="${page_number}"] div.textLayer`);
                const textSpans = pageElement ? pageElement.querySelectorAll('span') : [];
                let text = '';
                textSpans.forEach(span => {
                    text += span.innerText + ' ';
                });
                return text.trim();
            }
        """, page_number)

        # print the text content of the current page
        print(f"Page {page_number}:\n{text_content}\n")

        # save the text content to a file
        with open('arxiv_3.txt', 'a', encoding='utf-8', errors='ignore') as f:
            f.write(f"Page {page_number}:\n{text_content}\n")

        all_text_content.append(text_content)

    # keep the browser open for a while to inspect
    time.sleep(10)

# CLEANUP TODO: REMOVING PERCENTAGES, UNRECOGNIZED CHARACTERS, URLS AND KEYWORDS LIKE "CODE:", "FIGURE:", "GITHUB:" AND "WEBPAGE:"
