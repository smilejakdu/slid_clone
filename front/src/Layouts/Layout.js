import Navigation  from "./Navbar/Navbar";
import React from "react";

const Layout = ({ children }) => {
  return (
    <div>
      <Navigation />
      <div style={{ backgroundColor: '#f8f8f9' }}>{children}</div>
    </div>
  );
};

export default Layout;
