import React from "react";

function Skating() {
    return (
      <div className="Lift">
          <div className="Header"> 
              <h2 style={{"marginTop": "0px", "font-size": "39px"}}>Which skill would you like to test? </h2>
                <button className="curlBtn">Arabesque</button>
                <div><button className="squatBtn">Axel Jump</button></div>
          </div>
      </div>
    );
  }
  
export default Skating;
  