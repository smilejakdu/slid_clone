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
      title: "내 문서함",
      path: "/my_reports",
      cName: "nav-text",
    },
    {
      title: "삭제된 문서",
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
              <div style={{marginLeft:"30px"}}>
                <img
                  src={`${slid_logo_text}`}
                  alt=""
                  height="70"
                  style={{ background: "white" }}
                />
              </div>
              <div>
                <Link to="#" className={sidebar ? "menu-close" : "menu-bars"}>
                  <AiIcons.AiOutlineClose style={{ color: "white" }} />
                </Link>
              </div>
            </div>
{/* 로그인이 된다면 ==> 비회원은 작두키우기 , 로그인이 되어있지 않습니다. => 이메일주소 */}
            <div style={{color:"white"}}>
              비회원
            </div>
            <div style={{color:"white"}}>
              로그인이 되어있지 않습니다.
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
