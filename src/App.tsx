import useWebSocket, { ReadyState } from 'react-use-websocket'
import { useState, useEffect } from 'react'
import './App.css'
import { SocketProvider } from './SocketProvider'
import Lapping from './Lapping'
import Header from './Header'
// import BatteryData from './BatteryData'
// import CarData from './CarData'
// import SpeedGraph from './Graph'

let SOCKET_URL = "ws://" + location.host //livetimingdash.heroku.com for comp deployment
interface Data {
  power: number,
  speed: number,
  potench: number,
  mc_temp: number,
  accel: number
}
function App() {
  // const [currMsg, setMsg] = useState<string>("")
  // const { lastMessage, readyState } = useWebSocket(SOCKET_URL, { onOpen: () => console.log("socket opened"), shouldReconnect: (closeEvent) => true, retryOnError: true, share: true });
  // console.log("readystate:" + readyState)
  // let data: Data = { power: 0, speed: 0, potench: 0, mc_temp: 0, accel: 0 }
  // useEffect(() => {
  //   if (lastMessage != null) {
  //     setMsg(lastMessage.toString())
  //     data = Object.assign(data, JSON.parse(currMsg))
  //   }
  // }, [lastMessage])

  return (
    <>
      <Header />
      <SocketProvider>
        <Lapping />
      </SocketProvider>
      {/* <BatteryData /> */}
    </>
  )
}

export default App
