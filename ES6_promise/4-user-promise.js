export default function signUpUser(firstName, lastName) {
  return new Promise((resolve) => {
    // Create a new user object
    const user = {
      firstName,
      lastName,
    };

    // Resolve the promise with the user object
    resolve(user);
  });
}
