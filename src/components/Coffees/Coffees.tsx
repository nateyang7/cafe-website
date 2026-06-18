// src/components/Coffees/Coffees.tsx

import { ConsumableType } from "../../data/consumable";
import { consumables } from "../../data/consumables";
import styles from "./Coffees.module.css";

export default function Coffees() {
  return (
    <section id="coffees" className={styles.coffees}>
      <h1>Coffees</h1>

      <div className={styles.consumablesContainer}>
        {consumables
          .filter((coffee) => coffee.type === ConsumableType.DRINK)
          .map((coffee) => (
            <div className="consumable" key={coffee.id}>
              <img
                src={coffee.image}
                alt={coffee.name}
                className={styles.consumableShowcase}
              />
              <ul>
                <li>{coffee.name}</li>
                <li>{coffee.price} €</li>
              </ul>
            </div>
          ))}
      </div>
    </section>
  );
}
