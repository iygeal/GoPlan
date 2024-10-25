import React from 'react';
import Homepagenav from '../components/HomePageNav';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/landingpage.css';

const HomePage = () => {
  return (
    <div>
      <Homepagenav />
      <header className="text-center py-5 mb-5">
        <iframe
          className="container bg-secondary"
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3940.228028548445!2d7.494207375657828!3d9.042952688769068!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x104e0b9696e1bd7b%3A0x5adc4afcc682ac6b!2sUmuahia%20Cl%2C%20Garki%2C%20Abuja%20900103%2C%20Federal%20Capital%20Territory!5e0!3m2!1sen!2sng!4v1721396057815!5m2!1sen!2sng"
          allowFullScreen=""
          loading="lazy"
          referrerPolicy="no-referrer-when-downgrade"
          title="Google Maps"
        ></iframe>
      </header>
      <main>
        <section id="features" className="py-5 mb-5">
          <div className="container">
            <div className="d-flex justify-content-between align-items-center">
              <h1>TRAVELS</h1>
              <a href="/createplan" className="new_travel_btn">
                <span>+</span> Plan New Travel
              </a>
            </div>
            <p className="ps-5 py-3">
              Your travel log is empty.
              <button className="new_travel" onClick={() => {/* Add your click handler here */}}>
                Plan new travel
              </button>
            </p>
          </div>
        </section>
        <section id="most-visited-places" className="py-5">
          <div className="container">
            <h1>Most Visited Places</h1>
            <p className="paragraphs">
              Explore Nigeria's top attractions, from bustling cities to natural wonders.
            </p>
            <div className="row g-3">
              <div className="col-md-3">
                <img
                  src="../static/images/stock1.jpg"
                  className="img-fluid rounded border border-secondary"
                  alt=""
                />
              </div>
              <div className="col-md-3">
                <img
                  src="../static/images/stock2.jpg"
                  className="img-fluid rounded border border-secondary"
                  alt=""
                />
              </div>
              <div className="col-md-3">
                <img
                  src="../static/images/stock3.jpg"
                  className="img-fluid rounded border border-secondary"
                  alt=""
                />
              </div>
              <div className="col-md-3">
                <img
                  src="../static/images/stock4.jpg"
                  className="img-fluid rounded border border-secondary"
                  alt=""
                />
              </div>
            </div>
          </div>
        </section>
        <section id="festivals" className="py-5 text-white">
          <div className="text-center mt-5">
            <h1>Festivals</h1>
            <p className="paragraphs">
              Explore the various cultural festivals in Nigeria.
            </p>
            <div className="row gap-5 festivals-gallery justify-content-center py-5 mt-5">
              <div className="col col-md-4 festivals-images">
                <img
                  src="../static/images/stock5.jpg"
                  className="img-fluid border border-secondary"
                  alt=""
                />
                <div className="overlay-text">Festival 1 placeholder</div>
              </div>
              <div className="col col-md-4 festivals-images">
                <img
                  src="../static/images/stock6.jpg"
                  className="img-fluid border border-secondary"
                  alt=""
                />
                <div className="overlay-text">Festival 1 placeholder</div>
              </div>
              <div className="col col-md-4 festivals-images">
                <img
                  src="../static/images/stock7.jpg"
                  className="img-fluid border border-secondary"
                  alt=""
                />
                <div className="overlay-text">Festival 1 placeholder</div>
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
