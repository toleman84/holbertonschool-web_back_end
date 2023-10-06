export default function handleResponseFromAPI(promise) {
  promise.then(() => {console.log('Got a response from the API');});
  promise.then(() => ({ body: 'success', status: 200 }));
  promise.catch(() => new Error());
}
