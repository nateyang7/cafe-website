// src/App.tsx

import "./App.css";
import NavBar from "./components/NavBar/NavBar.tsx";

import home from "./assets/icons/home-icon.svg";
import coffee from "./assets/icons/coffee-icon.svg";
import pastry from "./assets/icons/pastry-icon.svg";

function App() {
  const navigationLinks = [
    { name: "home", icon: home },
    { name: "coffees", icon: coffee },
    { name: "pastries", icon: pastry },
  ];

  return (
    <>
      <NavBar navigationLinks={navigationLinks} />
    </>
  );
}

export default App;
