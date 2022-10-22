import React from "react";
import './Lifting.css';
import { useNavigate } from 'react-router-dom';

// curl up, squat
function Lifting() {
    const navigate = useNavigate();

    const curls = () => {
      navigate('/lifting/curls');
    };

    const squats = () => {
      navigate('/lifting/squats');
    };

    return (
      <div className="Lift">
          <div className="Header"> 
              <h2 style={{"marginTop": "0px", "font-size": "39px"}}>Which exercise would you like to test? </h2>
                <button className="curlBtn" onClick={curls}>Bicep Curls</button>
                <div><button className="squatBtn" onClick={squats}>Squats</button></div>
          </div>
      </div>
    );
  }
  
  export default Lifting;
  