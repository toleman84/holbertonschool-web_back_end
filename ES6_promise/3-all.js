import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  // Create a promise chain.
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      // Get the response bodies from the promises.
      const { body } = photoResponse;
      const { firstName, lastName } = userResponse;

      // Log the first name, last name, and photo URL to the console.
      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch(() => {
      // Log an error message to the console.
      console.log('Signup system offline');
    });
}
