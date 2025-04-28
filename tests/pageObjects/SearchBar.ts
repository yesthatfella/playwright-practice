import { type Page } from '@playwright/test';

export class SearchBar {
    readonly page: Page;

    constructor(page: Page) {
        this.page = page;
    }

    async searchProduct(productName: string) {
        await this.page.locator("textarea[name='q']").fill(productName);
        await this.page.getByRole('button', { name: 'Search'}).click();
    }
}