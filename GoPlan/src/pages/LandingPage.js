import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/landingpage.css';
import Container from 'react-bootstrap/Container';
import { useNavigate } from 'react-router-dom';
import Navigation from '../components/Navigation';


const LandingPage = () => {
  const navigate = useNavigate(); // Hook to navigate between pages
  return (
    <div>
      <Navigation/>
      <header className="text-center">
        <div className="container">
          <h1>Discover Nigeria Like Never Before</h1>
          <p>
            GoTravel aims to simplify the process of planning vacations by offering an easy-to-use platform for searching, organizing, and managing travel plans.
          </p>
          <div className="button-container">
            <button className="btn btn-outline-success" onClick={() => navigate("/login")}>Login</button>
            <button className="btn btn-success" onClick={() => navigate("/signup")}>Sign Up</button>
          </div>
        </div>
        <img
          src="/assets/images/zuma-3.png"
          className="container mt-4 header-img rounded"
          alt="zuma rock"
        />
      </header>

      <main>
        <section id="features" className="text-center py-5">
          <div className="container">
            <h1>Features</h1>
            <p>
              We plan to implement exciting features to make your vacation planning enjoyable.
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
            <div className="row g-3 custom-gallery">
              <div className="col-12 col-md-3">
                <img src="/assets/images/stock1.jpg" className="img-fluid rounded border border-secondary custom-image" alt="Stock 1" />
              </div>
              <div className="col-12 col-md-3">
                <img src="/assets/images/stock2.jpg" className="img-fluid rounded border border-secondary custom-image" alt="Stock 2" />
              </div>
              <div className="col-12 col-md-3">
                <img src="/assets/images/stock3.jpg" className="img-fluid rounded border border-secondary custom-image" alt="Stock 3" />
              </div>
              <div className="col-12 col-md-3">
                <img src="/assets/images/stock4.jpg" className="img-fluid rounded border border-secondary custom-image" alt="Stock 4" />
              </div>
            </div>
          </div>
        </section>

        <section id="festivals" className="py-5 text-white">
          <div className="text-center mt-5">
            <h1>Festivals</h1>
            <p className="features-description">Explore the various cultural festivals in Nigeria.</p>
            <div className="row gap-5 festivals-gallery justify-content-center py-5 mt-5">
              <div className="col-12 col-md-4 festivals-images">
                <img src="/assets/images/stock5.jpg" className="img-fluid border border-secondary" alt="Wrestling" />
                <div className="overlay-text">Wrestling</div>
              </div>
              <div className="col-12 col-md-4 festivals-images">
                <img src="/assets/images/stock6.jpg" className="img-fluid border border-secondary" alt="Igba Mmanyi Ukwu" />
                <div className="overlay-text">Igba Mmanyi Ukwu</div>
              </div>
              <div className="col-12 col-md-4 festivals-images">
                <img src="/assets/images/stock7.jpg" className="img-fluid border border-secondary" alt="Fulani" />
                <div className="overlay-text">Fulani</div>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="bg-light text-center text-lg-start">
        <Container className="p-4">
          <div className="text-center">
            <div className="my-5 mb-md-0">
              <img src="/assets/images/goplanlogo.png" className="logo my-3" alt="Goplanlogo" />
              <p>
                Discover Nigeria like never before with GoPlan. Explore the most visited places, festivals, and more.
              </p>
            </div>
          </div>
        </Container>
        <div className="text-center p-3" style={{ backgroundColor: 'rgba(0, 0, 0, 0.2)' }}>
          © 2024 Copyright:
          <a className="text-dark" href="https://github.com/VictorNalu/GoPlan/"> GoPlan Devs</a>
        </div>
      </footer>
    </div>

  );
};

export default LandingPage;
