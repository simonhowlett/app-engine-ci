const puppeteer = require('puppeteer');
var testApp = "http://127.0.0.1:8080/";

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(testApp);

    // Get the "viewport" of the page, as reported by the page.
    const dimensions = await page.evaluate(() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio
        };
    });

    console.log('Dimensions:', dimensions);

    await browser.close();
})();