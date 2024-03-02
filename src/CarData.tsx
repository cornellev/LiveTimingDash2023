import { useState, useEffect } from "react";
import { useSocket } from "./useSocket";
import SpeedGraph from "./Graph";

interface Data {
  speed: number;
  steering_angle: number;
}

/**
 * A component storing data about the car
 * @returns a component displaying the current speed and steering angle
 */
export default function CarData(props: Data) {
  // const socket = useSocket()
  // const [curr_speed, setSpeed] = useState(0);
  // const [speed_arr, setSpeedArr] = useState<number[]>([])
  // const [curr_steering_angle, setSteeringAngle] = useState(0);
  // let data: Data = { speed: 0, steering_angle: 0 }

  // useEffect(() => {
  //   const update = (rawData: string) => {
  //     data = Object.assign(data, JSON.parse(rawData))
  //     setSpeed(data.speed)
  //     setSteeringAngle(data.steering_angle)
  //     setSpeedArr(p => [...p, curr_speed])
  //   } //should be stringified in the server.js file before being sent here
  //   socket.onmessage = (event: MessageEvent) => {
  //     update(event.data)
  //   }
  //   socket.OPEN

  //   return () => {
  //     socket.close()
  //   }
  // }, [socket])

  return (<>
    <div className="car_data">
      <p className="measurement_nobg">CURRENT SPED: {props.speed}</p>
      <p className="measurement_nobg">STEERING ANGLE: {props.steering_angle}</p>
    </div>

  </>)
}