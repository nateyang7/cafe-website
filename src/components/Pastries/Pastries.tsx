// src/components/Pastries/Pastries.tsx

import { ConsumableType } from "../../data/consumable";
import { consumables } from "../../data/consumables";
import styles from "./Pastries.module.css";

export default function Pastries() {
  return (
    <section id="pastries" className={styles.pastries}>
      <h1>
        {"\u{1F950}"} Pastries {"\u{1F950}"}
      </h1>

      <div className={styles.pastriesContainer}>
        {consumables
          .filter((pastry) => pastry.type === ConsumableType.VIENNOISERIE)
          .map((pastry) => (
            <div className={styles.pastryDiv} key={pastry.id}>
              <img
                src={pastry.image}
                alt={pastry.name}
                className={styles.pastryImg}
              />
              <p>
                <strong>{pastry.name}</strong>: {pastry.price} €
              </p>
            </div>
          ))}
      </div>
    </section>
  );
}
