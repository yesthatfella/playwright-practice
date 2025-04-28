import {type Locator, type Page} from '@playwright/test'

export class ScrollHandler {
    readonly page: Page;

    constructor(page: Page) {
        this.page = page;
    }

    async getAutomation(element: Locator) {
        let scrollCount = 1;

        // Below logic ensures the ViewPort is properly located to fill-up Order details
        // Useful when form content is lazy-loading based
        while(scrollCount<=20){
            console.info("Scroll Count: "+scrollCount)

            if(await element.isVisible()){
                break;
            } else{
                await this.page.evaluate(() => window.scrollBy(0, 500));
                await this.page.waitForTimeout(200);
            }

            scrollCount++;
        }
    }
}