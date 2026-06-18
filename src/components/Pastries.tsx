// src/components/Pastries/Pastries.tsx

import { ConsumableType } from "../data/consumable.ts";
import { consumables } from "../data/consumables.ts";

export default function Pastries() {
  return (
    <section id="pastries" className="foodSection">
      <h1>
        {"\u{1F950}"} Pastries {"\u{1F950}"}
      </h1>

      <div className="foodContainer">
        {consumables
          .filter((pastry) => pastry.type === ConsumableType.VIENNOISERIE)
          .map((pastry) => (
            <div className="foodDiv" key={pastry.id}>
              <img src={pastry.image} alt={pastry.name} />
              <p>
                <strong>{pastry.name}</strong>: {pastry.price} €
              </p>
            </div>
          ))}
      </div>
    </section>
  );
}
