import { expect, type Page } from '@playwright/test';
import { ScrollHandler } from '../utils/scrollHandler';

export class PaymentPage {
    readonly page: Page;

    constructor(page: Page) {
        this.page = page;
    }

    async scrollIntoOrderDetails() {
        let payButton = this.page.getByRole('button', { name: 'Confirm my Order'});
        payButton.scrollIntoViewIfNeeded();
        new ScrollHandler(this.page).scrollBySteps(payButton);

        await expect(this.page.getByRole('heading', {name: 'Order Details'})).toBeVisible();
    }
    async payOrder(name: string, card: string, cvc: string) {
        this.scrollIntoOrderDetails();
        await this.page.getByRole('textbox', { name: 'name'}).fill(name);
        await this.page.getByRole('textbox', { name: 'card_number'}).fill(card);
        await this.page.getByRole('textbox', { name: 'cvc'}).fill(cvc);
        await this.page.getByRole('button', { name: 'Confirm My Order'}).click();
    }
}