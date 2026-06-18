// src/components/NavBar.tsx

import styles from "./NavBar.module.css";

type NavigationLink = {
  name: string;
  icon: string;
};

type NavBarProps = {
  navigationLinks: NavigationLink[];
};

export default function NavBar({ navigationLinks }: NavBarProps) {
  return (
    <nav className={styles.navbar}>
      <ul className={styles.navbarUl}>
        {navigationLinks.map((navigationLink) => (
          <li
            className={styles.navBarLi}
            key={navigationLink.name.toLocaleLowerCase()}
          >
            <a href={"#" + navigationLink.name.toLocaleLowerCase()}>
              <img src={navigationLink.icon} />
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
