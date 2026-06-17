// src/menu.js

import { ConsumableType, Consumable } from "./consumable.js";

const consumables = [
  new Consumable("Expresso", ConsumableType.DRINK, 1.0),
  new Consumable("Cappuccino", ConsumableType.DRINK, 3.0),
  new Consumable("Latte", ConsumableType.DRINK, 3.5),
  new Consumable("Quiche", ConsumableType.FOOD, 4.0),
  new Consumable("Croque-Monsieur", ConsumableType.FOOD, 4.0),
  new Consumable("Caesar Salad", ConsumableType.FOOD, 8.0),
  new Consumable("Croissant", ConsumableType.VIENNOISERIE, 4.0),
  new Consumable("Chocolate Croissant", ConsumableType.VIENNOISERIE, 1.0),
  new Consumable("Brioche", ConsumableType.VIENNOISERIE, 1.0),
];

// Sections id
const coffeesContainer = document.getElementById("coffees-container");
const foodContainer = document.getElementById("food-container");
const viennoiseriesContainer = document.getElementById(
  "viennoiseries-container",
);

/**
 * Add consumables of a type to a container of the HTML page.
 *
 * @param { HTMLElement } container - Element ID of the container of the HTML page.
 * @param { ConsumableType } typeToDisplay - Type of consumable to display only.
 */
function addConsumables(container, typeToDisplay) {
  for (const consumable of consumables) {
    if (consumable._type === typeToDisplay) {
      let consumableDiv = document.createElement("div");
      consumableDiv.id = consumable._name.toLocaleLowerCase();

      let consumableH3 = document.createElement("h3");
      consumableH3.textContent = consumable._name;
      consumableDiv.appendChild(consumableH3);

      container.appendChild(consumableDiv);
    }
  }
}

addConsumables(coffeesContainer, ConsumableType.DRINK);
addConsumables(foodContainer, ConsumableType.FOOD);
addConsumables(viennoiseriesContainer, ConsumableType.VIENNOISERIE);
