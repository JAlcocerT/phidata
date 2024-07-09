// This file contains the site configuration for the theme.

import { baseUrl } from '/src/utils/baseUrl.js'; // Import the utility function

// Metadata, SEO, and Social
export const SITE_TITLE = "Manual Theme"
export const SITE_DESCRIPTION = "A documentation template for Astro"
export const SITE_URL = "https://manual.otterlord.dev"
export const SITE_DEFAULT_OG_IMAGE = "/assets/og-image.png"


// Docs Sidebar
// Define the left sidebar items here.
// The path should match the folder name in src/content/docs/
export const SIDEBAR_ITEMS = {
  "Get Started": [
    baseUrl("/docs/get-started/introduction/"),
    baseUrl("/docs/get-started/installation/"),
  ],
  "Tutorials": [
    baseUrl("/docs/tutorials/build-x/"),
  ],
  "Guides": [
    baseUrl("/docs/guides/migrate-from-z/"),
  ]
};

// Define the WEB_PATH constant
// export const WEB_PATH = "astrotest";

// Docs Sidebar
// Define the left sidebar items here.
// The path should match the folder name in src/content/docs/


// export const SIDEBAR_ITEMS = {
//   "Get Started": [
//     `/${WEB_PATH}/docs/get-started/introduction/`,
//     `/${WEB_PATH}/docs/get-started/installation/`,
//   ],
//   "Youtube Groq Summaries": [
//     `/${WEB_PATH}/docs/tutorials/build-x/`,
//   ],
//   "Guides": [
//     `/${WEB_PATH}/docs/guides/migrate-from-z/`,
//   ]
// };