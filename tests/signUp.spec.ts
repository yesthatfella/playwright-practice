import { test, expect } from '@playwright/test';
import { SignUpPage } from './pageObjects/Registration';
import { TestData as data} from "./testData/data.json"


test.beforeEach(async ({ page, baseURL }) => {
  await page.goto(baseURL);
});

test('User is able to Sign Up', async ({ page }) => {
  let signUpPage = new SignUpPage(page);
  signUpPage.userSignUp(data.userRegistration.name, data.userRegistration.lastName, data.userRegistration.email, data.userRegistration.emailDomain, data.userRegistration.password);

  await expect(page.getByText("User successfully registered")).toBeVisible();
});

