import React from "react";

function Volleyball() {
    return (
      <div className="Lift">
          <div className="Header"> 
              <h2 style={{"marginTop": "0px", "font-size": "39px"}}>Which skill would you like to test? </h2>
                <button className="curlBtn">Spike</button>
                <div><button className="squatBtn">Set</button></div>
          </div>
      </div>
    );
  }
  
  export default Volleyball;