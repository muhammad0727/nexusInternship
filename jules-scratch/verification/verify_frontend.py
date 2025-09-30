from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the React app served by Django
    page.goto("http://127.0.0.1:8000/")

    # Wait for the main header to be visible
    expect(page.get_by_role("heading", name="Nexus Internship")).to_be_visible()

    # Wait for the component headers to be visible
    expect(page.get_by_role("heading", name="Users")).to_be_visible()
    expect(page.get_by_role("heading", name="Meetings")).to_be_visible()
    expect(page.get_by_role("heading", name="Documents")).to_be_visible()
    expect(page.get_by_role("heading", name="Payments")).to_be_visible()

    # Take a screenshot
    page.screenshot(path="jules-scratch/verification/verification.png")

    # Clean up
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)