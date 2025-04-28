import { type Page } from '@playwright/test';

export class SearchResultsPage {
    readonly page: Page;

    constructor(page: Page) {
        this.page = page;
    }

    async addProductToCard(productName: string) {
        // Below logic asumes that the button is located inside of a span down in Product name structure
        await this.page.locator('#results-container div.item').getByText(productName).locator("span > button").click();
    }
    
    async openProductDetailsPage(productName: string) {
        // Below logic asumes that the button is located inside of a span down in Product name structure
        await this.page.locator('#results-container div.item').getByText(productName).click();
    }
}