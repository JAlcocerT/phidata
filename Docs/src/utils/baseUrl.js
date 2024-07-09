// src/utils/baseUrl.js
export function baseUrl(path) {
    const basePath = '/astrotest'; // Set your base path here - Example when deploying to GH Pages
    return `${basePath}${path}`;
  }