import { expect, type Page} from '@playwright/test';

export class ProducDetailsPage {
    readonly page: Page;

    constructor(page: Page) {
        this.page = page;
    }

    async addItemToCart(productTitle: string) {
        // This would throw an assertion error in case the Page does not display Product title
        await expect(this.page.getByText(productTitle)).toBeVisible();
        await this.page.getByRole('button', { name: 'Add to Cart'}).click();
    }
}