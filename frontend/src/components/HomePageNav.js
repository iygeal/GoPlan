import React from 'react';
import { Container, Navbar, Nav } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/landingpage.css';

const Homepagenav = () => {
  return (
    <Navbar className="navbar navbar-expand-lg bg-body-tertiary">
      <Container fluid>
        <Navbar.Brand href="/home">
          <img className="logo" src="../static/images/gotravel logo.png" alt="GoTravel Logo" />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarSupportedContent" />
        <Navbar.Collapse id="navbarSupportedContent" className="justify-content-end">
          <form className="d-flex search" role="search">
            <input
              className="form-control me-2 search"
              type="search"
              placeholder="Search places and festivals"
              aria-label="Search"
            />
          </form>
          <Nav className="navbar-nav mb-2 mb-lg-0 align-items-lg-center align-items-md-start align-items-sm-start">
            <Nav.Item>
              <Nav.Link href="mainpage.html">Home</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="#festivals">Festivals</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <button className="nav-link btn-link" type="button">
                <img className="bell" src="../static/images/bell.png" alt="Notifications" />
              </button>
            </Nav.Item>
            <Nav.Item className="dropdown">
              <button
                className="nav-link dropdown-toggle btn-link"
                type="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <img className="user" src="../static/images/Male User.png" alt="User" />
              </button>
              <ul className="dropdown-menu">
                <li><a className="dropdown-item" href="profile.html">Profile</a></li>
                <li><button className="dropdown-item btn-link" type="button">Bookings</button></li>
                <li><button className="dropdown-item btn-link" type="button">Settings</button></li>
                <li><hr className="dropdown-divider" /></li>
                <li><a className="dropdown-item" href="index.html">Logout</a></li>
              </ul>
            </Nav.Item>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default Homepagenav;
