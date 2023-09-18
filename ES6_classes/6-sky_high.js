import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  // Override the evacuationWarningMessage method.
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
