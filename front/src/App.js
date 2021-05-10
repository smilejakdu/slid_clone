import React from "react";
import "./App.css";
import Navbar from "./Layouts/Navbar/Navbar"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "./pages/Home";
import Products from "./pages/Products";
import Layout from "./Layouts/Layout"

function App() {
  return (
    <>
      <Router>
        <Layout>
          <Switch>
            <Route path="/my_reports" component={Home} />
            <Route path="/delete_reports" component={Products} />
          </Switch>
        </Layout>
      </Router>
    </>
  );
}

export default App;
