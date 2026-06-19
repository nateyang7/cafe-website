// src/components/NavBar.tsx

export type NavigationLink = {
  name: string;
  icon: string;
};

type NavBarProps = {
  navigationLinks: NavigationLink[];
};

export default function NavBar({ navigationLinks }: NavBarProps) {
  return (
    <nav className="navBar">
      <ul>
        {navigationLinks.map((navigationLink) => (
          <li key={navigationLink.name.toLocaleLowerCase()}>
            <a href={"#" + navigationLink.name.toLocaleLowerCase()}>
              <img src={navigationLink.icon} />
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
