export default function loadBalancer(chinaDownload, USDownload) {
  const winnerPromise = Promise.race([chinaDownload, USDownload]);

  return winnerPromise.then((value) => value);
}
