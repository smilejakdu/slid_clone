import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.scss';
import { IconContext } from 'react-icons';
import * as AiIcons from "react-icons/ai";
import * as FaIcons from 'react-icons/fa';
import slid_logo_text from '../../utils/image/slid_logo_text.png'


function Navbar() {
  const [sidebar, setSidebar] = useState(false);
  const showSidebar = () => setSidebar(!sidebar);

  const SidebarData = [
    {
      title: "내문서함",
      path: "/my_reports",
      cName: "nav-text",
    },
    {
      title: "삭제된문서",
      path: "/delete_reports",
      cName: "nav-text",
    },
  ];

  return (
    <>
      <IconContext.Provider value={{ color: "#fff" }}>
        <div className="navbar">
          <Link to="#" className="menu-bars">
            <FaIcons.FaBars onClick={showSidebar} />
          </Link>
        </div>
        <div className={sidebar ? "nav-menu active" : "nav-menu"}>
          <ul className="nav-menu-items" onClick={showSidebar}>
            <div className="navbar-toggle">
              <img src={`${slid_logo_text}`} alt="" height="70" />
              <Link to="#" className="menu-bars">
                <AiIcons.AiOutlineClose style={{color:'black'}}/>
              </Link>
            </div>
            {SidebarData.map((item, index) => (
              <div>
                <li key={index} className={item.cName}>
                  <Link to={item.path}>
                    <span>{item.title}</span>
                  </Link>
                </li>
              </div>
            ))}
          </ul>
        </div>
      </IconContext.Provider>
    </>
  );
}

export default Navbar;
