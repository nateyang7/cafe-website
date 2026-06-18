// src/data/consumable.ts

export const ConsumableType = {
  DRINK: 0,
  FOOD: 1,
  VIENNOISERIE: 2,
} as const;

export type ConsumableType =
  (typeof ConsumableType)[keyof typeof ConsumableType];

/**
 * Represents a consumable.
 */
export class Consumable {
  static ID: number = 0;
  private _id: number;
  private _image: string;
  private _name: string;
  private _type: ConsumableType;
  private _price: number;

  /**
   * Creates a new consumable.
   *
   * @param { string } image - Consumable's image.
   * @param { string } name - Consumable's name.
   * @param { string } type - Consumable's type.
   * @param { number } price - Consumable's price in euros.
   */

  constructor(
    image: string,
    name: string,
    type: ConsumableType,
    price: number,
  ) {
    Consumable.ID++;
    this._id = Consumable.ID;
    this._image = image;
    this._name = name;
    this._type = type;
    this._price = price;
  }

  get id(): number {
    return this._id;
  }

  get image(): string {
    return this._image;
  }

  get name(): string {
    return this._name;
  }

  get type(): ConsumableType {
    return this._type;
  }

  get price(): number {
    return this._price;
  }
}
