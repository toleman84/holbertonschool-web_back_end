import { uploadPhoto, createUser } from "./utils";

export default function handleProfileSignup() {
  // Create a promise chain.
  Promise.all([uploadPhoto(), createUser()])
    .then((responses) => {
      // Get the response bodies from the promises.
      const [photoUrl, user] = responses;

      // Log the first name, last name, and photo URL to the console.
      console.log(`${photoUrl} ${user.firstName} ${user.lastName}`);
    })
    .catch((error) => {
      // Log an error message to the console.
      console.log("Signup system offline");
    });
}
