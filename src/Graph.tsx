// @ts-ignore
import CanvasJSReact from "@canvasjs/react-charts"

import { useState } from 'react';
import { useEffect } from 'react';
//var CanvasJSReact = require('./canvasjs.react');
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

const SpeedGraph = () => {
  const [currSpeed, setSpeed] = useState(0)

  const [points, updatePoints] = useState([{ x: 0, y: 0 }])
  const [currX, updateX] = useState(0)
  const options = {
    title: {
      text: "Speed"
    },
    data: [{
      type: "line",
      dataPoints: points
    }],
    axisX: {
      title: "Time", //not yet tho bc learning setinterval has been difficult
      minimum: 0
    },
    axisY: {
      title: "Speed",
      minimum: 0,
      maximum: 20 //set this to abt 5 beyond max speed of car
    }
  }
  function updateStuff() {
    setSpeed(Math.random() * 15);
    updateX(currX + 1);
    updatePoints([...points, { x: currX, y: currSpeed }])

  };
  function clearGraph() {
    updatePoints([{ x: 0, y: 0 }]);
    setSpeed(0)
  }


  return (
    <div>
      <div className="speed_stuff">
        <p>Current Speed:</p>
        <p id="sped">{currSpeed.toFixed(2)}</p>
        <button className="speed_button" onClick={updateStuff}>Click me!</button>
        <button className="reset" onClick={clearGraph}>Reset</button>
      </div>
      <CanvasJSChart options={options}
      /* onRef = {ref => this.chart = ref} */
      />
    </div>
  );

};

export default SpeedGraph;