// @ts-ignore
import CanvasJSReact from "@canvasjs/react-charts"

import { useState } from 'react';
import { useEffect } from 'react';
import { useSocket } from "./useSocket";
import CarData from "./CarData";
import BatteryData from "./BatteryData";
//var CanvasJSReact = require('./canvasjs.react');
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

interface Data {
  power: number,
  speed: number,
  potench: number,
  mc_temp: number,
  accel: number
}
interface GraphProps {
  data: Data
}
const SpeedGraph = (props: GraphProps) => {
  // const socket = useSocket()
  // let data: Data = { speed: 0, steering_angle: 0 }

  const [currSpeed, setSpeed] = useState(0)
  const [currTime, setTime] = useState(0)

  const [points, updatePoints] = useState([{ x: 0, y: 0 }])
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
  useEffect(() => {
    const ticker = setInterval(() => {
      setTime(t => t + 10)
    }, 10)

    return () => clearInterval(ticker)
  })
  // useEffect(() => {
  //   const updateData = (raw: string) => {
  //     data = Object.assign(data, JSON.parse(raw))
  //     setSpeed(data.speed)
  //     setAngle(data.steering_angle)
  //     updatePoints([...points, { x: currTime, y: currSpeed }])
  //   }
  //   socket.onmessage = (message) => {
  //     updateData(message.data)
  //   }

  // }, [socket])
  useEffect(() => {
    setSpeed(props.data.speed)
    updatePoints([...points, { x: currTime, y: currSpeed }])
  }, [props.data])

  function clearGraph() {
    updatePoints([{ x: 0, y: 0 }]);
    setSpeed(0)
  }


  return (
    <div className="graph">
      <div className="display-data-static">
        <CarData speed={currSpeed} />
      </div>


      <CanvasJSChart options={options}
      /* onRef = {ref => this.chart = ref} */
      />
      <button className="reset" onClick={clearGraph}>Reset</button>

    </div>
  );

};

export default SpeedGraph;