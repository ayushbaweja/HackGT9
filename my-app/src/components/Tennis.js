import React from "react";

function Tennis() {
    return (
      <div className="Lift">
          <div className="Header"> 
              <h2 style={{"marginTop": "0px", "font-size": "39px"}}>Which skill would you like to test? </h2>
                <button className="curlBtn">Forehand</button>
                <div><button className="squatBtn">Backhand</button></div>
          </div>
      </div>
    );
  }
  
  export default Tennis;
  