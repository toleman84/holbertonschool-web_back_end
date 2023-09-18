// import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }

    if (currency instanceof Currency) {
      throw new TypeError('Currency must be an instance of the Currency class');
    }

    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(amount) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }

    this._amount = amount;
  }

  get currency() {
    return this._currency;
  }

  set currency(currency) {
    if (currency instanceof Currency) {
      throw new TypeError('Currency must be an instance of the Currency class');
    }

    this._currency = currency;
  }

  displayFullPrice() {
    const { _name, _code } = this._currency;
    return `${this._amount} ${_name} (${_code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
