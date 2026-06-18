// src/components/Coffees/Coffees.tsx

import { ConsumableType } from "../data/consumable";
import { consumables } from "../data/consumables";

export default function Coffees() {
  return (
    <section id="coffees" className="foodSection">
      <h1>
        {"\u{2615}"} Coffees {"\u{2615}"}
      </h1>

      <div className="foodContainer">
        {consumables
          .filter((coffee) => coffee.type === ConsumableType.DRINK)
          .map((coffee) => (
            <div className="foodDiv" key={coffee.id}>
              <img src={coffee.image} alt={coffee.name} />
              <p>
                <strong>{coffee.name}</strong>: {coffee.price} €
              </p>
            </div>
          ))}
      </div>
    </section>
  );
}
