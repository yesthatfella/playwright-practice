import { type Page } from '@playwright/test';

export class SignUpPage {
    readonly page: Page;

    constructor(page: Page) {
        this.page = page;
    }

    async userSignUp(name: string, lastName: string, email: string, emailDomain: string, password: string) {
        await this.page.getByRole('textbox', { name: 'userName'}).fill(name);
        await this.page.getByRole('textbox', { name: 'userLastName'}).fill(lastName);
        let randomizedEmail = `${email}${Date.now()}${emailDomain}`;
        await this.page.getByRole('textbox', { name: 'email'}).fill(randomizedEmail);
        await this.page.getByRole('textbox', { name: 'password'}).fill(password);
        await this.page.getByRole('button', { name: 'Sign Up'}).click();
    }
}