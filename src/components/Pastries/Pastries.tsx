// src/components/Pastries/Pastries.tsx

import { ConsumableType } from "../../data/consumable";
import { consumables } from "../../data/consumables";
import styles from "./Pastries.module.css";

export default function Pastries() {
  return (
    <section id="pastries" className={styles.pastries}>
      <h1>Pastries</h1>

      <div className={styles.pastriesContainer}>
        {consumables
          .filter((pastry) => pastry.type === ConsumableType.VIENNOISERIE)
          .map((pastry) => (
            <div className="consumable" key={pastry.id}>
              <img
                src={pastry.image}
                alt={pastry.name}
                className={styles.pastryShowcase}
              />
              <ul>
                <li>{pastry.name}</li>
                <li>{pastry.price} €</li>
              </ul>
            </div>
          ))}
      </div>
    </section>
  );
}
