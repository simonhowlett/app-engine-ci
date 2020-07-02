const puppeteer = require('puppeteer');
var testApp = "http://127.0.0.1:8080/";

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(testApp);
    await page.screenshot({ path: 'example.png' });

    await browser.close();
})();