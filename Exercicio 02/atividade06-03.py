
from playwright.sync_api import sync_playwright

def main():
    query = 'tempo de manaus'
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        content = browser.new_context()
        page = content.new_page()
        
        page.goto('https://www.google.com', wait_until = 'domcontentloaded')
        
        try:
            page.locator('button:has-text("aceitar tudo")').click(timeout=1000)
        except:
            pass
        
        page.fill('//*[@id="APjFqb"]', query)
        page.keyboard.press('Enter')
        
        page.wait_for_selector('#search', timeout=30000)
        page.screenshot(path='result_google.png', full_page=True)
        
        content.close()
        browser.close()
        
if __name__ == '__main__':
    main()
        
    