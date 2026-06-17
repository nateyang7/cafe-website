// src/consumable.js

export const ConsumableType = Object.freeze({
  DRINK: 0,
  FOOD: 1,
  VIENNOISERIE: 2,
});

/**
 * Represents a consumable.
 */
export class Consumable {
  /**
   * Creates a new consumable.
   *
   * @param { string } name - Consumable's name.
   * @param { string } type - Consumable's type.
   * @param { number } price - Consumable's price in euros.
   */
  constructor(name, type, price) {
    this._id = 0;
    this._name = name;
    this._type = type;
    this._price = price;
    this._id++;
  }
}
