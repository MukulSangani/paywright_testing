import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("about:blank")
    page.goto("http://adobev2.qmigrator.ai/")
    page.goto("http://adobev2.qmigrator.ai/login")
    page.get_by_placeholder("user@example.com").click()
    page.get_by_placeholder("user@example.com").fill("sunil.kamuju@quadranttechnologies.com")
    page.get_by_placeholder("License key").click()
    page.get_by_placeholder("License key").fill("s72ujtSylYOK3+JZ7vlcF7OVIxRoINwCnFiSzZiN4mPbaZYSon9r3zCOCQjSt6tZY5wXJ481PGTqoDvlCmExsmW5IeWxQTN7yiasrRYfOtaMMIx4LS+WOi7TlFB64Cc2/ywlnFnIJe+bvRVAdCAagGxx0FHKaNNDyWWaqGezII6cmT/DT6grMd9jJkhCOjmLJ4cJdoWrd7tqrOdVo7kN04DyPhas4it3N/AbXdua20eECr592CZ3EGb+dkG1+ko6")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("link", name="󱲡 Assessment").click()
    page.get_by_role("link", name="Extraction", exact=True).click()
    page.wait_for_timeout(5000) # wait for 5 seconds
    page.get_by_role("combobox").first.select_option("New")
    page.get_by_label("Default select example").select_option("1")
    page.get_by_role("combobox").nth(2).select_option("11")
    page.get_by_role("textbox").click()
    page.get_by_role("option", name="Af_demo", exact=True).click()
    page.locator(".row > div:nth-child(5)").click()
    page.get_by_role("button", name="Check Details").click()
    page.get_by_role("button", name="Execute").click()
    page.get_by_role("button", name="Code Extraction Status").click()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Refresh").click()
    page.wait_for_timeout(180*1000)
    page.get_by_role("button", name="Refresh").click()
    page.get_by_role("button", name="Refresh").click()
    page.wait_for_timeout(20000)
    page.get_by_role("button", name="Refresh").click()
    # page.get_by_role("heading", name="Code Extraction List Refresh").click()
    # page.get_by_role("button", name="Refresh").click()
    # page.get_by_role("button", name="Refresh").click()
    # page.wait_for_timeout(10000)
    # page.get_by_role("button", name="Refresh").click()
    # page.get_by_role("button", name="Refresh").click()
    # page.get_by_role("button", name="Refresh").click()
    # page.get_by_role("button", name="Refresh").click()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Refresh").click()
    page.get_by_role("button", name="Refresh").click()
    page.get_by_role("button", name="Extraction Report").click()
    page.get_by_label("Extraction Report").get_by_role("button", name="Refresh").click()
    page.wait_for_timeout(5000)
    page.get_by_label("Extraction Report").get_by_role("combobox").first.select_option("1644")
    page.get_by_label("Extraction Report").get_by_role("button", name="Refresh").click()
    page.get_by_role("button", name="Page-Activity Log").click()
    page.wait_for_timeout(5000)
    page.get_by_label("Page-Activity Log").get_by_role("combobox").select_option("1644")
    page.wait_for_timeout(5000)
    # ---------------------ALL--------------------------------------


    # ----------------------------------------- Code Scan-----------------------------------

    page.get_by_role("link", name="󱲡 Assessment").click()
    page.get_by_role("link", name="Code Scan").click()
    page.wait_for_timeout(5000)
    page.get_by_role("combobox").first.select_option("1646")
    page.get_by_label("Default select example").first.select_option("1")
    page.get_by_role("combobox").nth(2).select_option("12")
    page.get_by_role("textbox").click()
    page.get_by_role("option", name="Af_demo", exact=True).click()
    page.locator("div:nth-child(5)").click()
    page.get_by_role("button", name="Check Details").click()
    page.get_by_role("button", name="Execute").click()
    page.get_by_role("button", name="Code Scan Status").click()
    page.get_by_role("button", name="Refresh").click()
    page.wait_for_timeout(10000)
    page.get_by_role("button", name="Refresh").click()
    page.get_by_role("button", name="Code Scan Report").click()
    page.get_by_label("Code Scan Report").get_by_role("button", name="Refresh").click()
    page.wait_for_timeout(2000)
    page.get_by_label("Code Scan Report").get_by_role("combobox").first.select_option("1646")
    page.get_by_role("button", name="Page-Activity Log").click()
    # page.get_by_role("cell", name="All_Objects Assessment Ended for Af_demo schema").click()
    page.wait_for_timeout(2000)
    # --------------------------------------ALL----------------------------------



    # --------------------------

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
