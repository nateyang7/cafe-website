// src/components/Coffees/Coffees.tsx

import { ConsumableType } from "../../data/consumable";
import { consumables } from "../../data/consumables";
import styles from "./Coffees.module.css";

export default function Coffees() {
  return (
    <section id="coffees" className={styles.coffees}>
      <h1>
        {"\u{2615}"} Coffees {"\u{2615}"}
      </h1>

      <div className={styles.coffeesContainer}>
        {consumables
          .filter((coffee) => coffee.type === ConsumableType.DRINK)
          .map((coffee) => (
            <div className={styles.coffeeDiv} key={coffee.id}>
              <img
                src={coffee.image}
                alt={coffee.name}
                className={styles.coffeeImg}
              />
              <p>
                <strong>{coffee.name}</strong> : {coffee.price} €
              </p>
            </div>
          ))}
      </div>
    </section>
  );
}
