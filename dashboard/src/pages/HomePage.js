import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/Homepage.css'; 
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

const HomePage = () => {
  return (
    <div>
      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="#home">
            <img src="/assets/images/goplanlogo.png" className="logo" alt="Goplanlogo" />
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav" className="justify-content-end">
            <Nav className="fs-5">
              <Nav.Link href="#home">Home</Nav.Link>
              <Nav.Link href="#features">Features</Nav.Link>
              <Nav.Link href="#most-visited-places">Most Visited Places</Nav.Link>
              <Nav.Link href="#festivals">Festivals</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <header className="text-center py-5 mt-5">
        <div className="container">
          <h1>Discover Nigeria Like Never Before</h1>
          <p>
            GoTravel aims to simplify the process of planning vacations by offering an easy-to-use platform for searching, organizing, and managing travel plans.
          </p>
          <div className="d-flex justify-content-center gap-4 mt-4">
            <button className="btn btn-outline-success">Login</button>
            <button className="btn btn-success">Sign Up</button>
          </div>
        </div>
        <img
          src="/assets/images/zuma-3.png"
          className="container mt-4 header-img rounded"
          alt="zuma rock"
        />
      </header>

      <main>
        <section id="features" className="text-center py-5 mt-5">
          <div className="container">
            <h1>Features</h1>
            <p>
              We have implemented exciting features to make your vacation planning enjoyable.
            </p>
            <div className="row g-5 icons">
              <div className="col-md-4">
                <img
                  src="/assets/images/customer-feedback-concept-illustration.png"
                  className="img-fluid icon-img"
                  alt=""
                />
                <p className="pt-4">See Recommendations</p>
              </div>
              <div className="col-md-4">
                <img
                  src="/assets/images/Friends.png"
                  className="img-fluid icon-img pt-5"
                  alt=""
                />
                <p className="pt-4">Plan With Friends</p>
              </div>
              <div className="col-md-4">
                <img
                  src="/assets/images/family-traveling.png"
                  className="img-fluid icon-img pb-2"
                  alt=""
                />
                <p className="pt-4">Book Flights and Hotels</p>
              </div>
            </div>
          </div>
        </section>

        <section id="most-visited-places" className="text-center py-5">
          <div className="container">
            <h1>Most Visited Places</h1>
            <p>Explore Nigeria's top attractions, from bustling cities to natural wonders.</p>
            <div className="row g-3">
              <div className="col-md-3">
                <img src="/assets/images/stock1.jpg" className="img-fluid rounded border border-secondary" alt="" />
              </div>
              <div className="col-md-3">
                <img src="/assets/images/stock2.jpg" className="img-fluid rounded border border-secondary" alt="" />
              </div>
              <div className="col-md-3">
                <img src="/assets/images/stock3.jpg" className="img-fluid rounded border border-secondary" alt="" />
              </div>
              <div className="col-md-3">
                <img src="/assets/images/stock4.jpg" className="img-fluid rounded border border-secondary" alt="" />
              </div>
            </div>
          </div>
        </section>

        <section id="festivals" className="py-5 text-white">
          <div className="text-center mt-5">
            <h1>Festivals</h1>
            <p className="features-description">Explore the various cultural festivals in Nigeria.</p>
            <div className="row gap-5 festivals-gallery justify-content-center py-5 mt-5">
              <div className="col col-md-4 festivals-images">
                <img src="/assets/images/stock5.jpg" className="img-fluid border border-secondary" alt="" />
                <div className="overlay-text">Wrestling</div>
              </div>
              <div className="col col-md-4 festivals-images">
                <img src="/assets/images/stock6.jpg" className="img-fluid border border-secondary" alt="" />
                <div className="overlay-text">Igba Mmanyi Ukwu</div>
              </div>
              <div className="col col-md-4 festivals-images">
                <img src="/assets/images/stock7.jpg" className="img-fluid border border-secondary" alt="" />
                <div className="overlay-text">Fulani</div>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="bg-light text-center py-3">
        <p className="mt-4">Copyright © 2024. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;
