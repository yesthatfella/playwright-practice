import { type Locator, type Page, expect } from '@playwright/test';

export class HomePage {
    readonly page: Page;

    constructor(page: Page) {
        this.page = page;
    }

    async scrollToElementIfLazyLoading(element: Locator) {
        let scrollCount = 1;
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