export default function getResponseFromAPI() {
  // Make an asynchronous HTTP request to the API.
  return new Promise((resolve) => {
    // Resolve the promise with the response data.
    resolve({ status: 200, body: 'Success' });
  });
}
