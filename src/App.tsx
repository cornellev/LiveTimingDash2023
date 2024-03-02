import './App.css'
import { SocketProvider } from './SocketProvider'
import Lapping from './Lapping'
import Header from './Header'
import BatteryData from './BatteryData'
import CarData from './CarData'
import SpeedGraph from './Graph'


function App() {
  return (
    <>
    <Header />
      <SocketProvider>
        <Lapping />
        {/* <BatteryData /> */}
      </SocketProvider>
    </>
  )
}

export default App
