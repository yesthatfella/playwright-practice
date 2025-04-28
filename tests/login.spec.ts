import { test, expect } from '@playwright/test';
import { LoginPage } from './pageObjects/Login';
import { TestData as data} from "./testData/data.json"

test.beforeEach(async ({ page, baseURL }) => {
  await page.goto(baseURL);
});

test('User is able to sign in', async ({ page }) => {
  let loginPage = new LoginPage(page);
  loginPage.userSignIn(data.userSignIn.email, data.userSignIn.password);

  await expect(page.getByText("Welcome to Admin Home")).toBeVisible();
});

test('User with wrong credentials sees error message ', async ({ page }) => {
  let loginPage = new LoginPage(page);
  loginPage.userSignIn(data.userSignIn.email, 'wrongPa$$word');

  await expect(page.locator('#loginError')).toHaveText('Invalid Credentials');
});