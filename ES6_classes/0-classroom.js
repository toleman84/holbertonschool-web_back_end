export default class ClassRoom {
  constructor(maxStudentsSize) {
    /* eslint-disable */
    this._maxStudentsSize = maxStudentsSize;
    /* eslint-enable */
  }

  get maxStudentsSize() {
    return this._maxStudentsSize;
  }
}
