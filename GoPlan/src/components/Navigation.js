import React from 'react'
import { Container, Navbar, Nav } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/homepage.css';
import { useNavigate } from 'react-router-dom';


function Navigation() {

    const navigate = useNavigate(); // Hook to navigate between pages
    return (
        <div>
            <Container>
                <Navbar className='px-4' bg="light" expand="md" fixed="top">
                    <Navbar.Brand href="#home">
                        <img src="/assets/images/goplanlogo.png" className="logo" alt="Goplanlogo" />
                    </Navbar.Brand>
                    {/* This is the hamburger menu bar */}
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav" className="justify-content-end">
                        <Nav className="fs-5">
                            <Nav.Link href="#home">Home</Nav.Link>
                            <Nav.Link href="#features">Features</Nav.Link>
                            <Nav.Link href="#most-visited-places">Most Visited Places</Nav.Link>
                            <Nav.Link href="#festivals">Festivals</Nav.Link>
                            <Nav.Link onClick={() => navigate("/login")}>Login</Nav.Link>
                            <Nav.Link onClick={() => navigate("/signup")}>Sign Up</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Navbar>
            </Container>
        </div>
    )
}

export default Navigation