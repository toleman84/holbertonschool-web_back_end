export default function handleResponseFromAPI(promise) {
  promise.then( () => console.log('Got a response from the API'));
  promise.then(
    () => ({
      status: 200,
      body: 'success',
      })
    );
  promise.catch(() => new Error() );
}
