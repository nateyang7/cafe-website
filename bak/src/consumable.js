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
   * @param { string } image - Consumable's image.
   * @param { string } name - Consumable's name.
   * @param { string } type - Consumable's type.
   * @param { number } price - Consumable's price in euros.
   */
  static id = 0;

  constructor(image, name, type, price) {
    Consumable.id++;
    this._id = Consumable.id;
    this._image = image;
    this._name = name;
    this._type = type;
    this._price = price;
  }
}
