import React from "react";

function Archery() {
    return (
      <div className="Lift">
          <div className="Header"> 
              <h2 style={{"marginTop": "0px", "font-size": "39px"}}>Which skill would you like to test? </h2>
                <button className="curlBtn">Transfer</button>
                <div><button className="squatBtn">Release</button></div>
          </div>
      </div>
    );
  }
  
  export default Archery;
  