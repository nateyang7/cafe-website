// src/data/navigationLinks.ts

type NavigationLink = {
  name: string;
  icon: string;
};

export const navigationLinks: NavigationLink[] = [
  { name: "home", icon: home },
  { name: "coffees", icon: coffee },
  { name: "pastries", icon: pastry },
];
