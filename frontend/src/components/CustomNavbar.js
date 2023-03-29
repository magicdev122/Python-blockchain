import React from "react";
import { Navbar, Nav } from "react-bootstrap";

function CustomNavbar() {
  return (
    <Navbar bg="light" expand="lg">
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="/">Home</Nav.Link>
          <br />
          <Nav.Link href="/blockchain">Blockchain</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default CustomNavbar;
