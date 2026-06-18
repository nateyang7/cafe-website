// src/data/consumables.ts

import { ConsumableType, Consumable } from "./consumable.ts";

import expressoImg from "../assets/consumables/expresso.jpg";
import cappuccinoImg from "../assets/consumables/cappuccino.jpg";
import latteImg from "../assets/consumables/latte.jpg";

import croissantImg from "../assets/consumables/croissant.jpg";
import chocolateCroissantImg from "../assets/consumables/chocolate-croissant.jpg";
import briocheImg from "../assets/consumables/brioche.jpg";

export const consumables: Consumable[] = [
  new Consumable(expressoImg, "Expresso", ConsumableType.DRINK, 1.0),
  new Consumable(cappuccinoImg, "Cappuccino", ConsumableType.DRINK, 3.0),
  new Consumable(latteImg, "Latte", ConsumableType.DRINK, 3.5),
  new Consumable(croissantImg, "Croissant", ConsumableType.VIENNOISERIE, 4.0),
  new Consumable(
    chocolateCroissantImg,
    "Chocolate Croissant",
    ConsumableType.VIENNOISERIE,
    1.0,
  ),
  new Consumable(briocheImg, "Brioche", ConsumableType.VIENNOISERIE, 1.0),
];
