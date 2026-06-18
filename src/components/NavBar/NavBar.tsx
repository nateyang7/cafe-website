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
      {navigationLinks.map((navigationLink) => (
        <a
          href={"#" + navigationLink.name.toLocaleLowerCase()}
          key={navigationLink.name.toLocaleLowerCase()}
        >
          <img src={navigationLink.icon} />
        </a>
      ))}
    </nav>
  );
}
