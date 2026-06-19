// src/App.tsx

import "./App.css";

import type { NavigationLink } from "./components/NavBar.tsx";

import NavBar from "./components/NavBar.tsx";
import Home from "./components/Home.tsx";
import Coffees from "./components/Coffees.tsx";
import Pastries from "./components/Pastries.tsx";

import home from "./assets/icons/home-icon.svg";
import coffee from "./assets/icons/coffee-icon.svg";
import pastry from "./assets/icons/pastry-icon.svg";

function App() {
  const navigationLinks: NavigationLink[] = [
    { name: "home", icon: home },
    { name: "coffees", icon: coffee },
    { name: "pastries", icon: pastry },
  ];

  return (
    <>
      <header>
        <NavBar navigationLinks={navigationLinks} />
      </header>

      <main>
        <Home />
        <Coffees />
        <Pastries />
      </main>

      <footer>&copy; Café 2026</footer>
    </>
  );
}

export default App;
