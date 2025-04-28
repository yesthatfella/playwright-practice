import { test, expect } from '@playwright/test';
import { SearchBar } from './pageObjects/SearchBar.ts';
import { SearchResultsPage } from './pageObjects/SearchResults';
import { TestData as data} from "./testData/data.json"


test.beforeEach(async ( { page, baseURL } ) => {
  await page.goto(baseURL);
});

test('Guest User Checkouts an Order', async ({ page }) => {
  let productTitle = data.regularProduct.title;
  let searchBar = new SearchBar(page);
  searchBar.searchProduct(productTitle);

  let searchResultsPage = new SearchResultsPage(page);
  searchResultsPage.addProductToCard(productTitle);

  await expect(page.getByText(productTitle)).toBeVisible();
});