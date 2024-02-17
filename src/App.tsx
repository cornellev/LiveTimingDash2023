import './App.css'
import { SocketProvider } from './SocketProvider'
import Lapping from './Lapping'
import BatteryData from './BatteryData'
import CarData from './CarData'
import SpeedGraph from './Graph'


function App() {
  return (
    <>
      <SocketProvider>
        <Lapping />
        {/* <BatteryData /> */}
      </SocketProvider>
    </>
  )
}

export default App
