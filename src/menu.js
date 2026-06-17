// src/menu.js

import { ConsumableType, Consumable } from "./consumable.js";

const consumables = [
  new Consumable("Expresso", ConsumableType.DRINK, 1.0),
  new Consumable("Cappuccino", ConsumableType.DRINK, 3.0),
  new Consumable("Latte", ConsumableType.DRINK, 3.5),
];

// Sections id
const coffeesContainer = document.getElementById("coffees-container");
const food = document.getElementById("food");
const viennoiseries = document.getElementById("viennoiseries");

// List of coffees
for (const consumable of consumables) {
  if (consumable._type === ConsumableType.DRINK) {
    let coffeeDiv = document.createElement("div");
    coffeeDiv.id = consumable._name.toLocaleLowerCase();

    let coffeeH3 = document.createElement("h3");
    coffeeH3.textContent = consumable._name;
    coffeeDiv.appendChild(coffeeH3);

    coffeesContainer.appendChild(coffeeDiv);
  }
}
