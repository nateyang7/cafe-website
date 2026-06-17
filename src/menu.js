// src/menu.js

import { ConsumableType, Consumable } from "./consumable.js";

const expressoImg = "../assets/consumables/expresso.jpg";
const cappuccinoImg = "../assets/consumables/cappuccino.jpg";
const latteImg = "../assets/consumables/latte.jpg";

const quicheImg = "../assets/consumables/quiche.jpg";
const croqueMonsieurImg = "../assets/consumables/croque-monsieur.jpg";
const cesarSaladImg = "../assets/consumables/cesar-salad.jpg";

const croissantImg = "../assets/consumables/croissant.jpg";
const chocolateCroissantImg = "../assets/consumables/chocolate-croissant.jpg";
const briocheImg = "../assets/consumables/brioche.jpg";

const consumables = [
  new Consumable(expressoImg, "Expresso", ConsumableType.DRINK, 1.0),
  new Consumable(cappuccinoImg, "Cappuccino", ConsumableType.DRINK, 3.0),
  new Consumable(latteImg, "Latte", ConsumableType.DRINK, 3.5),
  new Consumable(quicheImg, "Quiche", ConsumableType.FOOD, 4.0),
  new Consumable(
    croqueMonsieurImg,
    "Croque-Monsieur",
    ConsumableType.FOOD,
    4.0,
  ),
  new Consumable(cesarSaladImg, "Cesar Salad", ConsumableType.FOOD, 8.0),
  new Consumable(croissantImg, "Croissant", ConsumableType.VIENNOISERIE, 4.0),
  new Consumable(
    chocolateCroissantImg,
    "Chocolate Croissant",
    ConsumableType.VIENNOISERIE,
    1.0,
  ),
  new Consumable(briocheImg, "Brioche", ConsumableType.VIENNOISERIE, 1.0),
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
      // Create the div to contain the consumable informations
      let consumableDiv = document.createElement("div");
      consumableDiv.id = consumable._name.toLocaleLowerCase();
      consumableDiv.className = "consumable";

      // Create the image for the consumable
      let consumableImg = document.createElement("img");
      consumableImg.src = consumable._image;
      consumableImg.alt = consumable._name;
      consumableDiv.appendChild(consumableImg);

      // Create the header for the name of the consumable
      let consumableH3 = document.createElement("h3");
      consumableH3.textContent = `${consumable._name} : ${consumable._price} €`;
      consumableDiv.appendChild(consumableH3);

      container.appendChild(consumableDiv);
    }
  }
}

addConsumables(coffeesContainer, ConsumableType.DRINK);
addConsumables(foodContainer, ConsumableType.FOOD);
addConsumables(viennoiseriesContainer, ConsumableType.VIENNOISERIE);

console.log(consumables);
