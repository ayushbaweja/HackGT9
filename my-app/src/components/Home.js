import React from "react";
import './Home.css';
import { Routes, useNavigate, Route } from 'react-router-dom';

function Home() {
    const navigate = useNavigate();
    const lifting = () => {
      navigate('/lifting');
    };
    
    const skating = () => {
      navigate('/skating');
    };

    const tennis = () => {
      navigate('/tennis');
    };

    const archery = () => {
      navigate('/archery');
    };

    const volleyball = () => {
      navigate('/volleyball');
    };

    return (
        <div className="Home">
        <div className="Sport">
          Welcome to Muscle Movement Master
          <div style={{"marginTop": "20px", "font-size": "39px"}}> Choose your Sport </div>
          <button className="button" onClick={lifting}>Weight Lifting</button>
          <div>
          <button className="button" onClick={skating}>Figure Skating</button>
          </div>
          <div>
          <button className="button" onClick={tennis}>Tennis</button>
          </div>
          <div>
          <button className="button" onClick={archery}>Archery</button>
          </div>
          <div>
          <button className="button" onClick={volleyball}>Volleyball</button>
          </div>
        </div>
    </div>
    );
  }
  
  export default Home;
  