import { useState, useEffect } from "react";
import { useSocket } from "./useSocket";

interface Data {
  speed: number;
  steering_angle: number;
}

export default function CarData() {
  const socket = useSocket()
  const [curr_speed, setSpeed] = useState(0);
  const [speed_arr, setSpeedArr] = useState<number[]>([])
  const [curr_steering_angle, setSteeringAngle] = useState(0);
  let data: Data = { speed: 0, steering_angle: 0 }

  useEffect(() => {
    const update = (rawData: string) => {
      data = Object.assign(data, JSON.parse(rawData))
      setSpeed(data.speed)
      setSteeringAngle(data.steering_angle)
      setSpeedArr(p => [...p, curr_speed])
    } //should be stringified in the server.js file before being sent here
    socket.onmessage = (event: MessageEvent) => {
      update(event.data)
    }
    socket.OPEN

    return () => {
      socket.close()
    }
  }, [socket])

  return (
    <div>
      <p className="measurement">CURRENT SPEED: {curr_speed}</p>
      <p className="measurement">STEERING ANGLE: {curr_steering_angle}</p>
    </div>
  )
}