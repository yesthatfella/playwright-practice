import { type Page } from '@playwright/test';

export class LoginPage {
    readonly page: Page;

    constructor(page: Page) {
        this.page = page;
    }

    async userSignIn(userEmail: string, password: string) {
        await this.page.getByRole('textbox', { name: 'email'}).fill(userEmail);
        await this.page.getByRole('textbox', { name: 'password'}).fill(password);
        await this.page.getByRole('button', { name: 'Sign In'}).click();
    }
}